<script setup lang="ts">
import sources from "../assets/sources.csv";
</script>

<template>
  <div v-for="source in sources" class="sidebar-page">
    <a :href="source.source" target="_blank" class="sidebar-page-link">
      {{ source.title }}
      <img :src="source.ogimage" class="sidebar-page-image" loading="lazy" />
    </a>
    <hr />
  </div>
  <!-- <hr /> -->
</template>
