import { QueryClient } from '@tanstack/react-query'
import { SamaamApiError } from '@/lib/api'

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 30_000,
      // A 4xx from this service is a decision, not a hiccup. Retrying it wastes
      // the demo's seconds and can look like the gateway is flapping.
      retry: (failureCount, error) => {
        if (error instanceof SamaamApiError && error.status < 500) return false
        return failureCount < 2
      },
      refetchOnWindowFocus: false,
    },
  },
})
