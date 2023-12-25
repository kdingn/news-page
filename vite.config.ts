import dsv from "@rollup/plugin-dsv";
import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [vue(), dsv()],
  base: "/news-page/",
});
