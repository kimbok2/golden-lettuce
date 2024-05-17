<template>
  <div class="text-start">
    <!-- 지도 검색창 -->
    <div class="map-search-box border">
      <input type="text" />
      <input type="submit" />
    </div>
    <!-- 지도 그림 및 목록을 출력할 태그 -->
    <div class="d-flex">
      <div id="map" ref="mapContainer" style="width: 600px; height: 600px"></div>

      <!-- 은행 반복 -->
      <ul v-if="markerList" class="list-group overflow-y-scroll border rounded-0" style="height: 600px; width: 400px">
        <template v-for="data in markerList" :key="data.id">
          <li v-if="!data.place_name.includes('ATM')" class="list-group-item p-0" style="min-height: 175px">
            <div
              class="bg-primary-subtle py-1 px-3"
              style="min-height: 50px"
            >
              <!-- 은행 이름 -->
              <p class="fw-bold m-0">{{ data.place_name }}</p>
              <!-- 은행까지의 거리 -->
              <div class="d-flex justify-content-between align-items-center ">
                <span class="text-primary"> {{ data?.distance }} km</span>
                <!-- 은행 전화번호 -->
                <span v-show="data.phone" class="text-body-tertiary">{{ data.phone }}</span>
              </div>
            </div>
            <hr />
          </li>
        </template>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useScriptTag } from '@vueuse/core'
import { useUserStore } from '@/stores/user'

const API_KEY_MAP = import.meta.env.VITE_API_KEY_MAP
const mapScriptSrc = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY_MAP}&libraries=services`

const mapContainer = ref(null)

// 지도 객체 선언
const mapObject = ref(null)
let infowindow
const markerList = ref([])

// 지도 검색을 위한 변수 설정
const mapCenter = ref({ y: 36.3549777, x: 127.2983403 })
const mapLevel = ref(5)

// 지도 검색 인자에 전달할 키워드
const searchKeyWordCity = ref(null)
const searchKeyWord = ref(null)
const searchKeyWordDefault = ref('은행')

// mapCenter가 변경됐을 때를 보는 감시하는 함수
watch(
  mapCenter,
  (newMapCenter) => {
    searchCurrentMap()
    console.log('mapCenter : ', mapCenter.value)
  },
  { deep: true }
)

// mapCenter가 변경됐을 때를 보는 감시하는 함수
watch(
  mapLevel,
  (newMapLevel) => {
    searchCurrentMap()
    console.log('mapLevel : ', mapLevel.value)
  },
  { deep: true }
)

// 지도의 Script를 Load하는 함수
// script 태그를 별도로 생성해서, html의 head 안에 넣어줌
const loadScript = function () {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script')
    // 동적 로딩을 위한 autoload=false 추가
    script.src = mapScriptSrc
    script.addEventListener('load', () => kakao.maps.load(initMap))
    document.head.appendChild(script)
    // 로드 완료 메세지
    // console.log('loadScript 함수 실행 완료')
    resolve()
  })
}

// 초기 지도를 실제로 띄워주는 함수
const initMap = () => {
  const mapOptions = {
    //
    center: new kakao.maps.LatLng(mapCenter.value.y, mapCenter.value.x),
    level: mapLevel.value,
  }
  mapObject.value = new kakao.maps.Map(mapContainer.value, mapOptions)
  console.log('initMap 함수 실행 완료')

  infowindow = new kakao.maps.InfoWindow({ zIndex: 1, border: 'none' })

  if (mapObject.value) {
  }
  // 지도 객체가 Load되면 할 동작
  mapLevel.value = mapObject.value.getLevel()

  // 마우스 드래그로 지도 이동이 완료되었을 때 마지막 파라미터로 넘어온 함수를 호출하도록 이벤트를 등록합니다
  kakao.maps.event.addListener(mapObject.value, 'dragend', function () {
    // 지도 중심좌표를 얻어옵니다
    const latlng = mapObject.value.getCenter()

    mapCenter.value = {
      y: latlng.getLat(),
      x: latlng.getLng(),
    }
  })

  // 지도가 확대 또는 축소되면 마지막 파라미터로 넘어온 함수를 호출하도록 이벤트를 등록합니다
  kakao.maps.event.addListener(mapObject.value, 'zoom_changed', function () {
    // 지도의 현재 레벨을 얻어옵니다
    mapLevel.value = mapObject.value.getLevel()
  })

  // defaultMarker 함수 실행
  searchCurrentMap()
}

// Mount 훅에서 지도를 불러오는 동작 수행
// 지도 script가 (kakao.maps) 로드돼있으면 initMap, 아니면 loadScript
onMounted(() => {
  if (window.kakao?.maps) {
    console.log('onMount : 지도 Script가 이미 load되어 있음 -> initMap 함수 실행')
    initMap()
  } else {
    console.log('onMount : 지도 Script가 load되어있지 않음 -> loadScript 함수 실행')
    loadScript()
  }
})

// 현재 위치 및 검색어를 받아서 지도를 불러올 함수
const searchCurrentMap = () => {
  // 장소 검색 객체를 생성합니다
  const ps = new kakao.maps.services.Places(mapObject.value)

  ps.keywordSearch(searchKeyWordDefault.value, placesSearchCB, { useMapBounds: true })
}

// 카테고리 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
  console.log(`status: ${status}`)
  if (status === kakao.maps.services.Status.OK) {
    for (let i = 0; i < data.length; i++) {
      // 조건문으로 ATM 제거
      if (!data[i].place_name.includes('ATM')) {
        const distance = getDistance(mapCenter.value.y, mapCenter.value.x, data[i].y, data[i].x)
        data[i]['distance'] = parseFloat(distance.toFixed(2)).toString()
        console.log(distance)
        displayMarker(data[i])
      }
    }

    markerList.value = data.sort((a, b) => {
      return a.distance - b.distance
    })
  }
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {
  // 마커를 생성하고 지도에 표시합니다
  const marker = new kakao.maps.Marker({
    map: mapObject.value,
    position: new kakao.maps.LatLng(place.y, place.x),
  })

  // 마커에 클릭이벤트를 등록합니다
  kakao.maps.event.addListener(marker, 'click', function () {
    mapCenter.value = {
      y: place.y,
      x: place.x,
    }
    console.log(mapCenter.value)
    initMap()
    // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
    // 인포윈도우 표시
    console.log(place.place_name)
    infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>')
    infowindow.open(mapObject.value, marker)
  })

  // 마커에 마우스오버 이벤트를 등록합니다
  kakao.maps.event.addListener(marker, 'mouseover', function () {
    // 마커에 마우스오버 이벤트가 발생하면 인포윈도우를 마커위에 표시합니다
    infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>')
    infowindow.open(mapObject.value, marker)
  })
}
// 위도와 경도 사이의 거리를 구하는 함수
function getDistance(lat1, lon1, lat2, lon2) {
  const R = 6371 // 지구의 반경 (단위: km)
  const dLat = deg2rad(lat2 - lat1) // 위도 차이 (라디안)
  const dLon = deg2rad(lon2 - lon1) // 경도 차이 (라디안)
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * Math.sin(dLon / 2) * Math.sin(dLon / 2)
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
  const distance = R * c // 거리 (단위: km)
  return distance
}

// 각도 -> 라디안 변환 함수
function deg2rad(deg) {
  return deg * (Math.PI / 180)
}
</script>

<style scoped>
hr {
  margin-top: 0;
}

.map-search-box {
  width: 1000px;
  height: 100px;
}
</style>
