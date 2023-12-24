<script setup lang="ts">
const props = defineProps<{
  article: { [k: string]: string };
}>();
</script>

<template>
  <div>
    {{ props.article.source }}
  </div>
  <div>
    {{ props.article.date }}
  </div>
  <div>
    {{ props.article.title }}
  </div>
  <div>
    {{ props.article.link }}
  </div>
</template>

<style></style>
