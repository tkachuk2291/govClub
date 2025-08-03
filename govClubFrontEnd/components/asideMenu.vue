<script setup lang="ts">
  import { useMobileMenu } from '@/composables/useMobileMenu'
  const { isOpen, close } = useMobileMenu()


</script>

<template>
  <div class="overlay" v-show="isOpen" @click.self="close">
    <headerMobile />
  </div>

</template>

<style scoped lang="scss">
  .overlay {
  position: fixed;
  inset: 0;
  background-color: white;
  z-index: 1000;
  width: 100%;

}

</style>