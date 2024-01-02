<script setup lang="ts">
import Card from "./components/Card.vue";
import Header from "./components/Header.vue";

import wholeArticles from "./assets/articles.csv";
let articles = wholeArticles.slice(0, 60);

import "./styles/common.css";
if (/Android|iPhone/i.test(navigator.userAgent)) {
  import("./styles/spStyle.css");
} else {
  import("./styles/pcStyle.css");
}
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
</template>
