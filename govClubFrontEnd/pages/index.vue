<script setup lang="ts">


const {data: sections, pending, error} = await useFetch('http://localhost:8005/home-page/', {
  server: true,
  method: 'GET',
  headers: {
    accept: 'application/json'
  }
})
import {useRouter, useRoute} from 'vue-router'

const router = useRouter()

</script>
<template>
  <div class="page-container">
    <header class="header">
      <section class="hero-section">
        <div class="hero-content-top width-md">
          <h1 class="hero-content-top__title">{{ sections.hero.title_part1 }}</h1>
          <div class="hero-content-top__container">
            <p class="hero-content-top__text">{{ sections.hero.description }}</p>
            <a href="#" class="hero-content-top__button">Стати партнером</a>
          </div>
        </div>
        <div class="hero-content-bottom">
          <div class="hero-content-bottom__wrapper-img-top"></div>
          <div class="hero-content-bottom__wrapper-img-bottom-mobile"></div>


          <div class="hero-content-bottom__wrapper-img-bottom"></div>
          <div class="hero-content-bottom__header-container">
            <div class="hero-content-bottom__header" v-for="missionSubsection in sections.mission.mission_subsection">
              <h2 class="hero-content-bottom__header-title">{{ missionSubsection.title }}</h2>
              <p class="hero-content-bottom__header-description">
                {{ missionSubsection.description }}
              </p>
            </div>

          </div>
          <div class="hero-content-bottom__content-container">
            <div class="hero-content-bottom__item" v-for="missionCard in sections.mission.mission_card">
              <h3 class="hero-content-bottom__title">{{ missionCard.title }}</h3>
              <p class="hero-content-bottom__description">{{ missionCard.description }}</p>
            </div>
          </div>
        </div>
      </section>
    </header>
      <main class="main width-lg">
        <section class="directions width-md" id="directions">
          <h2 class="directions__title">{{ sections.direction.section_title }}</h2>
          <div class="directions__content">
            <div class="directions__card" v-for="directionsCard in sections.direction.direction_cards">
              <div class="directions__card-text-container">
                <h3 class="directions__card-title">{{ directionsCard.title }}</h3>
                <p class="directions__card-text">{{ directionsCard.description }}</p>
              </div>
              <a class="directions__card-button">Стати партнером</a>
            </div>
          </div>
        </section>
        <section class="course-announcements width-md" id="course-announcements">
          <div class="course-announcements__header">
            <h2 class="course-announcements__header-title">{{ sections.course_announcements.section_title }}</h2>
            <a class="course-announcements__header-button" href="#">Дивитися всі анонси</a>
          </div>
          <div class="course-announcements__content">

            <div class="course-announcements__card"
                 v-for="courseAnnouncementsCard in sections.course_announcements.course_announcement_card">
              <NuxtLink class="course-announcements__card-link"
                        :to="{ name: 'slug', params: { slug: `${courseAnnouncementsCard.slug}` } }">
                <div class="course-announcements__card-header">
                  <img
                      class="course-announcements__card-img"
                      alt="course"
                      :src="courseAnnouncementsCard.image"
                  />
                  <h3 class="course-announcements__card-title">{{ courseAnnouncementsCard.title }}</h3>
                </div>
                <div class="course-announcements__card-content">
                  <div class="course-announcements__card-info">
                    <p class="course-announcements__card-info-name">Лектор: <strong
                        class="course-announcements__text-fatty">{{ courseAnnouncementsCard.lector }}</strong></p>
                    <p class="course-announcements__card-info-date">{{ courseAnnouncementsCard.date }}</p>
                  </div>
                  <p class="course-announcements__card-text">{{ courseAnnouncementsCard.description }}</p>
                  <div class="course-announcements__card-button-container">
                    <a class="course-announcements__card-button course-announcements__card-button--blue">Записатися</a>
                    <a class="course-announcements__card-button course-announcements__card-button--white">Докладніше</a>
                  </div>
                </div>
              </NuxtLink>
            </div>
          </div>
        </section>
      </main>
  </div>
</template>

<style lang="scss" scoped>
$mobile: "(max-width: 768px)";
$tablet: "(min-width: 769px)";
$desktop: "(min-width: 1024px)";


.page-container {
  @media #{$mobile} {
    padding: 0 16px;
    padding-top:50px;
  }
}

.header {
  &__title {
    color: blueviolet;
  }
}

.main {
  display: flex;
  flex-direction: column;
  gap: 160px;
  margin-top: 70px;
  @media #{$mobile} {
    gap: 70px;
  }
}

