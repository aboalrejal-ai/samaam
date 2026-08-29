import { useTranslation } from 'react-i18next'
import { Link } from 'react-router'
import { PageHeader } from '@/components/PageHeader'
import { Button } from '@/components/ui/button'

export default function NotFoundPage() {
  const { t } = useTranslation()
  return (
    <>
      <PageHeader title={t('pages.notFound.title')} lead={t('pages.notFound.lead')} />
      <Button asChild variant="outline" className="w-fit">
        <Link to="/">{t('pages.notFound.back')}</Link>
      </Button>
    </>
  )
}
