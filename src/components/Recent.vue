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
var timer = 0;
const interval = 30;
const timerInterval = 60000 * 5;
const timerShowbar = 10000;
const elapsedwidth = ref<{ width: string }>({ width: "0%" });
const showbar = ref<boolean>(false);

function setStyle(j: number) {
  var offset = 0;
  if (window.innerWidth - sidebarWidth - cardWidth > 0) {
    offset = (window.innerWidth - sidebarWidth - cardWidth) / (numArticles - 1);
  }
  for (let i = 0; i < numArticles; i++) {
    styles[i]["left"] = offset * i + "px";
    styles[i]["z-index"] = String(numArticles - Math.abs(j - i));
    styles[i]["transform"] = "Scale(" + (1 - Math.abs(j - i) * 0.01) + ")";
  }
  if (selected.value != j) {
    selected.value = j;
    timer = 0;
    elapsedwidth.value.width = "0%";
    showbar.value = false;
  }
}
setStyle(selected.value);

function updateElapsedwidth() {
  timer += interval;
  if (timer >= timerInterval - timerShowbar) {
    elapsedwidth.value.width =
      ((timerShowbar - timerInterval + timer) / timerShowbar) * 100 + "%";
    showbar.value = true;
  }
  if (timer >= timerInterval) {
    selected.value = (selected.value + 1) % numArticles;
    setStyle(selected.value);
    timer = 0;
    elapsedwidth.value.width = "0%";
    showbar.value = false;
  }
}
setInterval(updateElapsedwidth, interval);

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
          <div
            :style="styles[i - 1]"
            class="recent-textbox"
            v-if="selected.valueOf() == i - 1"
          >
            <span class="recent-info">
              {{ props.articles[i - 1].date + ", " }}
              {{ props.articles[i - 1].source }}
            </span>
            <span class="recent-text">{{ props.articles[i - 1].title }}</span>
            <hr
              class="recent-timeline"
              :style="elapsedwidth"
              color="white"
              v-if="showbar"
            />
          </div>
        </a>
      </div>
    </div>
  </div>
  <hr class="recent-devider" />
</template>
