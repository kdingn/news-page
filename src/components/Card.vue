<script setup lang="ts">
const props = defineProps<{
  article: { [k: string]: string };
}>();
</script>

<template>
  <div class="card">
    <a :href="props.article.link" class="card-link" target="_blank">
      <div class="card-info">
        {{ props.article.date + ", " }}
        {{ props.article.source }}
      </div>
      <div class="card-title">
        {{ props.article.title }}
      </div>
      <img
        loading="lazy"
        decoding="async"
        :src="props.article.ogimage"
        class="card-image"
      />
    </a>
  </div>
</template>
