import { useTranslation } from 'react-i18next'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Skeleton } from '@/components/ui/skeleton'
import { CheckRow, CitationCard, VerdictBanner } from '@/components/primitives'
import type { EvaluationResponse } from '@/types/api'

/**
 * What the policy node decided, and on whose authority.
 *
 * Checks render in the order the service returned them. WARN is never
 * collapsed: a warning is part of the decision, not a footnote to it.
 */
export interface DecisionPanelProps {
  result: EvaluationResponse
  /** Arrives after the decision. Null while pending or when the model is down. */
  explanation?: string | null
  explaining?: boolean
}

export function DecisionPanel({ result, explanation, explaining }: DecisionPanelProps) {
  const { t } = useTranslation()
  const { policy, device_response: device, privacy } = result

  return (
    <div className="space-y-4">
      <VerdictBanner
        verdict={policy.verdict}
        action={policy.action}
        blocked={policy.blocked}
        httpStatus={device.status}
      >
        {(device.message ?? device.error) && (
          <p className="text-sm text-foreground/80">{device.message ?? device.error}</p>
        )}
      </VerdictBanner>

      {device.overridden_by && (
        <p className="rounded-md border border-warn-strong bg-warn/10 px-3 py-2 text-sm text-warn-strong">
          {t('console.overrideRecorded', { name: device.overridden_by })}
        </p>
      )}

      <Card>
        <CardHeader>
          <CardTitle className="text-base">{t('console.checks')}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-2">
          {policy.checks.map((check) => (
            <CheckRow key={check.rule} check={check} />
          ))}
        </CardContent>
      </Card>

      {(explaining || explanation || policy.explanation) && (
        <Card>
          <CardHeader>
            <CardTitle className="text-base">{t('console.explanation')}</CardTitle>
          </CardHeader>
          <CardContent>
            {explaining && !explanation ? (
              <div className="space-y-2">
                <Skeleton className="h-4 w-full" />
                <Skeleton className="h-4 w-11/12" />
                <Skeleton className="h-4 w-4/5" />
              </div>
            ) : (
              <p className="text-sm text-foreground/80">
                {explanation ?? policy.explanation}
              </p>
            )}
          </CardContent>
        </Card>
      )}

      <Card>
        <CardHeader>
          <CardTitle className="text-base">
            {t('console.citations')}{' '}
            <span className="font-mono text-sm text-muted-foreground">
              ({policy.citations.length})
            </span>
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          {policy.citations.map((citation) => (
            <CitationCard key={citation.record_id} citation={citation} />
          ))}
        </CardContent>
      </Card>

      {privacy && (
        <p className="text-xs text-muted-foreground">
          {privacy.identifiers_removed.length
            ? t('console.privacy', { fields: privacy.identifiers_removed.join('، ') })
            : t('console.privacyNone')}
        </p>
      )}
    </div>
  )
}
