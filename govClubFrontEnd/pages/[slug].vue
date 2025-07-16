<script setup lang="ts">

const route = useRoute()
const slug = route.params.slug


const {data: detailPage, pending, error} = await useFetch(`http://localhost:8001/course-card-detail/${slug}`, {
  server: true,
  method: 'GET',
  headers: {
    accept: 'application/json'
  }
})
console.log(detailPage , 'DD')

</script>

<template>
  <main class="main width-md">
    <section class="hero width-sm">
      <div class="hero-content-top">
        <div class="course-card">
          <div class="course-card__header">
            <div class="course-card__header-container">
              <h2 class="course-card__date">{{detailPage.hero_section.date}}</h2>
              <a href="#" class="course-card__button">Записатися</a>
            </div>
            <h3 class="course-card__title">{{detailPage.hero_section.section_title}}</h3>
          </div>
          <div class="course-card__content">
            <img
                class="course-card__img"
                alt="course"
                :src="detailPage.hero_section.image"
            />

          </div>
        </div>


      </div>
      <div class="hero-content-bottom">
        <div class="curator-card">
          <div class="curator-card__header">
            <h3 class="curator-card__header-text">{{detailPage.curator.section_title}}</h3>
          </div>
          <div class="curator-card__content">
            <img class="curator-card__img"
                 :src="detailPage.curator.image"
                 alt="curator"/>
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
      <h2 class="info__title">{{detailPage.about_course.section_title}}</h2>
      <p class="info__text">{{detailPage.about_course.description}}</p>
    </section>
    <section class="conference width-sm">

            <img class="conference__img"
                 :src="detailPage.course_photo.image"
                 alt="conference"/>
    </section>
    <section class="feedback">
      <feedback/>
    </section>
  </main>
</template>

<style scoped lang="scss">

.main {
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
    font-family: Sarala;
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

  &__title {
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

.conference {
  &__img {
    border-radius:30px;
    width: 840px;
  }
}


</style>