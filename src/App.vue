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
const arcArticles: { [k: string]: string }[] = [];
const recday = new Date();
recday.setDate(recday.getDate() - 7);
articles.map((x: { [k: string]: string }) => {
  if (new Date(x.date) > recday && recArticles.length < 7) {
    recArticles.push(x);
  } else {
    arcArticles.push(x);
  }
});

const arcTitle = "— Archive —";
const title = "— NEWS LINKS —";
var loadingActive = false;
</script>

<template>
  <div class="loading-wrap" v-if="loadingActive && pcMode">
    <div class="loading-content">
      <span class="loading-text">{{ title }}</span>
    </div>
  </div>
  <div class="whole-contents">
    <Header />
    <div class="sidebar" v-if="pcMode">
      <Sidebar />
    </div>
    <div class="contents">
      <div v-if="pcMode">
        <Recent :articles="recArticles" />
      </div>
      <div class="contents-hr" v-if="pcMode">
        <hr size="2" color="white" />
      </div>
      <div class="contents-cards">
        <div class="contents-title-block" v-if="pcMode">
          <span class="contents-title">{{ arcTitle }}</span>
        </div>
        <div v-for="article in arcArticles" v-if="pcMode">
          <Card :article="article" />
        </div>
        <div v-for="article in articles" v-else>
          <Card :article="article" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.loading-wrap {
  width: 100lvw;
  height: 100lvh;
  z-index: 1000;
  background-color: rgba(0, 0, 0);
}
.loading-content {
  display: flex;
  justify-content: center;
}
.loading-text {
  color: rgb(128, 188, 189, 0.9);
  font-size: 5rem;
  font-family: "Times New Roman", Times, serif;
  padding-top: 40vh;
}
</style>
