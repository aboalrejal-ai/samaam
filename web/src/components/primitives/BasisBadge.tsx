import { useTranslation } from 'react-i18next'
import { Badge } from '@/components/ui/badge'
import { cn } from '@/lib/utils'
import type { Basis } from '@/types/api'

/**
 * How strong the authority behind a check is — the distinction the whole
 * project rests on. A protocol departure is not a statutory violation and must
 * never be dressed as one.
 *
 * Colour is not the only channel. Per FRONTEND-PLAN §1.4 the three bases differ
 * by SHAPE as well: a filled 4px-cornered chip, an outlined pill, and bare
 * text. That survives colour blindness, a bad projector, and greyscale print.
 */
const BASIS_CLASS: Record<Basis, string> = {
  // Filled, hard 4px corners. The token radius scale starts at 8px, so the
  // 4px the plan specifies is written as a length.
  STATUTORY: 'rounded-[4px] border-transparent bg-danger-strong text-surface font-semibold',
  // Outlined, 1px edge, fully round.
  NATIONAL_PROTOCOL: 'rounded-pill border border-warn-strong bg-transparent text-warn-strong',
  // No background, no edge. Guidance, not an instrument of enforcement.
  CLINICAL_GUIDANCE: 'rounded-none border-transparent bg-transparent px-0 text-muted-foreground',
}

export interface BasisBadgeProps extends Omit<React.ComponentProps<typeof Badge>, 'variant'> {
  basis: Basis
}

export function BasisBadge({ basis, className, ...props }: BasisBadgeProps) {
  const { t } = useTranslation()

  return (
    <Badge
      data-basis={basis}
      className={cn(BASIS_CLASS[basis], className)}
      title={basis}
      {...props}
    >
      {t(`basis.${basis}`)}
    </Badge>
  )
}
