<script setup lang="ts">
const props = defineProps<{
  article: { [k: string]: string };
}>();
</script>

<template>
  <div class="card">
    <a :href="props.article.link">
      <div class="date">
        {{ props.article.date }}
      </div>
      <div class="title">
        {{ props.article.title }}
      </div>
    </a>
  </div>
</template>

<style scoped>
a {
  color: inherit;
  text-decoration: none;
}
.date {
  font-size: 1rem;
}
.title {
  font-size: 2rem;
}
.card {
  height: 49vw;
  width: 98vw;
  margin-top: 1vw;
  outline: solid;
  outline-width: 1px;
  background-color: rgba(255, 255, 255, 0.5);
}
</style>
