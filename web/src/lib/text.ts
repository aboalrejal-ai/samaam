const ARABIC_SCRIPT = /[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]/

/**
 * Direction of a quoted passage.
 *
 * Statutory text is rendered in the language it was issued in, so an English
 * provision quoted inside the Arabic UI needs `dir="ltr"` on its own paragraph
 * and vice versa. The resolved citations on the wire carry no language field,
 * so the script itself is the signal.
 */
export function scriptDirection(text: string | undefined): 'ltr' | 'rtl' {
  return text !== undefined && ARABIC_SCRIPT.test(text) ? 'rtl' : 'ltr'
}
