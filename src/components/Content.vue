<script setup lang="ts">
import { reactive } from "vue";
const articlePath = "src/assets/articles.csv";
const articles = reactive<any>([]);

fetch(articlePath)
  .then((res) => {
    return res.text();
  })
  .then((data) => {
    const rows = data.split("\r\n");
    const columns = rows[0].split(", ");
    rows.slice(1).forEach((row) => {
      articles.push(
        Object.fromEntries(columns.map((key, i) => [key, row.split(", ")[i]]))
      );
    });
  });
</script>

<template>
  <div v-for="article in articles">
    {{ article }}
  </div>
</template>

<style scoped></style>
