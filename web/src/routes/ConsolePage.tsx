import { useTranslation } from 'react-i18next'
import { PageHeader } from '@/components/PageHeader'
import { PlaceholderNote } from '@/components/PlaceholderNote'

/** Phase 3 builds this screen. POST /device/execute. */
export default function ConsolePage() {
  const { t } = useTranslation()
  return (
    <>
      <PageHeader
        title={t('pages.console.title')}
        lead={t('pages.console.lead')}
        endpoint="POST /device/execute"
      />
      <PlaceholderNote />
    </>
  )
}
