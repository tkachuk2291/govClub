<script setup lang="ts">
import {useMobileMenu} from '@/composables/useMobileMenu'
import {useFeedback} from "~/composables/useFeedback";

const {toggle, isOpen} = useMobileMenu()
const {toggleForm, isOpenForm, closeForm} = useFeedback()

</script>

<template>
  <header class="header">
    <img class="header__img" alt="HeaderLogo" src="/header/headerLogo.svg"/>
    <div class="header__container">
      <button class="header__button">
        <a class="header__button-link" href="#"  @click="toggleForm">Записатися</a>
      </button>
      <a href="#" class="header__button-menu" @click="toggle">
        <img v-show="!isOpen" src="../public/headerMobile/menu.svg" alt="menu"/>
        <img v-show="isOpen" src="../public/headerMobile/isOpenMenu.svg" alt="menu1"/>
      </a>
    </div>
  </header>
  <div v-if="isOpenForm" class="feedback-overlay">
    <img src="../public/feedbackForm/mobile/close-mobile.svg" alt="close" class="close-btn" @click="closeForm" />
    <feedback/>
  </div>

</template>

<style scoped lang="scss">
.header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 auto;


  &__button {
    background-color: #345686;
    border: none;
    border-radius: 90px;
    padding: 8px 16px;
    width: 134px;
    height: 46px;
  }

  &__button-link {
    color: #fff;
    text-decoration: none;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: 0;
  }


  &__container {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  &__button-menu {
    display: inline-flex;
    padding: 0;
    margin: 0;
  }


}

.feedback-overlay {
  position: fixed;
  inset: 0;
  background-color: #345686;
  z-index: 1000;
  width: 100%;
}

.close-btn{
  position: fixed;
  z-index: 1000;
  right: 5px;
  top:30px;
  cursor: pointer;
}
</style>