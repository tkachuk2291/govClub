<script setup lang="ts">
</script>

<template>
  <main class="main width-md">
    <section class="hero width-sm">
      <div class="hero-content-top">
        <div class="course-card">
          <div class="course-card__header">
            <div class="course-card__header-container">
              <h2 class="course-card__date">27.02.2023 </h2>
              <a href="#" class="course-card__button">Записатися</a>
            </div>
            <h3 class="course-card__title">Авторський курс з комунікацій</h3>
          </div>
          <div class="course-card__content">
            <img class="course-card__img" alt="course" src="/course-announcements/detail-page/authors-courses.png"/>
          </div>
        </div>


      </div>
      <div class="hero-content-bottom"></div>
    </section>

    <section class="schedule width-sm"></section>
    <section class="info width-sm"></section>
    <section class="feedback"></section>
  </main>
</template>

<style scoped lang="scss">

.course-card {

  &__header{
    display: flex;
    flex-direction: column;
    gap:40px;
  }

  &__date {
    font-weight: 400;
    font-size: 32px;
    line-height: 1.6%;
    letter-spacing: 0;
  }

  &__button {
    width: 180px;
    height: 60px;
    border-radius: 90px;
    padding: 16px;
    background-color: #345686;
    color: white;
    text-decoration: none;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;

  }
  &__header-container{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  &__title{
    font-weight: 700;
    font-size: 40px;
    line-height: 1.5%;
    letter-spacing: 0;
  }
  &__img{
    max-width: 800px;
  }


}


</style>