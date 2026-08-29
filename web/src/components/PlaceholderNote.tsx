import { useTranslation } from 'react-i18next'
import { Card, CardContent } from '@/components/ui/card'

/** Stands in until the phase that owns a screen builds it. */
export function PlaceholderNote() {
  const { t } = useTranslation()
  return (
    <Card size="sm" className="rounded-md border-s-2 border-s-border ring-0 shadow-ring">
      <CardContent className="px-3">
        <p className="text-sm text-muted-foreground">{t('pages.placeholder')}</p>
      </CardContent>
    </Card>
  )
}
