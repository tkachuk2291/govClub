<script setup lang="ts">
const {data: sections, pending, error} = await useFetch('http://localhost:8004/team/', {
  server: true,
  method: 'GET',
  headers: {
    accept: 'application/json'
  }
})
</script>
<template>
  <main class="main width-md">
    <section class="hero">
      <div class="hero-top">
        <h1 class="hero-top__title">{{sections.hero_section.title }}</h1>
        <div class="hero-top__img-container">
    <img class="hero-top__img" alt="team"  :src="sections.hero_section.image" />
        </div>
      </div>
      <div class="hero-bottom">
        <div class="hero-bottom__content">
          <h3 class="hero-bottom__content-title">{{sections.team_info.title }}</h3>
          <p class="hero-bottom__content-text">{{sections.team_info.description }}</p>
        </div>
        <img class="hero-bottom__img" alt="team" :src="sections.team_info.image"/>
      </div>
    </section>

    <section class="team">
      <curatorCard v-for="(member, index) in sections.team_member_cards"
                   :key="index"
                   :curatorCardProps="member"/>
    </section>

    <section class="feedback">
      <feedback/>
    </section>

  </main>

</template>

<style lang="scss" scoped>

.main{
  display: flex;
  flex-direction: column;
  gap: 160px;
  margin-top: 70px;
}

.team{
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
}

.hero-top {
  display: flex;
  flex-direction: column;
  gap: 70px;
  &__title {
    font-weight: 700;
    font-size: 80px;
    line-height: 1.2;
    letter-spacing: 0;
  }

  &__img {
    width: 840px;
    height: 474px;
    border-radius: 30px;
    object-fit: cover;
  }

  &__img-container {
    display: flex;
    justify-content: center;
    align-items: center;
  }
}

.hero {
  display: flex;
  flex-direction: column;
  gap: 160px;
}

.hero-bottom {
  display: flex;
  gap: 83px;

  &__content {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  &__content-title {
    font-weight: 700;
    font-size: 80px;
    line-height: 1.2;
    letter-spacing: 0;
  }

  &__content-text {
    font-weight: 400;
    font-size: 22px;
    line-height: 1.5;
    letter-spacing: 0;
  }

  &__img {
    width: 620px;
    height: 474px;
    border-radius: 30px;
  }
}
</style>