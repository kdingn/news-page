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
      <div>
        <img :src="props.article.ogimage" class="center-cropped" />
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
  font-size: 1.5rem;
}
.title {
  font-size: 2.6rem;
  margin-bottom: 1vw;
  padding-left: 2vw;
  padding-right: 2vw;
}
.center-cropped {
  width: 96vw;
  height: 100%;
  background-position: center center;
  background-repeat: no-repeat;
  outline: solid;
  outline-width: 1px;
  opacity: 0.9;
  z-index: 3;
  border-radius: 1vw;
}
.card {
  padding: 1vw;
  min-height: 49vw;
  width: 96vw;
  margin-top: 1vw;
  outline: solid;
  outline-width: 1px;
  background-color: rgb(243, 248, 255, 0.8);
  border-radius: 1vw;
}
</style>