.hero-section {
  display: flex;
  flex-direction: column;
  gap: 100px;
  align-items: center;
  justify-content: center;
  @media #{$mobile} {
    gap: 70px;
  }
}

.hero-content-top {
  display: flex;
  width: 100%;
  flex-direction: column;
  gap: 50px;
  @media #{$mobile} {
    gap: 16px;
  }


  &__item1 {
    grid-column: 1 / 13;
    @media #{$mobile} {
      grid-column: 1 / 2;
    }
  }

  &__item2 {
    grid-column: 4 / 13;
    margin-bottom: 50px;
    @media #{$mobile} {
      grid-column: 1 / -1;
    }
  }

  &__item3 {
    grid-column: 1 / 14;
    @media #{$mobile} {
      grid-column: 1 / 2;
    }
  }

  &__container {
    display: flex;
    gap: 150px;
    @media #{$mobile} {
      flex-direction: column;
      gap: 40px;
    }
  }

  &__title {
    white-space: normal;
    //width: 1300px;
    font-weight: 700;
    font-size: 80px;
    line-height: 1.2;
    @media #{$mobile} {
      font-size: 32px;
      letter-spacing: 0;
      width: 375px;
    }
  }

  &__button {
    width: 950px;
    height: 80px;
    text-decoration: none;
    background-color: #345686;
    padding: 16px;
    box-sizing: border-box;
    border-radius: 90px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    @media #{$mobile} {
      width: 100%;
      height: 70px;
      padding: 23px;
    }
  }

  &__text {
    max-width: 180px;
    font-weight: 400;
    font-size: 18px;
    line-height: 150%;
    letter-spacing: 0;

  }
}

.hero-content-bottom {
  border-radius: 30px;
  position: relative;
  background: #FFF9E5;
  width: 98%;
  box-sizing: border-box;
  height: 100%;
  @media #{$mobile} {
    border-radius: 20px;
  }


  .flex-group-base {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 52px;
  }

  &__header-title {
    font-weight: 700;
    font-size: 80px;
    line-height: 1.2;
    letter-spacing: 0;
    @media #{$mobile} {
      font-size: 32px;
    }
  }

  &__title {
    font-weight: 700;
    font-size: 40px;
    line-height: 1.5;
    letter-spacing: 0;
    @media #{$mobile} {
      font-size: 22px;
      line-height: 1.2;
    }

  }

  &__description {
    font-weight: 400;
    font-size: 22px;
    line-height: 1.5;
    letter-spacing: 0;
    max-width: 620px;
    @media #{$mobile} {
      font-size: 16px;
    }

  }

  &__header-description {
    font-weight: 400;
    font-size: 22px;
    line-height: 1.5;
    letter-spacing: 0;
    max-width: 577px;
    @media #{$mobile} {
      font-size: 20px;
    }
  }

  &__img {
    width: 371px;
    max-height: 384px;
    position: absolute;

  }


  &__header-container {
    display: flex;
    gap: 77px;
    max-width: 1300px;
    margin: 0 auto 100px auto;
    padding-top: 140px;
    @media #{$mobile} {
      max-width: 100%;
      margin:0 20px 32px 20px;
      flex-direction: column;
      gap: 40px;
      padding-top: 50px;
    }

  }

  &__header {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }


  &__item {
    @extend .flex-group-base;
    border-radius: 30px;
    box-sizing: border-box;
    min-height: 199px;
    @media #{$mobile} {
      align-items: start !important;
      flex-direction: column;
      padding: 0 !important;
      margin: 0 20px;
      min-height: 124px;
      gap:10px;
      border-radius: 15px;

    }

    &:nth-child(odd) {
      background-color: #FFEFC2;
      @media #{$mobile} {
        margin: 0 10px;
        padding: 20px 10px !important;
      }
    }


  }


  &__wrapper-img-top {
    background-image: url('/hero-content-bottom/flower-bottom.png');
    background-repeat: no-repeat;
    width: 371px;
    height: 384px;
    position: absolute;
    left: 0;
    bottom: 0;
    @media #{$mobile} {
      display: none;
    }
  }

  &__wrapper-img-bottom {
    background-image: url('/hero-content-bottom/flower-top.png');
    background-repeat: no-repeat;
    width: 371px;
    height: 384px;
    position: absolute;
    right: 0;
    top: 0;
    @media #{$mobile} {
      display: none;
    }


  }

  &__wrapper-img-bottom-mobile {
    background-image: url('/hero-content-bottom/flower-mobile.png');
    background-repeat: no-repeat;
    width: 183px;
    height: 244px;
    position: absolute;
    right: 0;
    top: 1px;
    @media #{$desktop} {
      display: none;
    }
  }


  &__content-container {
    display: flex;
    flex-direction: column;
    max-width: 1384px;
    margin: 0 auto;
    @media #{$mobile} {
      max-width: 100%;
      gap:24px;
    }
  }

  &__sections {
    display: flex;
    flex-direction: column;
    gap: 40px;
  }

  &__wrapper {
    padding: 140px 0;
  }

}

