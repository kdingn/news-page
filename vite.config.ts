import vue from "@vitejs/plugin-vue";
import fileURLToPath from "file-url-to-path";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [vue()],
  base: "/news-page/",
  resolve: {
    alias: [
      {
        find: "@",
        replacement: fileURLToPath(`${new URL("./src", import.meta.url)}`),
      },
    ],
  },
});
