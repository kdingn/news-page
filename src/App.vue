<script setup lang="ts">
import Card from "./components/Card.vue";
import Header from "./components/Header.vue";
import Sidebar from "./components/Sidebar.vue";

import wholeArticles from "./assets/articles.csv";
let articles = wholeArticles.slice(0, 60);

import "./styles/common.css";
const pcMode = !/Android|iPhone/i.test(navigator.userAgent);
if (pcMode) {
  import("./styles/pcStyle.css");
} else {
  import("./styles/spStyle.css");
}
</script>

<template>
  <div class="background">
    <Header />
    <div class="sidebar" v-if="pcMode">
      <Sidebar />
    </div>
    <div class="contents">
      <div v-for="article in articles">
        <Card :article="article" />
      </div>
    </div>
  </div>
</template>
