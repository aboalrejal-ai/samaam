import { useEffect, useState } from 'react'
import { Direction } from 'radix-ui'
import { useTranslation } from 'react-i18next'
import { Link, useLocation } from 'react-router'
import { ConnectionIndicator } from '@/components/ConnectionIndicator'
import { NavMain } from '@/components/nav-main'
import { KbSidebar } from '@/components/kb/KbSidebar'
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarRail,
  SidebarSeparator,
} from '@/components/ui/sidebar'
import { DEV_ROUTE, NAV_ROUTES } from '@/lib/routes'

/**
 * Adapted from the `sidebar-07` block: collapse-to-icon behaviour and the rail
 * are the block's, unmodified.
 *
 * Replaced, because the app has no such concepts: the team switcher became the
 * project mark, the user menu became the connection indicator, and the projects
 * group is gone.
 */
export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
  const { pathname } = useLocation()
  const onKb = pathname.startsWith('/kb')
  // Back swaps the panel for the nav without navigating, so the rest of the
  // system stays reachable without losing the search. Leaving /kb resets it.
  const [navShown, setNavShown] = useState(false)
  useEffect(() => { if (!onKb) setNavShown(false) }, [onKb])
  const { t } = useTranslation()
  const direction = Direction.useDirection()

  return (
    // The sidebar's fixed container pins itself with physical left-0 / right-0
    // off `side`, while the gap that reserves its space sits in the flex flow
    // and does follow `dir`. Left unset, the Arabic layout draws the rail on
    // the left and reserves its width on the right. `side` is the inline-start
    // edge for the current direction.
    <Sidebar collapsible="icon" side={direction === 'rtl' ? 'right' : 'left'} {...props}>
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton asChild size="lg" tooltip={t('brand.tagline')}>
              <Link to="/">
                {/* The mark is the valve: a seat with a stem through it. */}
                <span
                  aria-hidden
                  className="flex aspect-square size-8 shrink-0 items-center justify-center rounded-md bg-primary text-primary-foreground"
                >
                  <svg viewBox="0 0 24 24" className="size-4" fill="none" aria-hidden>
                    <path
                      d="M12 3v6m0 6v6"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                    />
                    <circle cx="12" cy="12" r="3.4" stroke="currentColor" strokeWidth="2" />
                    <path
                      d="M5 12h3.6m6.8 0H19"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                    />
                  </svg>
                </span>
                <span className="grid flex-1 text-start leading-tight">
                  {/* One Arabic word needs no dir override; forcing rtl here
                      would align it against the block's start edge. */}
                  <span lang="ar" className="truncate font-display text-base font-semibold">
                    {t('brand.name')}
                  </span>
                  <span className="truncate font-mono text-xs tracking-[0.12em] text-muted-foreground">
                    {t('brand.latin')}
                  </span>
                </span>
              </Link>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>

      <SidebarContent>
        {onKb && !navShown ? (
          <KbSidebar onBack={() => setNavShown(true)} />
        ) : (
          <NavMain label={t('nav.group')} items={NAV_ROUTES} />
        )}
      </SidebarContent>

      <SidebarFooter>
        <NavMain items={[DEV_ROUTE]} />
        <SidebarSeparator />
        <ConnectionIndicator />
      </SidebarFooter>

      <SidebarRail />
    </Sidebar>
  )
}
