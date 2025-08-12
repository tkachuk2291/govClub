<script setup lang="ts">

watch(isOpen, (val) => {
  if (val) {
    document.body.classList.add('no-scroll')
  } else {
    document.body.classList.remove('no-scroll')
  }
})


</script>

<template>
  <div class="aside-menu" v-show="isOpenForm">
    <headerMobile/>

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
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  position: fixed;
  inset: 0;
  background-color: white;
  z-index: 1000;
  width: 100%;
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