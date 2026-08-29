import { useTranslation } from 'react-i18next'
import { PageHeader } from '@/components/PageHeader'
import { PlaceholderNote } from '@/components/PlaceholderNote'

/** Phase 5.4 builds this screen. GET /kb/gaps. */
export default function GapsPage() {
  const { t } = useTranslation()
  return (
    <>
      <PageHeader
        title={t('pages.gaps.title')}
        lead={t('pages.gaps.lead')}
        endpoint="GET /kb/gaps"
      />
      <PlaceholderNote />
    </>
  )
}
