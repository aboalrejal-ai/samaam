import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from '@/App'
// Sets <html lang> and <html dir> before the first paint, so an Arabic reload
// does not flash left-to-right on the way in.
import '@/lib/i18n'
import '@/index.css'

const container = document.getElementById('root')
if (container === null) throw new Error('Missing #root in index.html')

createRoot(container).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
