<template>
  <div>
    <Header v-show="currentWidth === 'tablet' || currentWidth === 'desktop' "></Header>
    <HeaderMobile v-show="currentWidth === 'mobile'"></HeaderMobile>
    <asideMenu />
    <NuxtPage/>
    <NuxtRouteAnnouncer/>
  </div>
</template>

<script setup lang="ts">
  import Header from "~/components/Header.vue";
  import {useWindowSizeSelect} from "~/composables/useScreenSize";
  const currentWidth = useWindowSizeSelect()

</script>
