<script setup lang="ts">
const props = defineProps<{
  articles: { [k: string]: string }[];
}>();
</script>

<template>
  <div class="recent-contents">
    {{ props.articles }}
  </div>
</template>
