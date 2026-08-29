import { useTranslation } from 'react-i18next'
import { ArrowLeft, Plus, X } from 'lucide-react'
import {
  SidebarGroup, SidebarGroupLabel, SidebarMenu, SidebarMenuAction,
  SidebarMenuButton, SidebarMenuItem, SidebarSeparator,
} from '@/components/ui/sidebar'
import { useKbSearchState } from '@/lib/kb-search'
import { scriptDirection } from '@/lib/text'

/**
 * The sidebar while the Knowledge Base is open: a way back to the nav, a fresh
 * search, and what has been asked so far.
 *
 * Deliberately "search history", not "conversations". Nothing here is a thread
 * — each entry is one question with the filters it was asked under, and
 * clicking it re-runs that exact search. The hackathon guide's first named
 * mistake is a general chatbot wearing a policy project's name, and a panel of
 * past chats is how a project starts looking like one.
 *
 * Back swaps this panel for the nav without leaving the page, so the rest of
 * the system stays reachable without losing the search.
 */
export function KbSidebar({ onBack }: { onBack: () => void }) {
  const { t } = useTranslation()
  const { history, apply, forget, reset } = useKbSearchState()

  return (
    <>
      <SidebarGroup className="pb-0">
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton onClick={onBack} tooltip={t('kb.sidebar.back')}>
              <ArrowLeft aria-hidden className="rtl:rotate-180" />
              <span>{t('kb.sidebar.back')}</span>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarGroup>

      <SidebarSeparator />

      <SidebarGroup className="py-0">
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton onClick={reset} tooltip={t('kb.sidebar.new')}>
              <Plus aria-hidden />
              <span>{t('kb.sidebar.new')}</span>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarGroup>

      <SidebarSeparator />

      <SidebarGroup>
        <SidebarGroupLabel>{t('kb.sidebar.history')}</SidebarGroupLabel>
        {history.length === 0 ? (
          <p className="px-2 py-1.5 text-xs text-muted-foreground group-data-[collapsible=icon]:hidden">
            {t('kb.sidebar.empty')}
          </p>
        ) : (
          <SidebarMenu>
            {history.map((entry) => (
              <SidebarMenuItem key={entry.id}>
                {/* Tooltip is not decoration: the rail collapses to 3rem and
                    the label disappears with it. */}
                <SidebarMenuButton
                  onClick={() => apply(entry)}
                  tooltip={`${entry.q} — ${t(`kb.collections.${entry.collection}`)}`}
                  className="h-auto flex-col items-start gap-0.5 py-1.5"
                >
                  <span
                    dir={scriptDirection(entry.q)}
                    className="w-full truncate text-sm"
                  >
                    {entry.q}
                  </span>
                  <span className="w-full truncate text-[10px] text-muted-foreground">
                    {t(`kb.collections.${entry.collection}`)}
                  </span>
                </SidebarMenuButton>
                <SidebarMenuAction
                  showOnHover
                  onClick={() => forget(entry.id)}
                  aria-label={t('kb.sidebar.forget')}
                >
                  <X aria-hidden />
                </SidebarMenuAction>
              </SidebarMenuItem>
            ))}
          </SidebarMenu>
        )}
      </SidebarGroup>
    </>
  )
}
