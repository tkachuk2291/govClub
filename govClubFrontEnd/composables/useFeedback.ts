import { ref } from 'vue'

const isOpenForm = ref(false)

export function useFeedback() {
  const openForm = () => isOpenForm.value = true
  const closeForm = () => isOpenForm.value = false
  const toggleForm = () => isOpenForm.value = !isOpenForm.value

  return { isOpenForm, openForm, closeForm, toggleForm }
}