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

import { ref } from "vue";
const title = "NEWS LINKS";
const loadingActive = ref<boolean>(false);
function switchLoading() {
  loadingActive.value = false;
}
setTimeout(switchLoading, 2000);

const arcTitle = "— Archive —";
</script>

<template>
  <Transition>
    <div class="loading-wrap" v-if="loadingActive.valueOf() && pcMode">
      <div class="loading-content">
        <div class="loading-text">
          <span class="easein">{{ title }}</span>
        </div>
      </div>
    </div>
  </Transition>
  <div class="whole-contents">
    <Header />
    <div class="sidebar" v-if="pcMode">
      <Sidebar />
    </div>
    <div class="contents">
      <div v-if="pcMode">
        <Recent :articles="recArticles" />
      </div>
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

<style>
.loading-wrap {
  position: absolute;
  width: 100vw;
  height: 100vh;
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
.easein {
  animation: blinking 2s ease-in;
}
@keyframes blinking {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
.v-enter-active,
.v-leave-active {
  transition: opacity 2s ease;
}
.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
