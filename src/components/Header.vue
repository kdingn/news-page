<script setup lang="ts">
const title: string = "TECH NEWS LINKS";
</script>

<template>
  <div class="header">
    <div class="header-content">
      <span class="title">
        {{ title }}
      </span>
    </div>
  </div>
</template>

<style scoped>
.header {
  position: sticky;
  top: 0;
  background-color: black;
  width: 100%;
  opacity: 0.8;
}

.header-content {
  padding-left: 1rem;
  vertical-align: middle;
}
.title {
  color: white;
  font-size: 4rem;
  font-family: "Times New Roman", Times, serif;
}
</style>
