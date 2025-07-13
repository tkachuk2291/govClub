<script setup lang="ts">

</script>

<template>

  <section class="feedback">
    <div class="feedback__container">
      <div class="feedback__header">
        <h2 class="feedback__header-title">записатись</h2>
        <p class="feedback__header-description">Шукаєте курс але в переліку його немає? напишіть нам, в нас є що
          запропонувати!</p>
      </div>

      <div class="feedback__content">
        <form class="form-feedback">
          <input class="form-feedback__input" placeholder="Ім’я" type="text"/>

          <input class="form-feedback__input" placeholder="Ім’я" type="text"/>

          <input class="form-feedback__input" placeholder="Ім’я" type="text"/>

          <input class="form-feedback__input" placeholder="Ім’я" type="text"/>

          <button class="form-feedback__button" type="button">Надіслати повідомлення</button>
        </form>
      </div>
      <p class="feedback__text">Продовжуючи ви погоджуєтесь з <a href="#">Політикою Конфіденційності</a></p>

    </div>
    <img class="feedback__img" alt="blue-flower" src="/feedbackForm/flower-blue.png"/>

  </section>


</template>

<style scoped lang="scss">
.feedback {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  background-color: #345686;
  border-radius: 30px;

  &__container {
    padding: 100px 0;
    grid-column: 3/10;
  }

  &__img {
    width: 371px;
    height: 384px;
    grid-column: 10/13;
  }

  &__header {
    display: grid;
    grid-template-rows: repeat(2, 1fr);
    grid-template-columns: repeat(11, 1fr);
  }

  &__header-title {
    grid-column: 5/8;
    font-weight: 700;
    font-size: 80px;
    line-height: 1.2;
    letter-spacing: 0;
    color: white;
  }

  &__header-description {
    grid-row: 2;
    grid-column: 4/12;
    font-weight: 400;
    font-size: 20px;
    line-height: 1.5;
    letter-spacing: 0;
    color: white;
  }

  &__text {
    font-weight: 400;
    font-size: 18px;
    line-height: 1.5;
    letter-spacing: 0;
    color: #FFFFFF;
    grid-column: 4/10;
  }


}

.form-feedback {
  display: grid;
  grid-template-rows: repeat(2, 1fr);
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 40px;

  &__input {
    border: 1px solid #899EBC;
    border-radius: 30px;
    width: 400px;
    height: 60px;
    box-sizing: border-box;
    background-color: transparent;
    padding: 16px 0 17px 16px
  }

  &__button {
    border-radius: 90px;
    background-color: #FFFFFF;
    color: #345686;
    padding: 28px 0;
    grid-column: 1/-1;
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: 0;
  }
}


</style>