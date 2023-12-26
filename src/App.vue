<script setup lang="ts">
import wholeArticles from "./assets/articles.csv";
import Card from "./components/Card.vue";
import Header from "./components/Header.vue";

let articles = wholeArticles.slice(0, 20);
</script>

<template>
  <div class="background">
    <Header />
    <div class="contents">
      <div v-for="article in articles">
        <Card :article="article" />
      </div>
    </div>
  </div>
  <!-- </div> -->
</template>

<style scoped>
.contents {
  background-color: rgba(0, 0, 0, 0.1);
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
