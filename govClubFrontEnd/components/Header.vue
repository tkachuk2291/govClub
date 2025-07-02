<script setup lang="ts">

</script>

<template>
  <header class="header">
    <img class="header__img" alt="HeaderLogo" src="/header/headerLogo.svg"/>
    <nav class="header__nav">
      <a class="header__link" href="#">Напрямки</a>
      <a class="header__link" href="#">Курси</a>
      <a class="header__link" href="#">Команда</a>
      <a class="header__link" href="#">Контакти</a>
    </nav>
    <div class="header__container">
      <div class="header__languageContainer">
        <a class="header__link" href="#">Укр</a>
        <img class="header__img" alt="arrow_down" src="/header/language/arrow_drop_down.svg"/>
      </div>
      <button class="header__button">
        <a class="header__button-link" href="#">Записатися</a>
      </button>
    </div>

  </header>
</template>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1280px;
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

  &__container{
    display: flex;
    align-items: center;
    gap: 45px;
  }


}

</style>