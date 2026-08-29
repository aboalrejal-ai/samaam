import { useTranslation } from 'react-i18next'
import { PageHeader } from '@/components/PageHeader'
import { PlaceholderNote } from '@/components/PlaceholderNote'

/** Phase 5.6 builds this screen. GET /framework. */
export default function ReadinessPage() {
  const { t } = useTranslation()
  return (
    <>
      <PageHeader
        title={t('pages.readiness.title')}
        lead={t('pages.readiness.lead')}
        endpoint="GET /framework"
      />
      <PlaceholderNote />
    </>
  )
}
