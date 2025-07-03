<script setup lang="ts">

</script>

<template>
  <header class="header">
    <main>
      <section class="hero">
        <h1 class="hero__title hero__item1">Gov Club відкриває двері </h1>
        <h1 class="hero__title hero__item2">державного сектору</h1>
        <div class="hero__container hero__item3">
          <p class="hero__text">Об'єднуємо людей, які вірять в Україну.</p>
          <a href="#" class="hero__button">Стати партнером</a>
        </div>
      </section>

    </main>
  </header>
</template>

<style lang="scss" scoped>
.header {
  &__title {
    color: blueviolet;
  }
}

.hero{
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: repeat(12 , 1fr);
  grid-auto-flow: column;


  &__item1 {
    grid-column: 1 / 11;
  }
  &__item2 {
    grid-column: 6 / 12;
  }
  &__item3 {
    grid-column: 1 / 13;
  }
  &__container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 150px;
  }
  &__title {
      font-family: Inter;
      font-weight: 700;
      font-size: 80px;

      //line-height: 120%;
      //letter-spacing: 0;
  }
  &__button{
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
  }
  &__text {
    max-width: 180px;
    font-family: Inter;
    font-weight: 400;
    font-size: 18px;
    line-height: 150%;
    letter-spacing: 0;

  }

}



</style>