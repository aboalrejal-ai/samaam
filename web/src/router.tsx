import { createBrowserRouter } from 'react-router'
import { AppShell } from '@/components/AppShell'
import AuditPage from '@/routes/AuditPage'
import ConsolePage from '@/routes/ConsolePage'
import DataRequestPage from '@/routes/DataRequestPage'
import DevPrimitivesPage from '@/routes/DevPrimitivesPage'
import GapsPage from '@/routes/GapsPage'
import KnowledgeBasePage from '@/routes/KnowledgeBasePage'
import NotFoundPage from '@/routes/NotFoundPage'
import ReadinessPage from '@/routes/ReadinessPage'

/** The six screens of FRONTEND-PLAN Part 1-b, plus Phase 1's gate page. */
export const router = createBrowserRouter([
  {
    path: '/',
    Component: AppShell,
    children: [
      { index: true, Component: ConsolePage },
      { path: 'data', Component: DataRequestPage },
      { path: 'kb', Component: KnowledgeBasePage },
      { path: 'gaps', Component: GapsPage },
      { path: 'audit', Component: AuditPage },
      { path: 'readiness', Component: ReadinessPage },
      { path: 'dev/primitives', Component: DevPrimitivesPage },
      { path: '*', Component: NotFoundPage },
    ],
  },
])
