<script setup lang="ts">
import {useFeedback} from "~/composables/useFeedback";
import {useAsideMenu} from '~/composables/useAsideMenu'
import {toggleUI} from '~/composables/priorityMenu'

const {toggleForm, isOpenForm, closeForm} = useFeedback()
const {toggleMenu, isOpenMenu, closeMenu} = useAsideMenu()


</script>

<template>
  <header class="header width-md">
    <img class="header__img" alt="HeaderLogo" src="/header/headerLogo.svg"/>
    <nav class="header__nav">
      <NuxtLink :to="{ path: '/', hash: '#directions' }" class="header__link">Напрямки</NuxtLink>
      <NuxtLink :to="{ path: '/', hash: '#course-announcements' }" class="header__link">Курси</NuxtLink>
      <NuxtLink :to="{ path: 'team/'}" class="header__link">Команда</NuxtLink>
      <NuxtLink :to="{ path: '/' , hash: '#contacts'}" class="header__link">Контакти</NuxtLink>

    </nav>
    <div class="header__container">
      <div class="header__languageContainer">
        <a class="header__link" href="#">Укр</a>
        <img class="header__img" alt="arrow_down" src="/header/language/arrow_drop_down.svg"/>
      </div>
      <a class="header__button-link" href="#"  @click="toggleUI('form')">Записатися</a>
    </div>

  </header>
  <header class="header-mobile width-md" >
    <img class="header-mobile__img" alt="HeaderLogo" src="/headerMobile/headerLogoMobile.svg"/>
    <div class="header-mobile__container">
      <button class="header-mobile__button">
        <a class="header-mobile__button-link" href="#" @click="toggleUI('form')">Записатися</a></button>
      <a href="#" class="header-mobile__button-menu" @click="toggleMenu">
        <img v-show="!isOpenMenu" src="../public/headerMobile/menu.svg" alt="menu"/>
        <img v-show="isOpenMenu" src="../public/headerMobile/isOpenMenu.svg" alt="menu1"/>
      </a>
    </div>

    <div v-if="isOpenForm" class="feedback-overlay">
      <img src="../public/feedbackForm/mobile/close-mobile.svg" alt="close" class="close-btn" @click="toggleForm"/>
      <feedback/>
    </div>
  </header>
  <div class="aside-menu" v-if="isOpenMenu">
    <div class="aside-menu-content">
      <ul class="menu">
        <li class="menu__item">
          <NuxtLink :to="{ path: '/', hash: '#directions' }" class="menu__link" @click="toggleMenu">Напрямки</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink :to="{ path: '/', hash: '#course-announcements' }" class="menu__link" @click="toggleMenu">Курси</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink :to="{ path: 'team/'}" class="menu__link" @click="toggleMenu">Команда</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink :to="{ path: '/' , hash: '#contacts'}" class="menu__link" @click="toggleMenu">Контакти</NuxtLink>
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
.header {
  display: none;
  @media (max-width: 1900px) {
    padding: 0 32px;
  }
  @media (min-width: 951px) {
    display: flex;
  }
  justify-content: space-between;
  align-items: center;
  max-width: 1480px;
  margin: 0 auto;

  &__nav {
    display: flex;
    align-items: center;
    gap: 50px;
  }

  &__languageContainer {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  &__button {
    background-color: #345686;
    border: none;
    border-radius: 90px;
    padding: 16px;
    width: 180px;
    height: 60px;
  }

  &__button-link {
    color: #fff;
    text-decoration: none;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: 0;
    background-color: #345686;
    border-radius: 90px;
    padding: 16px;
    width: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  &__link {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: 0;
    color: #000;
    text-decoration: none;
  }

  &__container {
    display: flex;
    align-items: center;
    gap: 45px;
  }


}


.header-mobile {
  @media (min-width: 950px) {
    display: none;
  }
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 auto;
  padding: 30px 16px 0 16px;
  box-sizing: border-box;


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
  height: 100vh;
  position: fixed;
  inset: 0;
  background-color: #345686;
  z-index: 1000;
  width: 100%;
}

.close-btn {
  position: fixed;
  z-index: 1000;
  right: 5px;
  top: 30px;
  cursor: pointer;
}


.aside-menu {
  position: fixed;
  padding-top: 200px;
  overflow-y: hidden;
  height: 100vh;
  top: 88px;
  gap: 200px;
  width: 100vw;
  background-color: white;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.menu {
  display: flex;
  flex-direction: column;
  gap: 50px;

  &__link {
    text-decoration: none;
    color: #101014;
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: 0;
  }
}

.language-container {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-bottom: 60px;
}


</style>