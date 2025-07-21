<script setup lang="ts">

import CuratorCard from "~/components/curatorCard.vue";

const route = useRoute()
const slug = route.params.slug


const {data: detailPage, pending, error} = await useFetch(`http://localhost:8001/course-card-detail/${slug}`, {
  server: true,
  method: 'GET',
  headers: {
    accept: 'application/json'
  }
})

// const curatorCardProps = computed(() => ({
//   section_title: detailPage.value?.curator?.section_title,
//   image: detailPage.value?.curator?.image,
//   title: detailPage.value?.curator?.title,
//   text: detailPage.value?.curator?.text
// }))

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
        <CuratorCard v-if="detailPage?.curator" :curatorCardProps="detailPage.curator" />
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
      <feedback :page="slug" />
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