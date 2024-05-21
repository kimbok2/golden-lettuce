<template>
  <div>
    <h1 class="d-flex justify-content-center">
      <span>내 주변 은행 찾기</span><span class="material-symbols-outlined mx-3" style="font-size: 50px"> map </span>
    </h1>
    <div class="map-container">
      <Map />
    </div>
  </div>
</template>

<script setup>
import Map from '@/components/Maps/Map.vue'
</script>

<style scoped>
.map-container {
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
</style>
