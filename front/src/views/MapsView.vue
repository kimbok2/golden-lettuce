<template>
  <div>
    <h1>MapsView</h1>
    <div id="map" ref="mapContainer" style="width: 500px; height: 400px"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useScriptTag } from '@vueuse/core'

const API_KEY_MAP = 'e9369f485e6ce5f8ff90ff269f8b6572'

const mapContainer = ref(null)

const initMap = () => {
  if (!window.kakao || !window.kakao.maps) {
    console.error('Kakao map script failed to load')
    return
  }

  const options = {
    center: new kakao.maps.LatLng(33.450701, 126.570667),
    level: 3,
  }
  new kakao.maps.Map(mapContainer.value, options)
}

onMounted(() => {
  const scriptLoaded = ref(false)
  useScriptTag(`//dapi.kakao.com/v2/maps/sdk.js?appkey=${API_KEY_MAP}`, () => {
    scriptLoaded.value = true
    initMap()
  })

  console.log(scriptLoaded)
})
</script>

<style scoped></style>
