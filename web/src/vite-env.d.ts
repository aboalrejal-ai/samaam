/// <reference types="vite/client" />

interface ImportMetaEnv {
  /** Origin of the Samaam FastAPI service. Defaults to http://localhost:8000. */
  readonly VITE_API_BASE_URL?: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
