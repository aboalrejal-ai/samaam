# صِمَام · Samaam — Web

Operator interface for the Samaam policy gateway. React 19 · TypeScript 5.7 · Vite 6 ·
Tailwind v4 · shadcn/ui · TanStack Query v5 · react-router v7.

> بيانات محاكاة لأغراض الهاكاثون فقط — synthetic data, hackathon use only.

## Running it

The FastAPI service must be up first; it takes about 15 seconds to boot because it loads a
local embedding model.

```bash
# from the repository root
.venv/bin/uvicorn app.main:app --reload --port 8000

# then, in web/
npm install
npm run dev          # http://localhost:5173
```

The service origin defaults to `http://localhost:8000` and can be pointed elsewhere with
`VITE_API_BASE_URL`. CORS on the service is already open for `:5173`. No key is read here —
the frontend never talks to a model provider.

| Script | What it does |
| :--- | :--- |
| `npm run dev` | Dev server on `:5173` |
| `npm run build` | `tsc -b` then a production build into `dist/` |
| `npm run typecheck` | Types only |
| `npm run preview` | Serves the built output |

Sanity check that the wiring is live: the sidebar footer should read `43 · 6 · 1338`, the
knowledge-base counts from `GET /health`. A red dot there means the service is down.

## Layout

```
src/
  index.css              Tailwind + the design tokens + the shadcn role mapping
  types/api.ts           Wire types, mirroring app/main.py and app/policy_node.py
  lib/api.ts             Typed client. 403 is a result here, not an exception
  lib/queries.ts         TanStack Query hooks and query keys
  lib/i18n.ts            i18next; also owns <html lang> and <html dir>
  lib/theme.tsx          The .dark class on <html>
  lib/routes.ts          The six-screen page inventory
  components/primitives/ Measured · BasisBadge · VerdictBanner · CheckRow ·
                         CitationCard · VerificationChip
  components/ui/         shadcn. Generated — regenerate rather than edit
  routes/                One file per screen
```

## Things worth knowing before editing

**Colour comes from tokens, never from literals.** `src/index.css` imports
`design/dashboard/tokens.css` and bridges it into Tailwind. Two shadcn role names collide with
token names of the same spelling, and the mapping block in that file resolves both: the sky
accent is reachable as `primary` (`text-primary`, `bg-primary`), and the grey body text as
`muted-foreground`. `accent` and `muted` keep their shadcn meanings — subtle surfaces — because
repointing them would turn every hover state solid blue.

Status hues carry text and 1px edges through `success-strong` / `warn-strong` /
`danger-strong`, which are darkened shades of the same tokens. The plain tokens are fills; on
white they do not clear 4.5:1.

**Logical properties only.** `ps-4`, `me-2`, `text-start`, `border-s` — never `pl`, `mr`,
`text-left`, `border-l`. The Arabic toggle flips the whole document, including the sidebar,
which is why `AppSidebar` passes `side` from the current direction.

**Compose from shadcn.** Only `Measured` and `BasisBadge` are hand-written here, plus
`PipelineRail` when it lands. Writing `<div className="rounded-lg border p-4">` means
rebuilding `Card`.

**Never restate a decision.** Thresholds, verdicts and citations live in the service. The
frontend renders what arrived and computes nothing — no invented limit, no invented citation,
no invented link.

Do not translate quoted statutory text, record ids (`MOH-CM-PROPHYLAXIS`), verdict names
(`VIOLATION`), basis names (`STATUTORY`), or measured values and units.

## Gate page

`/dev/primitives` renders every primitive in every state. Print it in greyscale: if
`STATUTORY` still reads differently from `NATIONAL_PROTOCOL`, the shape channel is working.
