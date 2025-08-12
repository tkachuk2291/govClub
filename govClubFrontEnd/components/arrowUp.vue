<script setup lang="ts">
const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};
</script>

<template>
  <a href="#" class="scroll-up-arrow" @click.prevent="scrollToTop">
    <img src="/arrowUp/keyboard_arrow_up.png" alt="Scroll Up Arrow" />
  </a>
</template>

<style scoped>
.scroll-up-arrow {
  background-color: white;
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0,0,0,0.3);
  z-index: 1000;
  opacity: 0.8;
  transition: opacity 0.3s;
  text-decoration: none;
  border: 1px solid black;
}

.scroll-up-arrow:hover {
  opacity: 1;
}

.scroll-up-arrow img {
  width: 24px;
  height: 24px;
  pointer-events: none;
}
</style>
