<script setup lang="ts">
import Card from "./components/Card.vue";
import Header from "./components/Header.vue";
import Sidebar from "./components/Sidebar.vue";

import "./styles/common.css";
const pcMode = !/Android|iPhone/i.test(navigator.userAgent);
if (pcMode) {
  const style = import("./styles/pcStyle.css");
  new Promise((resolve) => resolve(style));
} else {
  const style = import("./styles/spStyle.css");
  new Promise((resolve) => resolve(style));
}

import articles from "./assets/articles.csv";
const recArticles: { [k: string]: string }[] = [];
const othArticles: { [k: string]: string }[] = [];
const recday = new Date();
recday.setDate(recday.getDate() - 7);
articles.map((x: { [k: string]: string }) => {
  if (new Date(x.date) > recday) {
    recArticles.push(x);
  } else {
    othArticles.push(x);
  }
});

const recTitle = "— Recent News —";
const othTitle = "— Archive —";
</script>

<template>
  <div class="background">
    <Header />
    <div class="sidebar" v-if="pcMode">
      <Sidebar />
    </div>
    <div class="contents">
      <div class="contents-title" v-if="pcMode">
        <span class="contents-title-shadow"> {{ recTitle }}</span>
      </div>
      <div class="contents-rec-cards">
        <div v-for="article in recArticles">
          <Card :article="article" />
        </div>
      </div>
      <div class="contents-hr" v-if="pcMode"><hr color="black" size="1" /></div>
      <div class="contents-title" v-if="pcMode">
        <span class="contents-title-shadow">
          {{ othTitle }}
        </span>
      </div>
      <div class="contents-rec-cards">
        <div v-for="article in othArticles">
          <Card :article="article" />
        </div>
      </div>
    </div>
  </div>
</template>
