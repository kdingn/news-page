<script setup lang="ts">
import Header from "./components/Header.vue";
import Card from "./components/Card.vue";

import { reactive } from "vue";
type articleType = { [k: string]: string };
const articlePath = "src/assets/articles.csv";
const articles = reactive<Array<articleType>>([]);

fetch(articlePath)
  .then((res) => {
    return res.text();
  })
  .then((data) => {
    const rows = data.split("\r\n");
    const columns = rows[0].split(",");
    rows.slice(1).forEach((row) => {
      const values = row.split(",");
      articles.push(
        Object.fromEntries(columns.map((key, i) => [key, values[i]]))
      );
    });
  });
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
}
.background {
  background-image: url("./assets/background.avif");
  background-position: center center;
  background-size: cover;
  background-attachment: fixed;
  min-height: 100vh;
}
</style>
