<script setup lang="ts">
import Content from "@/components/Content.vue";
import Header from "@/components/Header.vue";
</script>

<template>
  <div class="background">
    <Header />
    <div class="padding">
      <div class="contents">
        <Content />
      </div>
    </div>
  </div>
</template>

<style scoped>
.padding {
  padding: 0.5vw;
}
.contents {
  background-color: rgba(0, 0, 0, 0.1);
  min-height: 50vh;
}
.background {
  background-image: url("@/assets/background.avif");
  background-position: center center;
  background-size: cover;
  background-attachment: fixed;
  min-height: 100vh;
}
</style>
