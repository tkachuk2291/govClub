<script setup lang="ts">
import {useMobileMenu} from '@/composables/useMobileMenu'

const {isOpen, close} = useMobileMenu()


</script>

<template>
  <div class="aside-menu" v-show="isOpen" @click.self="close">
    <div class="aside-menu-header">
      <headerMobile/>
    </div>
    <div class="aside-menu-content">
      <ul class="menu">
        <li class="menu__item">
          <a class="menu__link" href="#">Напрямки</a>
        </li>
        <li class="menu__item">
          <a class="menu__link" href="#">Курси</a>
        </li>
        <li class="menu__item">
          <a class="menu__link" href="#">Команда</a>
        </li>
        <li class="menu__item">
          <a class="menu__link" href="#">Контакти</a>
        </li>
      </ul>
    </div>

    <div class="language-container">
      <p class="language-container__text">Укр</p>
      <img src="../public/aside-menu/arrow_drop_down.svg" alt="arrow_drop_down" class="language-container__img">
    </div>
  </div>

</template>

<style scoped lang="scss">



.aside-menu {
  position: fixed;
  inset: 0;
  background-color: white;
  z-index: 1000;
  width: 100%;
}

</style>