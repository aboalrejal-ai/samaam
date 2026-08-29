/**
 * Typed client for the Samaam service.
 *
 * Two things this file is careful about:
 *
 * 1. `403 Policy Violation` is a result, not a failure. It is the whole point
 *    of the demo. The device and data endpoints return the full decision in
 *    FastAPI's `detail` envelope on rejection, so those calls resolve with the
 *    decision and the HTTP status rather than throwing.
 * 2. A dead server and a rejected request are different things and must never
 *    look alike on screen. Transport failures raise `SamaamOfflineError`.
 */

import type {
  AuditEntry,
  DataRequestBody,
  DataRequestResponse,
  EvaluationRequest,
  EvaluationResponse,
  FrameworkResponse,
  HealthResponse,
  KbCollection,
  KbGap,
  KbRecord,
  KbSearchResponse,
  Scenario,
  PolicyPayload,
} from '@/types/api'

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

/** The Samaam service could not be reached at all. */
export class SamaamOfflineError extends Error {
  constructor(readonly cause: unknown) {
    super(`Could not reach the Samaam service at ${API_BASE_URL}`)
    this.name = 'SamaamOfflineError'
  }
}

/** The service answered, but with an error the caller did not expect. */
export class SamaamApiError extends Error {
  constructor(
    readonly status: number,
    readonly body: unknown,
    message?: string,
  ) {
    super(message ?? `Samaam service returned HTTP ${status}`)
    this.name = 'SamaamApiError'
  }
}

/** A policy-gated call: the outcome carries the status the device saw. */
export interface GatedOutcome<T> {
  /** 200 when the worklist was released, 403 when the policy node withheld it. */
  httpStatus: number
  result: T
}

interface RequestOptions {
  signal?: AbortSignal
}

function url(path: string, params?: Record<string, string | number | boolean | undefined>) {
  const target = new URL(path, API_BASE_URL)
  for (const [key, value] of Object.entries(params ?? {})) {
    if (value !== undefined) target.searchParams.set(key, String(value))
  }
  return target.toString()
}

async function send(
  path: string,
  init: RequestInit,
  params?: Record<string, string | number | boolean | undefined>,
): Promise<Response> {
  try {
    return await fetch(url(path, params), {
      ...init,
      headers: { Accept: 'application/json', ...init.headers },
    })
  } catch (cause) {
    throw new SamaamOfflineError(cause)
  }
}

async function readJson(response: Response): Promise<unknown> {
  const text = await response.text()
  if (!text) return null
  try {
    return JSON.parse(text) as unknown
  } catch {
    throw new SamaamApiError(response.status, text, 'Samaam service returned a non-JSON body')
  }
}

async function get<T>(
  path: string,
  params?: Record<string, string | number | boolean | undefined>,
  options?: RequestOptions,
): Promise<T> {
  const response = await send(path, { method: 'GET', signal: options?.signal }, params)
  const body = await readJson(response)
  if (!response.ok) throw new SamaamApiError(response.status, body)
  return body as T
}

/**
 * POST to an endpoint that mirrors the device status code. 403 resolves with
 * the decision unwrapped from FastAPI's `detail` envelope.
 */
async function postGated<TBody, TResult>(
  path: string,
  body: TBody,
  options?: RequestOptions,
): Promise<GatedOutcome<TResult>> {
  const response = await send(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
    signal: options?.signal,
  })
  const payload = await readJson(response)

  if (response.ok) {
    return { httpStatus: response.status, result: payload as TResult }
  }

  const detail = (payload as { detail?: unknown } | null)?.detail
  const isDecision =
    response.status === 403 &&
    typeof detail === 'object' &&
    detail !== null &&
    'verdict' in detail

  if (isDecision) {
    return { httpStatus: response.status, result: detail as TResult }
  }
  throw new SamaamApiError(response.status, payload)
}

/* ── Endpoints ──────────────────────────────────────────────────────── */

export function getHealth(options?: RequestOptions): Promise<HealthResponse> {
  return get<HealthResponse>('/health', undefined, options)
}

export function getScenarios(options?: RequestOptions): Promise<Scenario[]> {
  return get<Scenario[]>('/scenarios', undefined, options)
}

/** Evaluates without touching the device. Returns 200 even when blocked. */
export function evaluate(
  body: EvaluationRequest,
  options?: RequestOptions,
): Promise<EvaluationResponse> {
  return send(
    '/evaluate',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      signal: options?.signal,
    },
  ).then(async (response) => {
    const payload = await readJson(response)
    if (!response.ok) throw new SamaamApiError(response.status, payload)
    return payload as EvaluationResponse
  })
}

/** Hands the worklist to the scanner. 403 means it never got there. */
export function executeOnDevice(
  body: EvaluationRequest,
  options?: RequestOptions,
): Promise<GatedOutcome<EvaluationResponse>> {
  return postGated<EvaluationRequest, EvaluationResponse>('/device/execute', body, options)
}

/**
 * Puts a decision that has already been taken into words.
 *
 * Deliberately a second call. The policy node decides in milliseconds and the
 * model takes tens of seconds; binding them would make a refusal look slow,
 * and a refusal has to land the instant the button is pressed.
 */
export async function explainDecision(
  policy: PolicyPayload,
  options?: RequestOptions,
): Promise<string> {
  const response = await send('/explain', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ policy }),
    signal: options?.signal,
  })
  const payload = (await readJson(response)) as { explanation?: string } | null
  return payload?.explanation ?? ''
}

/** The privacy path. Admits no clinical override. */
export function requestData(
  body: DataRequestBody,
  options?: RequestOptions,
): Promise<GatedOutcome<DataRequestResponse>> {
  return postGated<DataRequestBody, DataRequestResponse>('/data/request', body, options)
}

export interface KbSearchParams {
  q: string
  collection?: KbCollection
  top_k?: number
  verified_only?: boolean
}

export function searchKb(
  { q, collection = 'policies', top_k = 6, verified_only = true }: KbSearchParams,
  options?: RequestOptions,
): Promise<KbSearchResponse> {
  return get<KbSearchResponse>('/kb/search', { q, collection, top_k, verified_only }, options)
}

export function getKbRecord(recordId: string, options?: RequestOptions): Promise<KbRecord> {
  return get<KbRecord>(`/kb/record/${encodeURIComponent(recordId)}`, undefined, options)
}

export function getKbGaps(options?: RequestOptions): Promise<KbGap[]> {
  return get<KbGap[]>('/kb/gaps', undefined, options)
}

export function getAudit(options?: RequestOptions): Promise<AuditEntry[]> {
  return get<AuditEntry[]>('/audit', undefined, options)
}

export function getFramework(options?: RequestOptions): Promise<FrameworkResponse> {
  return get<FrameworkResponse>('/framework', undefined, options)
}
