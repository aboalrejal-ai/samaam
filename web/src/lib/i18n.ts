import i18next from 'i18next'
import { initReactI18next } from 'react-i18next'
import ar from '@/locales/ar.json'
import en from '@/locales/en.json'

export const LANGUAGES = ['en', 'ar'] as const
export type Language = (typeof LANGUAGES)[number]

/** English is the default: the judging panel is international. */
export const DEFAULT_LANGUAGE: Language = 'en'

const STORAGE_KEY = 'samaam.language'

export function isLanguage(value: unknown): value is Language {
  return typeof value === 'string' && (LANGUAGES as readonly string[]).includes(value)
}

export function dirOf(language: Language): 'ltr' | 'rtl' {
  return language === 'ar' ? 'rtl' : 'ltr'
}

function storedLanguage(): Language {
  try {
    const stored = localStorage.getItem(STORAGE_KEY)
    return isLanguage(stored) ? stored : DEFAULT_LANGUAGE
  } catch {
    return DEFAULT_LANGUAGE
  }
}

/** Keeps <html lang> and <html dir> in step with i18next. */
export function applyLanguageToDocument(language: Language) {
  const root = document.documentElement
  root.lang = language
  root.dir = dirOf(language)
  try {
    localStorage.setItem(STORAGE_KEY, language)
  } catch {
    // A locked-down browser must not break the demo.
  }
}

void i18next.use(initReactI18next).init({
  resources: {
    en: { translation: en },
    ar: { translation: ar },
  },
  lng: storedLanguage(),
  fallbackLng: DEFAULT_LANGUAGE,
  supportedLngs: LANGUAGES,
  interpolation: { escapeValue: false },
})

applyLanguageToDocument(storedLanguage())

i18next.on('languageChanged', (language) => {
  if (isLanguage(language)) applyLanguageToDocument(language)
})

export default i18next
