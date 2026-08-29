import { useTranslation } from 'react-i18next'
import { PageHeader } from '@/components/PageHeader'
import { PlaceholderNote } from '@/components/PlaceholderNote'

/** Phase 5.1–5.3 build this screen. GET /kb/search. */
export default function KnowledgeBasePage() {
  const { t } = useTranslation()
  return (
    <>
      <PageHeader
        title={t('pages.kb.title')}
        lead={t('pages.kb.lead')}
        endpoint="GET /kb/search"
      />
      <PlaceholderNote />
    </>
  )
}
