import { useTranslation } from 'react-i18next'
import { Card } from '@/components/ui/card'
import { cn } from '@/lib/utils'
import { HUMAN_IN_THE_LOOP_VERDICTS, type Verdict } from '@/types/api'

type Tone = 'released' | 'withheld' | 'unsettled' | 'abstained'

/**
 * INSUFFICIENT_EVIDENCE and POTENTIAL_GAP are deliberate verdicts, not
 * failures, and FRONTEND-PLAN Part 4 forbids drawing them as errors. They read
 * neutral and carry the referral line instead.
 */
const VERDICT_TONE: Record<Verdict, Tone> = {
  COMPLIANT: 'released',
  VIOLATION: 'withheld',
  AMBIGUITY: 'unsettled',
  CONFLICT: 'unsettled',
  POTENTIAL_GAP: 'abstained',
  INSUFFICIENT_EVIDENCE: 'abstained',
}

const TONE_CLASS: Record<Tone, string> = {
  released: 'border-s-success bg-success/8 text-success-strong',
  withheld: 'border-s-danger bg-danger/8 text-danger-strong',
  unsettled: 'border-s-warn bg-warn/8 text-warn-strong',
  abstained: 'border-s-muted-foreground bg-surface-warm text-fg',
}

export interface VerdictBannerProps extends React.ComponentProps<typeof Card> {
  verdict: Verdict
  /** Whether the policy node withheld execution. */
  blocked: boolean
  /** The status the device actually returned. Derived from `blocked` if absent. */
  httpStatus?: number
}

export function VerdictBanner({
  verdict,
  blocked,
  httpStatus,
  className,
  ...props
}: VerdictBannerProps) {
  const { t } = useTranslation()
  const tone = VERDICT_TONE[verdict]
  const status = httpStatus ?? (blocked ? 403 : 200)
  const referred = (HUMAN_IN_THE_LOOP_VERDICTS as readonly Verdict[]).includes(verdict)

  return (
    <Card
      data-slot="verdict-banner"
      data-verdict={verdict}
      data-blocked={blocked}
      role="status"
      className={cn(
        'gap-2 rounded-md border-s-4 px-4 ring-0 shadow-ring',
        TONE_CLASS[tone],
        className,
      )}
      {...props}
    >
      <div className="flex flex-wrap items-center justify-between gap-3">
        {/* The verdict name is a contract value and is never translated. */}
        <span
          dir="ltr"
          className="font-display text-xl font-bold tracking-[0.04em] uppercase"
        >
          {verdict}
        </span>
        <span
          dir="ltr"
          className={cn(
            'font-mono text-sm tabular-nums',
            blocked ? 'font-semibold' : 'text-muted-foreground',
          )}
        >
          HTTP {status}
        </span>
      </div>

      <p className="text-sm text-fg-2">{t(`verdict.${verdict}`)}</p>

      {referred && (
        <p className="text-xs text-muted-foreground">{t('verdict.humanInTheLoop')}</p>
      )}
    </Card>
  )
}
