<script setup lang="ts">
import Card from "./Card.vue";

import { reactive } from "vue";
const articlePath = "src/assets/articles.csv";
const articles = reactive<any>([]);

console.log(articlePath);

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
  <div v-for="article in articles">
    <Card />
    {{ article }}
  </div>
</template>

<style scoped></style>
