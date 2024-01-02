import { defineStore } from "pinia";

function isSmartPhone() {
  if (
    window.matchMedia &&
    window.matchMedia("(max-device-width: 640px)").matches
  ) {
    return true;
  } else {
    return false;
  }
  // if (navigator.userAgent.match(/iPhone|Android.+Mobile/)) {
  //   return true;
  // } else {
  //   return false;
  // }
}

export const useDeviceStore = defineStore("device", () => {
  const spMode = isSmartPhone();
  return { spMode };
});
