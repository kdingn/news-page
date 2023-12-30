import { defineStore } from "pinia";

function isSmartPhone() {
  if (navigator.userAgent.match(/iPhone|Android.+Mobile/)) {
    return true;
  } else {
    return false;
  }
}

export const useDeviceStore = defineStore("device", () => {
  const spMode = isSmartPhone();
  return { spMode };
});
