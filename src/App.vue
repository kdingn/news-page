<script setup lang="ts">
import articles from "./assets/articles.csv";
import Card from "./components/Card.vue";
import Header from "./components/Header.vue";
</script>

<template>
  <div class="background">
    <Header />
    <div class="padding">
      <div class="contents">
        <div v-for="article in articles">
          <Card :article="article" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.padding {
  padding: 0.5vw;
}
.contents {
  background-color: rgba(0, 0, 0, 0.1);
  min-height: 50vh;
  padding: 0.5vw;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.background {
  background-image: url("./assets/background.avif");
  background-position: center center;
  background-size: cover;
  background-attachment: fixed;
  min-height: 100vh;
}
</style>
