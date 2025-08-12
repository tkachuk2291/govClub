<script setup lang="ts">

import {useFeedback} from "~/composables/useFeedback";

const {page} = defineProps(['page'])


const formFeedback = reactive({
  name: '',
  email: '',
  message: '',
  phone: '',
  page: page || 'unknown',
})


function resetFrom() {
  formFeedback.name = '';
  formFeedback.email = '';
  formFeedback.message = '';
  formFeedback.phone = '';
}


async function submitForm() {
  const response = await fetch('http://localhost:8005/feedback/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(formFeedback),
  });
  const data = await response.json();
  if (response.status == 201) {
    resetFrom()
  }
}


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
        <form class="form-feedback" @submit.prevent="submitForm">
          <div class="form-feedback__input-container">
            <input v-model="formFeedback.name" class="form-feedback__input" placeholder="Ім’я" type="text"/>
            <input v-model="formFeedback.email" class="form-feedback__input" placeholder="емейл" type="email"/>
            <input v-model="formFeedback.phone" class="form-feedback__input" placeholder="телефон" type="number"/>
            <input v-model="formFeedback.message" class="form-feedback__input" placeholder="ваше повідомлення"
                   type="text"/>
            <input type="hidden" class="form-feedback__input" v-model="formFeedback.pageLabel"/>

          </div>
          <button class="form-feedback__button" type="submit">Надіслати повідомлення</button>
        </form>
      </div>
      <p class="feedback__text">Продовжуючи ви погоджуєтесь з <a class="feedback__text-link" href="#">Політикою
        Конфіденційності</a></p>
    </div>
    <div class="feedback__img-container"></div>

  </section>


</template>

<style scoped lang="scss">
.feedback {
  min-height: 600px;
  position: relative;
  background-color: #345686;
  border-radius: 30px;
  @media (max-width: 768px) {
    padding: 0 20px;
    background-image: url('/feedbackForm/mobile/flower-blue-mobile.png');
    background-repeat: no-repeat;
    background-size: contain;
  }


  &__content {
    margin: 56px 0 30px 0;
  }

  &__container {
    padding: 100px 0;
    max-width: 840px;
    width: 100%;
    margin: 0 auto;
  }

  &__img-container {
    position: absolute;
    top: 0;
    right: 0;
    background-image: url('/feedbackForm/flower-blue.png');
    background-repeat: no-repeat;
    width: 400px;
    height: 400px;
    background-position: center;
    background-size: cover;


    @media (max-width: 768px) {
      display: none;
    }
  }

  &__header {
    align-items: center;
    display: flex;
    flex-direction: column;
    gap: 16px

  }

  &__header-title {
    font-weight: 700;
    font-size: 80px;
    line-height: 1.2;
    letter-spacing: 0;
    color: #FFFFFF;
    @media (max-width: 768px) {
      font-weight: 700;
      font-size: 38px;
      line-height: 1.2;
      letter-spacing: 0;
    }
  }

  &__header-description {
    width: 573px;
    font-weight: 400;
    font-size: 22px;
    line-height: 1.5;
    letter-spacing: 0;
    color: white;
    @media (max-width: 768px) {
      width: 100%;
      font-weight: 400;
      font-size: 20px;
      line-height: 1.5;
      letter-spacing: 0;
      padding: 0 20px;
    }
  }

  &__text {
    font-weight: 400;
    font-size: 18px;
    line-height: 1.5;
    letter-spacing: 0;
    color: white;
    @media (max-width: 768px) {
      font-weight: 400;
      font-size: 18px;
      line-height: 1.5;
      letter-spacing: 0;
    }

  }

  &__text-link {
    font-family: Sarala;
    font-weight: 400;
    font-size: 18px;
    line-height: 1.5;
    letter-spacing: 0;
    text-decoration: underline;
    text-decoration-style: solid;
    color: white;
  }


}

.form-feedback {
  display: flex;
  flex-direction: column;
  gap: 40px;
  @media (max-width: 768px) {
    gap: 32px
  }

  &__input-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 40px;
    @media (max-width: 768px) {
      gap: 16px
    }
  }

  &__input {
    border: 1px solid #899EBC;
    color: white;
    border-radius: 30px;
    width: 400px;
    height: 60px;
    box-sizing: border-box;
    background-color: transparent;
    padding: 16px 0 17px 16px;
    @media (max-width: 768px) {
      width: 100%;
      height: 100%;
    }
    //outline: none;
    &:focus {
      outline: none;
      border: 1px solid white;
    }

    &::placeholder {
      color: #899EBC;
    }
  }

  &__button {
    border-radius: 90px;
    background-color: #FFFFFF;
    color: #345686;
    padding: 28px 0;
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: 0;
    @media (max-width: 768px) {
      padding: 18px 0;
    }
  }
}


</style>