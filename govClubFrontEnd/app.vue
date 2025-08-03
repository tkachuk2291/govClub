<template>
  <div>
    <Header v-if="currentWidth === 'tablet' || currentWidth === 'desktop' "></Header>
    <HeaderMobile v-if="currentWidth === 'mobile'"></HeaderMobile>
    <NuxtPage/>
    <NuxtRouteAnnouncer/>
  </div>
</template>

<script setup lang="ts">
  import Header from "~/components/Header.vue";
  import {useWindowSizeSelect} from "~/composables/useScreenSize";
  const currentWidth = useWindowSizeSelect()

</script>
