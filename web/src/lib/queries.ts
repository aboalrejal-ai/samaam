import { useMutation, useQuery } from '@tanstack/react-query'
import {
  evaluate,
  executeOnDevice,
  getAudit,
  getConnectors,
  getFramework,
  getHealth,
  getKbGaps,
  getKbRecord,
  getScenarios,
  requestData,
  pullFhirPatient,
  searchKb,
  testConnector,
  type KbSearchParams,
} from '@/lib/api'
import { queryClient } from '@/lib/query-client'
import type { DataRequestBody, EvaluationRequest } from '@/types/api'

export const queryKeys = {
  health: ['health'] as const,
  scenarios: ['scenarios'] as const,
  audit: ['audit'] as const,
  framework: ['framework'] as const,
  connectors: ['connectors'] as const,
  kbGaps: ['kb', 'gaps'] as const,
  kbRecord: (recordId: string) => ['kb', 'record', recordId] as const,
  kbSearch: (params: KbSearchParams) => ['kb', 'search', params] as const,
}

/**
 * Polls /health so a dead server is visible at a glance instead of being
 * discovered by a click that fails in front of the judges.
 */
export function useHealth() {
  return useQuery({
    queryKey: queryKeys.health,
    queryFn: ({ signal }) => getHealth({ signal }),
    refetchInterval: 10_000,
    refetchIntervalInBackground: true,
    staleTime: 0,
    retry: false,
  })
}

export function useScenarios() {
  return useQuery({
    queryKey: queryKeys.scenarios,
    queryFn: ({ signal }) => getScenarios({ signal }),
    staleTime: Infinity,
  })
}

export function useAudit() {
  return useQuery({
    queryKey: queryKeys.audit,
    queryFn: ({ signal }) => getAudit({ signal }),
    staleTime: 0,
  })
}

export function useFramework() {
  return useQuery({
    queryKey: queryKeys.framework,
    queryFn: ({ signal }) => getFramework({ signal }),
    staleTime: Infinity,
  })
}

export function useKbGaps() {
  return useQuery({
    queryKey: queryKeys.kbGaps,
    queryFn: ({ signal }) => getKbGaps({ signal }),
    staleTime: Infinity,
  })
}

export function useKbRecord(recordId: string | null) {
  return useQuery({
    queryKey: queryKeys.kbRecord(recordId ?? ''),
    queryFn: ({ signal }) => getKbRecord(recordId as string, { signal }),
    enabled: recordId !== null && recordId.length > 0,
  })
}

export function useKbSearch(params: KbSearchParams, enabled = true) {
  return useQuery({
    queryKey: queryKeys.kbSearch(params),
    queryFn: ({ signal }) => searchKb(params, { signal }),
    enabled: enabled && params.q.trim().length >= 2,
  })
}

export function useEvaluate() {
  return useMutation({ mutationFn: (body: EvaluationRequest) => evaluate(body) })
}

/** Submitting to the device writes audit entries, so the trail is invalidated. */
export function useExecuteOnDevice() {
  return useMutation({
    mutationFn: (body: EvaluationRequest) => executeOnDevice(body),
    onSettled: () => queryClient.invalidateQueries({ queryKey: queryKeys.audit }),
  })
}

export function useRequestData() {
  return useMutation({
    mutationFn: (body: DataRequestBody) => requestData(body),
    onSettled: () => queryClient.invalidateQueries({ queryKey: queryKeys.audit }),
  })
}

/**
 * The connector inventory. Polled, because the DICOM card changes on its own:
 * a scanner querying the worklist registers itself without anyone clicking.
 */
export function useConnectors() {
  return useQuery({
    queryKey: queryKeys.connectors,
    queryFn: ({ signal }) => getConnectors({ signal }),
    refetchInterval: 15_000,
    retry: false,
  })
}

/**
 * A live probe, deliberately a mutation rather than a query: it opens a real
 * socket, so it fires when a person asks for it and is never served from cache.
 */
export function useConnectorTest() {
  return useMutation({
    mutationFn: (connectorId: string) => testConnector(connectorId),
    onSettled: () => queryClient.invalidateQueries({ queryKey: queryKeys.connectors }),
  })
}

export function useFhirPull() {
  return useMutation({
    mutationFn: (patientId: string) => pullFhirPatient(patientId),
  })
}
