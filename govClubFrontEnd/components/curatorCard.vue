<script setup lang="ts">
const props = defineProps({
  curatorCardProps: {
    type: Object,
    required: true,
  },
})



</script>

<template>
  <div class="curator-card">
    <div class="curator-card__header">
      <h3 class="curator-card__header-text">{{ curatorCardProps.section_title }}</h3>
    </div>
    <div class="curator-card__content">
      <div class="curator-card__img_container">
        <img class="curator-card__img"
             :src="curatorCardProps.image"
             alt="curator"/>
      </div>
      <div class="curator-card__text-container">
        <h4 class="curator-card__title">{{ curatorCardProps.fullname }}</h4>
        <p class="curator-card__text">{{ curatorCardProps.description }}</p>
      </div>
    </div>

  </div>
</template>

<style scoped lang="scss">
.curator-card {
  display: flex;
  flex-direction: column;
  gap: 30px;
  width: 400px;
  @media (max-width: 768px) {
    margin: 0 auto;
  }

  &__header-text {
    font-weight: 700;
    font-size: 32px;
    line-height: 1.5;
    letter-spacing: 0;
    @media (max-width: 768px) {
      font-size: 22px;
      line-height: 1.2;

    }
  }

  &__img {
    width: 400px;
    height: 400px;
    @media (max-width: 768px) {
      width: 182px;
      height: 182px;
    }

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
    @media (max-width: 768px) {
      font-size: 16px;
      line-height: 1.5;
    }
  }

  &__text {
    font-weight: 400;
    font-size: 18px;
    line-height: 1.5;
    letter-spacing: 0;
    color: #4D5358;
  }
  &__img_container{
    display: flex;
    @media (max-width: 768px) {
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }
}

</style>