import { Moon, Sun } from 'lucide-react'
import { useTranslation } from 'react-i18next'
import { Button } from '@/components/ui/button'
import { Tooltip, TooltipContent, TooltipTrigger } from '@/components/ui/tooltip'
import { useTheme } from '@/lib/theme'

/**
 * Toggles the `.dark` class on <html>. The second token layer that class
 * selects is Phase 6.9; until then this switches the hook, not the palette.
 */
export function ThemeToggle() {
  const { t } = useTranslation()
  const { theme, toggleTheme } = useTheme()
  const label = theme === 'dark' ? t('shell.themeDark') : t('shell.themeLight')

  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <Button variant="ghost" size="icon-sm" aria-label={label} onClick={toggleTheme}>
          {theme === 'dark' ? <Sun aria-hidden /> : <Moon aria-hidden />}
        </Button>
      </TooltipTrigger>
      <TooltipContent>{label}</TooltipContent>
    </Tooltip>
  )
}
