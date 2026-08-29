import { useCallback, useEffect, useState } from 'react'
import type { KbCollection } from '@/types/api'
import { KB_COLLECTIONS } from '@/types/api'

/**
 * Past searches, kept in the browser.
 *
 * Same shape as `samaam.theme` and `samaam.language`: every read and write is
 * guarded, because storage throws in a private window and in browsers set to
 * block site data — and a locked-down browser must not break the demo. What
 * comes back out is validated rather than trusted; the value is user-writable.
 */
const STORAGE_KEY = 'samaam.kb.history'
const LIMIT = 20

export interface SearchHistoryEntry {
  id: string
  q: string
  collection: KbCollection
  verifiedOnly: boolean
  at: string
}

function isEntry(value: unknown): value is SearchHistoryEntry {
  if (typeof value !== 'object' || value === null) return false
  const e = value as Record<string, unknown>
  return (
    typeof e.id === 'string' &&
    typeof e.q === 'string' &&
    e.q.trim().length > 0 &&
    typeof e.at === 'string' &&
    typeof e.verifiedOnly === 'boolean' &&
    (KB_COLLECTIONS as readonly string[]).includes(e.collection as string)
  )
}

function read(): SearchHistoryEntry[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) return []
    const parsed: unknown = JSON.parse(raw)
    return Array.isArray(parsed) ? parsed.filter(isEntry).slice(0, LIMIT) : []
  } catch {
    return []
  }
}

function write(entries: SearchHistoryEntry[]) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(entries))
  } catch {
    // Ignored: history is a convenience, not a requirement.
  }
}

export function useSearchHistory() {
  const [history, setHistory] = useState<SearchHistoryEntry[]>([])

  // Read after mount rather than during render: the initialiser would run on
  // the server-render path too, and storage is a browser-only capability.
  useEffect(() => setHistory(read()), [])

  const remember = useCallback(
    (entry: Omit<SearchHistoryEntry, 'id' | 'at'>) => {
      const q = entry.q.trim()
      if (q.length < 2) return
      setHistory((prev) => {
        // The same question in the same collection is one entry, moved to the
        // top — not a second row saying the same thing.
        const rest = prev.filter(
          (e) => !(e.q === q && e.collection === entry.collection),
        )
        const next = [
          { ...entry, q, id: crypto.randomUUID(), at: new Date().toISOString() },
          ...rest,
        ].slice(0, LIMIT)
        write(next)
        return next
      })
    },
    [],
  )

  const forget = useCallback((id: string) => {
    setHistory((prev) => {
      const next = prev.filter((e) => e.id !== id)
      write(next)
      return next
    })
  }, [])

  const clear = useCallback(() => {
    setHistory([])
    write([])
  }, [])

  return { history, remember, forget, clear }
}
