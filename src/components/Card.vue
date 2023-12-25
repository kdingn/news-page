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
  font-size: 0.6rem;
}
.title {
  font-size: 1rem;
}
.card {
  color: rgba(10, 10, 10);
  min-height: 5rem;
  outline: solid;
  margin-bottom: 0.5vw;
  margin-right: 0.5vw;
  outline-width: 1px;
  background-color: rgba(220, 220, 220, 0.9);
  width: 20rem;
  padding: 0.2vw;
  box-shadow: -5px -5px 10px 0px rgba(255, 255, 255, 0.5),
    5px 5px 10px 0px rgba(0, 0, 0, 0.3);
}
</style>
