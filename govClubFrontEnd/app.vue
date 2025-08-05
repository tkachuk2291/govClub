<template>
  <div>
    <Header v-show="currentWidth === 'tablet' || currentWidth === 'desktop' "></Header>
    <HeaderMobile v-show="currentWidth === 'mobile'"></HeaderMobile>
    <asideMenu v-show="currentWidth === 'mobile' && isOpen" />
    <NuxtPage/>
    <NuxtRouteAnnouncer/>
  </div>
</template>



<script setup lang="ts">
  import Header from "~/components/Header.vue";
  import {useWindowSizeSelect} from "~/composables/useScreenSize";
  import {useMobileMenu} from "~/composables/useMobileMenu";
  const currentWidth = useWindowSizeSelect()
  const {isOpen} = useMobileMenu()


</script>
