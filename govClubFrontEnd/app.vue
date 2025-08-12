<template>
  <div>
    <Header></Header>
<!--    <HeaderMobile v-else></HeaderMobile>-->
<!--    <asideMenu v-if="currentWidth === 'mobile' && isOpen" />-->
    <NuxtPage/>
    <NuxtRouteAnnouncer/>
  </div>
</template>



<script setup lang="ts">
  import Header from "~/components/Header.vue";
</script>
