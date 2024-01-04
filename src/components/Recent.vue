<script setup lang="ts">
import { onMounted, reactive, ref } from "vue";

const props = defineProps<{
  articles: { [k: string]: string }[];
}>();

const numArticles = props.articles.length;
const cardWidth = 800;
const sidebarWidth = 280;
const selected = ref<number>(0);
const styles = reactive<{ [k: string]: string }[]>(
  [...Array(numArticles).keys()].map(() => {
    return {
      left: "",
      "z-index": "",
      transform: "",
    };
  })
);

function setStyle(j: number) {
  var offset = 0;
  if (window.innerWidth - sidebarWidth - cardWidth > 0) {
    offset = (window.innerWidth - sidebarWidth - cardWidth) / (numArticles - 1);
  }
  for (let i = 0; i < numArticles; i++) {
    styles[i]["left"] = offset * i + "px";
    styles[i]["z-index"] = String(numArticles - Math.abs(j - i));
    styles[i]["transform"] = "Scale(" + (1 - Math.abs(j - i) * 0.002) + ")";
  }
}
setStyle(selected.value);

function update() {
  setStyle(selected.value);
}
onMounted(() => window.addEventListener("resize", update));
</script>

<template>
  <div class="recent-contents">
    <div v-for="i in numArticles">
      <div v-on:mouseover="setStyle(i - 1)">
        <a
          :href="props.articles[i - 1].link"
          target="_black"
          class="recent-link"
        >
          <img
            :src="props.articles[i - 1].ogimage"
            :style="styles[i - 1]"
            class="recent-card"
          />
        </a>
      </div>
    </div>
  </div>
</template>
