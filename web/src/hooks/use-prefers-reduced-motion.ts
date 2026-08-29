import { useEffect, useState } from 'react'

const QUERY = '(prefers-reduced-motion: reduce)'

/**
 * Whether the reader has asked for less motion.
 *
 * FRONTEND-PLAN 2.7 and 6.3: when this is true the seal becomes an immediate
 * state change rather than a timed one. The meaning is never dropped — only the
 * animation that carries it.
 */
export function usePrefersReducedMotion(): boolean {
  const [reduced, setReduced] = useState(
    () => typeof window !== 'undefined' && window.matchMedia(QUERY).matches,
  )

  useEffect(() => {
    const media = window.matchMedia(QUERY)
    const onChange = () => setReduced(media.matches)
    media.addEventListener('change', onChange)
    onChange()
    return () => media.removeEventListener('change', onChange)
  }, [])

  return reduced
}
