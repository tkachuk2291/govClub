import { useWindowSize } from '@vueuse/core';
import { computed } from 'vue'; // Не забудьте импортировать computed

export function useWindowSizeSelect() {
  const { width } = useWindowSize();

  return computed(() => {
    if (width.value <= 768) {
      return 'mobile';
    } else if (width.value <= 1024) {
      return 'tablet';
    } else {
      return 'desktop';
    }
  });
}