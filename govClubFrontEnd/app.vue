<template>
  <div>
    <Header></Header>
    <arrowUp />

    <NuxtPage/>
    <NuxtRouteAnnouncer/>
  </div>
</template>



<script setup lang="ts">
  import Header from "~/components/header.vue";
</script>
