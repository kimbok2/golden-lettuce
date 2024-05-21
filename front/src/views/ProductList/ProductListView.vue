<template>
  <div>
    <h1 class="main-h1-container">
      <span>상품 검색</span>
      <span class="material-symbols-outlined"> find_in_page </span>
    </h1>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped></style>
