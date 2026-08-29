import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'

export const THEMES = ['light', 'dark'] as const
export type Theme = (typeof THEMES)[number]

/** Light is the default: clearer on video, and the token package is built for it. */
export const DEFAULT_THEME: Theme = 'light'

const STORAGE_KEY = 'samaam.theme'

interface ThemeContextValue {
  theme: Theme
  setTheme: (theme: Theme) => void
  toggleTheme: () => void
}

const ThemeContext = createContext<ThemeContextValue | null>(null)

function storedTheme(): Theme {
  try {
    const stored = localStorage.getItem(STORAGE_KEY)
    return stored === 'dark' || stored === 'light' ? stored : DEFAULT_THEME
  } catch {
    return DEFAULT_THEME
  }
}

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setThemeState] = useState<Theme>(storedTheme)

  useEffect(() => {
    document.documentElement.classList.toggle('dark', theme === 'dark')
    try {
      localStorage.setItem(STORAGE_KEY, theme)
    } catch {
      // Ignored: storage is a convenience, not a requirement.
    }
  }, [theme])

  const setTheme = useCallback((next: Theme) => setThemeState(next), [])
  const toggleTheme = useCallback(
    () => setThemeState((current) => (current === 'dark' ? 'light' : 'dark')),
    [],
  )

  const value = useMemo(() => ({ theme, setTheme, toggleTheme }), [theme, setTheme, toggleTheme])

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
}

export function useTheme(): ThemeContextValue {
  const value = useContext(ThemeContext)
  if (value === null) throw new Error('useTheme must be used inside a ThemeProvider')
  return value
}
