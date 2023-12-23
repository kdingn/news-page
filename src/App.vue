<script setup lang="ts">
import Header from "./components/Header.vue";
</script>

<template>
  <div class="background">
    <div class="align-center"><Header /></div>
  </div>
</template>

<style scoped>
.align-center {
  display: flex;
  justify-content: center;
}
.background {
  /* background-image: url("./assets/background.avif"); */
  background-image: url("./assets/background.avif");
  height: 100vh;
  background-position: center center;
  background-size: cover;
}
</style>
