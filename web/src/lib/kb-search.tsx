import { createContext, use, useCallback, useMemo, useState } from 'react'
import {
  useSearchHistory, type SearchHistoryEntry,
} from '@/hooks/use-search-history'
import type { KbCollection } from '@/types/api'

/**
 * Search state shared between the Knowledge Base page and the sidebar panel.
 *
 * The sidebar is a sibling of the routed outlet, so a past search clicked there
 * has no way to reach the page except through a provider. Same shape as
 * `lib/theme.tsx`: a nullable context and a hook that throws outside it.
 *
 * Note the split between `draft` and `query`. Typing updates `draft`, and the
 * page debounces it into live results — that is worth keeping, it shows
 * retrieval working as you type. Only a deliberate submit sets `query` and
 * writes history, so the trail records questions rather than keystrokes.
 */
export interface KbSearchValue {
  draft: string
  setDraft: (value: string) => void
  /** The last committed question. Empty until something is submitted. */
  query: string
  collection: KbCollection
  setCollection: (value: KbCollection) => void
  verifiedOnly: boolean
  setVerifiedOnly: (value: boolean) => void
  topK: number
  setTopK: (value: number) => void
  history: SearchHistoryEntry[]
  /** Submit the draft: records it and marks it as the committed question. */
  commit: () => void
  /** Re-run a past search, restoring the filters it was made with. */
  apply: (entry: SearchHistoryEntry) => void
  forget: (id: string) => void
  /** Empty the box for a fresh question. History is untouched. */
  reset: () => void
}

const KbSearchContext = createContext<KbSearchValue | null>(null)

export function KbSearchProvider({ children }: { children: React.ReactNode }) {
  const [draft, setDraft] = useState('')
  const [query, setQuery] = useState('')
  const [collection, setCollection] = useState<KbCollection>('policies')
  const [verifiedOnly, setVerifiedOnly] = useState(true)
  const [topK, setTopK] = useState(8)
  const { history, remember, forget } = useSearchHistory()

  const commit = useCallback(() => {
    const q = draft.trim()
    if (q.length < 2) return
    setQuery(q)
    remember({ q, collection, verifiedOnly })
  }, [draft, collection, verifiedOnly, remember])

  const apply = useCallback((entry: SearchHistoryEntry) => {
    setDraft(entry.q)
    setQuery(entry.q)
    setCollection(entry.collection)
    setVerifiedOnly(entry.verifiedOnly)
  }, [])

  const reset = useCallback(() => {
    setDraft('')
    setQuery('')
  }, [])

  const value = useMemo<KbSearchValue>(
    () => ({
      draft, setDraft, query, collection, setCollection,
      verifiedOnly, setVerifiedOnly, topK, setTopK,
      history, commit, apply, forget, reset,
    }),
    [draft, query, collection, verifiedOnly, topK, history, commit, apply, forget, reset],
  )

  return <KbSearchContext value={value}>{children}</KbSearchContext>
}

export function useKbSearchState() {
  const value = use(KbSearchContext)
  if (value === null) {
    throw new Error('useKbSearchState must be used inside KbSearchProvider')
  }
  return value
}
