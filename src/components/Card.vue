<script setup lang="ts">
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
        <img
          loading="lazy"
          decoding="async"
          :src="props.article.ogimage"
          class="card-image"
        />
      </div>
    </a>
  </div>
</template>
