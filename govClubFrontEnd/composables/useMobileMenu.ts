import { ref } from 'vue'

const isOpen = ref(false)

export function useMobileMenu() {
  const open = () => isOpen.value = true
  const close = () => isOpen.value = false
  const toggle = () => isOpen.value = !isOpen.value

  return { isOpen, open, close, toggle }
}