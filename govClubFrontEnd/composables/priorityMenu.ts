import {useFeedback} from "~/composables/useFeedback";
import {useAsideMenu} from '~/composables/useAsideMenu'

const {isOpenForm, closeForm, openForm} = useFeedback()
const {isOpenMenu, closeMenu, openMenu} = useAsideMenu()

export function toggleUI(type: 'menu' | 'form') {
  if (type === 'menu') {
    if (isOpenMenu.value) {
      closeMenu()
    } else {
      closeForm()
      openMenu()
    }
  }

  if (type === 'form') {
    if (isOpenForm.value) {
      closeForm()
    } else {
      closeMenu()
      openForm()
    }
  }
}
