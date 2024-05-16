<template>
  <div>
    <h1>MyAccountView</h1>
    <button @click="logOut" class="btn btn-primary mx-1">로그아웃</button>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";

const store = useUserStore();
const logOut = function () {
  store.logOut();
};
</script>

<style scoped></style>
