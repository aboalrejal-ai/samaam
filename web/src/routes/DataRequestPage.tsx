import { useTranslation } from 'react-i18next'
import { PageHeader } from '@/components/PageHeader'
import { PlaceholderNote } from '@/components/PlaceholderNote'

/** Phase 4 builds this screen. POST /data/request. */
export default function DataRequestPage() {
  const { t } = useTranslation()
  return (
    <>
      <PageHeader
        title={t('pages.data.title')}
        lead={t('pages.data.lead')}
        endpoint="POST /data/request"
      />
      <PlaceholderNote />
    </>
  )
}
