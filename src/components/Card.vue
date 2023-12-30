<script setup lang="ts">
import { useDeviceStore } from "../stores/device";
const spMode = useDeviceStore().spMode;

const props = defineProps<{
  article: { [k: string]: string };
}>();
</script>

<template>
  <div class="card">
    <a :href="props.article.link" class="card-link">
      <div class="card-info">
        {{ props.article.date + ", " }}
        {{ props.article.source }}
      </div>
      <div class="card-title">
        {{ props.article.title }}
      </div>
      <div>
        <img :src="props.article.ogimage" class="card-image" />
      </div>
    </a>
  </div>
</template>

<style scoped>
.card-link {
  color: inherit;
  text-decoration: none;
}
.card-info {
  font-size: 1.5rem;
}
.card-title {
  font-size: 2.6rem;
  margin-bottom: 1vw;
  padding-left: 2vw;
  padding-right: 2vw;
}
.card-image {
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
