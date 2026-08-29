import { useTranslation } from 'react-i18next'
import { PageHeader } from '@/components/PageHeader'
import { PlaceholderNote } from '@/components/PlaceholderNote'

/** Phase 5.5 builds this screen. GET /audit. */
export default function AuditPage() {
  const { t } = useTranslation()
  return (
    <>
      <PageHeader
        title={t('pages.audit.title')}
        lead={t('pages.audit.lead')}
        endpoint="GET /audit"
      />
      <PlaceholderNote />
    </>
  )
}
