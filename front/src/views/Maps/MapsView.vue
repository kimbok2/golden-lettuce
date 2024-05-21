<template>
  <div>
    <h1 class="main-h1-container">
      <span>내 주변 은행 찾기</span><span class="material-symbols-outlined"> map </span>
    </h1>
    <div class="main-container">
      <Map />
    </div>
  </div>
</template>

<script setup>
import Map from '@/components/Maps/Map.vue'
</script>

<style scoped>
.main-container {
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
</style>
