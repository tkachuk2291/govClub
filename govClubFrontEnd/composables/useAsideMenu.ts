import { ref, watch } from 'vue'

const isOpenMenu = ref(false)

export function useAsideMenu() {
  const openMenu = () => isOpenMenu.value = true
  const closeMenu = () => isOpenMenu.value = false
  const toggleMenu = () => isOpenMenu.value = !isOpenMenu.value

  watch(isOpenMenu, (value) => {
    if (value) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = ''
    }
  })

  return { isOpenMenu, openMenu, closeMenu, toggleMenu }
}