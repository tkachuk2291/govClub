import {ref, watch} from 'vue'

const isOpenForm = ref(false)

export function useFeedback() {
  const openForm = () => isOpenForm.value = true
  const closeForm = () => isOpenForm.value = false
  const toggleForm = () => isOpenForm.value = !isOpenForm.value
   watch(isOpenForm, (value) => {
    if (value) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = ''
    }
  })
  return { isOpenForm, openForm, closeForm, toggleForm }
}