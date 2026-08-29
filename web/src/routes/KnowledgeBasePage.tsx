import { useEffect, useMemo, useState } from 'react'
import { useTranslation } from 'react-i18next'
import { PageHeader } from '@/components/PageHeader'
import { VerificationChip } from '@/components/primitives'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Skeleton } from '@/components/ui/skeleton'
import { Switch } from '@/components/ui/switch'
import { useKbSearch } from '@/lib/queries'
import { KB_COLLECTIONS } from '@/types/api'
import type { KbCollection } from '@/types/api'

/**
 * Retrieval over the verified corpus.
 *
 * A search field, not a chat. Nothing is carried between queries and nothing
 * is generated: a question goes in, ranked records come back. That is the
 * distinction the hackathon guide draws when it warns against a chatbot
 * wearing a policy project's name.
 */
export default function KnowledgeBasePage() {
  const { t } = useTranslation()
  const [raw, setRaw] = useState('')
  const [query, setQuery] = useState('')
  const [collection, setCollection] = useState<KbCollection>('policies')
  const [verifiedOnly, setVerifiedOnly] = useState(true)

  // Debounced: every keystroke would embed a query locally for nothing.
  useEffect(() => {
    const timer = window.setTimeout(() => setQuery(raw.trim()), 300)
    return () => window.clearTimeout(timer)
  }, [raw])

  const params = useMemo(
    () => ({ q: query, collection, top_k: 8, verified_only: verifiedOnly }),
    [query, collection, verifiedOnly],
  )
  const { data, isFetching } = useKbSearch(params, query.length > 1)

  return (
    <>
      <PageHeader
        title={t('pages.kb.title')}
        lead={t('pages.kb.lead')}
        endpoint="GET /kb/search"
      />

      <div className="space-y-3">
        <Input
          value={raw}
          onChange={(event) => setRaw(event.target.value)}
          placeholder={t('kb.placeholder')}
          className="h-12 text-base"
          autoFocus
        />
        <div className="flex flex-wrap items-center gap-4">
          <div className="flex items-center gap-1.5">
            <span className="text-xs text-muted-foreground">{t('kb.collection')}</span>
            {KB_COLLECTIONS.map((name) => (
              <Button
                key={name}
                size="sm"
                variant={collection === name ? 'default' : 'outline'}
                onClick={() => setCollection(name)}
              >
                {t(`kb.collections.${name}`)}
              </Button>
            ))}
          </div>
          <div className="flex items-center gap-2">
            <Switch id="verified" checked={verifiedOnly} onCheckedChange={setVerifiedOnly} />
            <Label htmlFor="verified" className="text-sm">{t('kb.verifiedOnly')}</Label>
          </div>
        </div>
        <p className="text-xs text-muted-foreground">{t('kb.hint')}</p>
      </div>

      <div className="mt-6 space-y-3">
        {query.length <= 1 && (
          <Card>
            <CardContent className="py-10 text-center text-sm text-muted-foreground">
              {t('kb.prompt')}
            </CardContent>
          </Card>
        )}

        {isFetching && !data && (
          <>
            <Skeleton className="h-24 w-full" />
            <Skeleton className="h-24 w-full" />
          </>
        )}

        {data && data.results.length === 0 && (
          <Card>
            <CardContent className="py-10 text-center text-sm text-muted-foreground">
              {t('kb.empty')}
            </CardContent>
          </Card>
        )}

        {data && data.results.length > 0 && (
          <p className="text-xs text-muted-foreground">
            {t('kb.results', { count: data.count })}
          </p>
        )}

        {data?.results.map((hit) => (
          <Card key={`${hit.record_id}-${hit.section}`}>
            <CardContent className="space-y-2 py-4">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <span dir="ltr" className="font-mono text-xs font-semibold text-foreground">
                  {hit.record_id}
                </span>
                <div className="flex items-center gap-2">
                  <span dir="ltr" className="font-mono text-xs tabular-nums text-muted-foreground">
                    {hit.similarity.toFixed(3)} {t('kb.similarity')}
                  </span>
                  <VerificationChip verification={hit.verification} />
                </div>
              </div>
              <p className="text-sm font-medium text-foreground">{hit.title}</p>
              <p className="text-xs text-muted-foreground">
                {hit.authority} · {hit.section}
              </p>
              <p className="text-sm text-foreground/80">{hit.content}</p>
              {hit.url && (
                <a
                  href={hit.url}
                  target="_blank"
                  rel="noreferrer"
                  dir="ltr"
                  className="inline-block break-all font-mono text-xs text-primary-strong underline underline-offset-2"
                >
                  {hit.url}
                </a>
              )}
            </CardContent>
          </Card>
        ))}
      </div>
    </>
  )
}
