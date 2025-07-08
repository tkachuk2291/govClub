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
      <div class="hero-content-bottom">
        <div class="curator-card">
          <div class="curator-card__header">
            <h3 class="curator-card__header-text">Куратори</h3>
          </div>
          <div class="curator-card__content">
            <img class="curator-card__img" src="/curators/curator.png" alt="curator"/>
            <div class="curator-card__text-container">
              <h4 class="curator-card__title">Леся Червінська</h4>
              <p class="curator-card__text">Кандидат наук, магістр державного
                управління в сфері інформаційних технологій та публічного управління</p>
            </div>
          </div>

        </div>
      </div>
    </section>

<!--    <section class="schedule width-sm"></section>-->
    <section class="info width-sm">
      <h2 class="info__title">Детальніше про наш курс</h2>
      <p class="info__text">У рамках Форуму CDTO пройшли виступи CDTO в стилі TEDx.Цей динамічний формат дозволив
        дізнатися про рішення, які реалізовували у себе наші учасники. CDTO НАЗК Станіслава Гейдера розповідав про те,
        як іт-інструменти допомагають підвищити взаємодію в організації CDTO Мінекономіки Ігор Дядюра поділився досвідом
        про цифрову трансформація дозвільної системи CDTO Мінагро Тарас Дзьоба розказав про використання даних та
        алгоритмів для вироблення державних політик у агросекторі CDTO
        Держспецзв'язку Віктор Жора розповів про реєстр ОКІІ CDTO Міндовкілля Руслан Стрілець висвітлив тему залучення
        стейкхолдерів та громадського сектору до цифровізації на прикладі ЕКО-послуг СДТО Держпродспоживслужби Анатолій
        Вовнюк розказав про спільне й відмінне у трансформаціях у державному та комерційному секторах Директор ДП
        Прозоро Василь Задворний пояснив важливістьволодіння ІТ системами й як дійсно управляти зоною своєї
        відповідальностіРадник Міністра охорони здоров'я Роман Ланський поділився досвідом того, яка теорія та практика
        регіонального впровадження диспетчеризації швидкої допомогиЕкс-СДТО Митниці Євген Єнтіс розповів про те, як він
        разом з командою робив реформу у Державній митній службі України</p>
    </section>
    <section class="conference width-sm">
<!--      <img class="conference__img" src="/conference/conference.png" alt="conference"/>-->
    </section>
    <section class="feedback">
      <feedback />
    </section>
  </main>
</template>

<style scoped lang="scss">

.main{
  display: flex;
  flex-direction: column;
  gap: 60px;
}

.hero {
  display: flex;
  flex-direction: column;
  gap: 40px
}

.course-card {
  display: flex;
  flex-direction: column;
  gap: 40px;

  &__header {
    display: flex;
    flex-direction: column;
    gap: 40px;
  }

  &__date {
    font-weight: 400;
    font-size: 32px;
    line-height: 1.6;
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
  &__title{
    font-weight: 700;
    font-size: 40px;
    line-height: 1.5;
    letter-spacing: 0;

  }

  &__header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__img {
    max-width: 800px;
  }

}

.curator-card {
  display: flex;
  flex-direction: column;
  gap: 30px;
  max-width: 400px;

  &__header-text {
    font-weight: 700;
    font-size: 32px;
    line-height: 1.5;
    letter-spacing: 0;
  }

  &__img {
    width: 400px;
    height: 400px;

  }

  &__content {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  &__text-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  &__title {
    font-weight: 700;
    font-size: 20px;
    line-height: 1.5;
    letter-spacing: 0;
  }

  &__text {
    font-weight: 400;
    font-size: 18px;
    line-height: 1.5;
    letter-spacing: 0;
  }
}

.info {
  display: flex;
  flex-direction: column;
  gap: 30px;

  &__title {
    font-weight: 700;
    font-size: 32px;
    line-height: 1.5;
    letter-spacing: 0;
  }

  &__text {
    font-weight: 400;
    font-size: 18px;
    line-height: 1.5;
    letter-spacing: 0;
  }
}

.conference{
  &__img{
    width: 800px;
  }
}



</style>