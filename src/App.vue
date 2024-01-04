<script setup lang="ts">
import Card from "./components/Card.vue";
import Header from "./components/Header.vue";
import Recent from "./components/Recent.vue";
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
const recday = new Date();
recday.setDate(recday.getDate() - 7);
articles.map((x: { [k: string]: string }) => {
  if (new Date(x.date) > recday) {
    recArticles.push(x);
  }
});

const arcTitle = "— Archive —";
</script>

<template>
  <div class="background">
    <Header />
    <div class="sidebar" v-if="pcMode">
      <Sidebar />
    </div>
    <div class="contents">
      <div v-if="pcMode">
        <Recent :articles="recArticles" />
      </div>
      <!-- <div class="contents-hr" v-if="pcMode"><hr color="black" size="1" /></div> -->
      <div class="contents-cards">
        <div class="contents-title-block" v-if="pcMode">
          <span class="contents-title">{{ arcTitle }}</span>
        </div>
        <div v-for="article in articles">
          <Card :article="article" />
        </div>
      </div>
    </div>
  </div>
</template>
