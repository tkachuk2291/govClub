<script setup lang="ts">

</script>

<template>

  <section class="feedback">
    <div class="feedback__header">
      <div class="feedback__header-text-container">
        <h2 class="feedback__header-title">записатись</h2>
        <p class="feedback__header-description">Шукаєте курс але в переліку його немає? напишіть нам, в нас є що
          запропонувати!</p>
      </div>
      <img alt="blue-flower" src="/feedbackForm/blue-flower.png"/>
    </div>

    <div class="feedback__content">
      <form class="feedback-form">
        <input class="feedback-form__input" placeholder="Ім’я" type="text"/>

        <input class="feedback-form__input" placeholder="Ім’я" type="text"/>

        <input class="feedback-form__input" placeholder="Ім’я" type="text"/>

        <input class="feedback-form__input" placeholder="Ім’я" type="text"/>

        <button class="feedback-form__button" type="button">Надіслати повідомлення</button>
      </form>
      <p class="feedback__text">Продовжуючи ви погоджуєтесь з <a href="#">Політикою Конфіденційності</a></p>
    </div>
  </section>


</template>

<style scoped lang="scss">
.feedback {
  //background-image: url('/feedbackForm/blue-flower.png');
  //display: grid;
  //grid-template-columns: repeat(12 , 1fr);
  //grid-auto-flow: column;
  background-color: #345686;
  border-radius: 30px;
}

</style>