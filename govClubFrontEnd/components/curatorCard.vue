<script setup lang="ts">
const props = defineProps({
  curatorCardProps: {
    type: Object,
    required: true
  }
})

console.log(props.curatorCardProps.section_title , 'FFF')

</script>

<template>
  <div class="curator-card">
    <div class="curator-card__header">
      <h3 class="curator-card__header-text">{{ curatorCardProps.section_title }}</h3>
    </div>
    <div class="curator-card__content">
      <img class="curator-card__img"
           :src="curatorCardProps.image"
           alt="curator"/>
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
</style>