import { useCallback, useEffect, useMemo, useState } from 'react'
import { usePrefersReducedMotion } from '@/hooks/use-prefers-reduced-motion'
import { PIPELINE_NODES } from '@/types/api'

/** Node P: where the valve is. The token waits here for the verdict. */
export const GATE_INDEX = PIPELINE_NODES.indexOf('P')
export const SINK_INDEX = PIPELINE_NODES.length - 1

/** The calm descent, FRONTEND-PLAN 2.4. */
export const NODE_TRANSIT_MS = 180
/** The seal, FRONTEND-PLAN 2.5. The one sharp motion in the product. */
export const SEAL_MS = 90

export type NodeState = 'idle' | 'active' | 'passed' | 'sealed' | 'unreached'

export interface PipelineTransit {
  /** Index of the node the token occupies. `null` before anything is sent. */
  position: number | null
  /** The valve is shut: the worklist stopped at P and never reached the device. */
  sealed: boolean
  /**
   * P has been sealed at least once in this session. Survives an override —
   * FRONTEND-PLAN 2.6: the incident is never erased.
   */
  scarred: boolean
  /** The token has arrived and is no longer moving. */
  settled: boolean
  reducedMotion: boolean
  /** How long the token's current move takes, in ms. Zero under reduced motion. */
  stepMs: number
  stateOf: (index: number) => NodeState
  /** The token enters at SRC and descends to the gate to await the verdict. */
  begin: () => void
  /** The verdict blocked. The valve shuts at P. */
  seal: () => void
  /** The verdict released, or an override reopened the valve. Runs to SINK. */
  release: () => void
  reset: () => void
}

interface TransitState {
  /** `null` while dormant; otherwise the node the token has reached. */
  position: number | null
  /** Where the token is headed. */
  target: number
  sealed: boolean
  scarred: boolean
}

const DORMANT: TransitState = { position: null, target: 0, sealed: false, scarred: false }

/**
 * Drives the worklist token down the seven Y.3172 nodes.
 *
 * The token descends to P and holds there, because P is where the decision is
 * actually made — so a slow server reads as deliberation at the gate rather
 * than as a stalled animation. From P it either runs on to SINK or the valve
 * shuts on it.
 */
export function usePipelineTransit(): PipelineTransit {
  const reducedMotion = usePrefersReducedMotion()
  const [state, setState] = useState<TransitState>(DORMANT)
  const { position, target, sealed, scarred } = state

  // One step per tick. Re-running on `position` chains the steps and gives
  // clean cancellation if the outcome arrives mid-descent.
  useEffect(() => {
    if (position === null || position >= target) return
    if (reducedMotion) {
      setState((prev) => ({ ...prev, position: prev.target }))
      return
    }
    const timer = window.setTimeout(
      () =>
        setState((prev) => ({
          ...prev,
          position: Math.min((prev.position ?? 0) + 1, prev.target),
        })),
      NODE_TRANSIT_MS,
    )
    return () => window.clearTimeout(timer)
  }, [position, target, reducedMotion])

  const begin = useCallback(() => {
    // A fresh attempt reopens the valve but keeps the scar of the last one.
    setState((prev) => ({
      position: reducedMotion ? GATE_INDEX : 0,
      target: GATE_INDEX,
      sealed: false,
      scarred: prev.scarred,
    }))
  }, [reducedMotion])

  const seal = useCallback(() => {
    setState((prev) => ({ ...prev, target: GATE_INDEX, sealed: true, scarred: true }))
  }, [])

  const release = useCallback(() => {
    setState((prev) => ({ ...prev, target: SINK_INDEX, sealed: false }))
  }, [])

  const reset = useCallback(() => setState(DORMANT), [])

  const stateOf = useCallback(
    (index: number): NodeState => {
      if (position === null) return 'idle'
      if (sealed) {
        if (index < GATE_INDEX) return 'passed'
        if (index === GATE_INDEX) return 'sealed'
        return 'unreached'
      }
      if (index < position) return 'passed'
      if (index > position) return 'idle'
      return position === target ? 'passed' : 'active'
    },
    [position, sealed, target],
  )

  return useMemo(
    () => ({
      position,
      sealed,
      scarred,
      settled: position !== null && position === target,
      reducedMotion,
      stepMs: reducedMotion ? 0 : sealed ? SEAL_MS : NODE_TRANSIT_MS,
      stateOf,
      begin,
      seal,
      release,
      reset,
    }),
    [position, target, sealed, scarred, reducedMotion, stateOf, begin, seal, release, reset],
  )
}