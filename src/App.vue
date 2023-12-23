<script setup lang="ts">
import Header from "./components/Header.vue";
</script>

<template>
  <div class="background">
    <Header />
    <div class="padding">
      <div class="contents">
        <div v-for="i in 100" :key="i">{{ i }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.padding {
  padding: 1vw;
}
.contents {
  background-color: black;
  opacity: 0.1;
}
.background {
  background-image: url("./assets/background.avif");
  background-position: center center;
  background-size: cover;
  background-attachment: fixed;
}
</style>