.directions {
  display: flex;
  flex-direction: column;
  gap: 60px;
  @media #{$mobile} {
    gap: 32px;
  }

  &__title {
    font-weight: 700;
    font-size: 80px;
    line-height: 1.2;
    letter-spacing: 0;
    @media #{$mobile} {
      font-size: 32px;
      letter-spacing: 0;
    }
  }

  &__content {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    //grid-template-rows: 316px;
    column-gap: 40px;
    @media #{$mobile} {
       grid-template-columns: 1fr;
      column-gap: 0;
      row-gap: 16px;
       //grid-template-rows: 343px;
    }
  }


  &__card {
    display: flex;
    flex-direction: column;
    background-color: #FFEFC2;
    padding: 30px;
    border-radius: 30px;
    align-items: center;
    //min-height: 316px;
    justify-content: space-between;
    box-sizing: border-box;

    @media #{$mobile} {
      min-height: 280px;
      justify-content: flex-start;
    }

    &:nth-child(odd) {
      background-color: #C5DAF9;
    }

  }

  &__card-text-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
    flex-grow: 1;
  }

  &__card-title {
    font-weight: 700;
    font-size: 32px;
    line-height: 1.5;
    letter-spacing: 0;
    @media #{$mobile} {
      font-size: 22px;
      line-height: 1.2;
    }
  }

  &__card-text {
    font-weight: 400;
    font-size: 18px;
    line-height: 1.5;
    letter-spacing: 0;
    overflow-wrap: break-word;
  }

  &__card-button {
    padding: 18px 0;
    border-radius: 18px;
    background-color: #FFFFFF;
    color: #101014;
    width: 100%;
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: 0;
    text-align: center;
    margin-top: auto;
    @media #{$mobile} {
      color:#345686;
    }

  }


  &__card-button {
    display: block;
  }

}

.course-announcements {
  display: flex;
  flex-direction: column;
  gap: 60px;
  @media #{$mobile} {
    gap: 32px;
  }


  &__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__header-title {
    font-weight: 700;
    font-size: 80px;
    line-height: 1.2;
    letter-spacing: 0;
    @media #{$mobile} {
      font-size: 32px;
    }
  }

  &__header-button {
    width: 277px;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 90px;
    color: #345686;
    border: 1px solid #345686;
    text-decoration: none;
    @media #{$mobile} {
      display: none;
    }
  }

  &__card {
    display: flex;
    flex-direction: column;
    gap: 10px;
    min-height: 601px;
    @media #{$mobile} {
      min-height: 0;
    }
  }

  &__card-title {
    font-weight: 700;
    font-size: 32px;
    line-height: 1.5;
    letter-spacing: 0;
    @media #{$mobile} {
      font-size: 22px;
      line-height: 1.2;
      max-width: 343px;
    }

  }

  &__card-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__card-img {
    width: 100%;
  }

  &__card-link {
    text-decoration: none;
    color: black;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  &__content {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 40px;
    @media #{$mobile} {
      grid-template-columns: 1fr;
      gap: 40px;
    }
  }

  &__card-header {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  &__card-content {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  &__info-name {
    font-weight: 400;
    font-size: 18px;
    line-height: 1.5;
    letter-spacing: 0;
  }

  &__date {
    font-weight: 400;
    font-size: 18px;
    line-height: 150%;
    letter-spacing: 0;
  }

  &__card-text {
    font-weight: 400;
    font-size: 18px;
    line-height: 1.5;
    letter-spacing: 0;
    @media #{$mobile} {
      font-size: 18px;
    }
  }

  &__card-button-container {
    display: flex;
    gap: 10px;
  }


  &__card-button {
    border-radius: 90px;
    width: 180px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #345686;
    @media #{$mobile} {
      height: 46px;
      width: 100%;
    }
  }

  &__card-button--blue {
    background-color: #345686;
    color: #FFFFFF;

  }

  &__card-button--white {
    background-color: #FFFFFF;
    color: #345686;
  }

  &__text-fatty {
    font-weight: bold;
  }


}


</style>