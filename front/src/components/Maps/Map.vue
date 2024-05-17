<template>
  <div>
    <h1>MapView</h1>
    <div class="text-start">
      <input type="text" />
      <input type="submit" />
    </div>
    <div style="min-height: 50px; min-width: 50px">
      <ul v-if="markerList">
        <template v-for="data in markerList">
          <li v-if="!data.place_name.includes('ATM')">
            {{ data.place_name }}
          </li>
        </template>
      </ul>
    </div>
    <div id="map" ref="mapContainer" style="width: 500px; height: 300px"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useScriptTag } from '@vueuse/core'

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
const searchKeyWord = ref(null)

// mapCenter가 변경됐을 때를 보는 감시하는 함수
watch(
  mapCenter,
  (newMapCenter) => {
    searchCurrentMap()
    console.log(mapObject.value)
  },
  { deep: true }
)

// mapCenter가 변경됐을 때를 보는 감시하는 함수
watch(
  mapLevel,
  (newMapLevel) => {
    searchCurrentMap()
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
    // infowindow
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

  infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })


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

    let message = '변경된 지도 중심좌표는 ' + latlng.getLat() + ' 이고, '
    message += '경도는 ' + latlng.getLng() + ' 입니다'

    console.log(message)
  })

  // defaultMarker 함수 실행
  searchCurrentMap()
}

// Mount 훅에서 지도를 불러오는 동작 수행
// 지도 script가 (kakao.maps) 로드돼있으면 initMap, 아니면 loadScript
onMounted(() => {
  if (window.kakao?.maps) {
    console.log('지도 Script가 이미 load되어 있음 -> initMap 함수 실행')
    initMap()
  } else {
    console.log('지도 Script가 load되어있지 않음 -> loadScript 함수 실행')
    loadScript()
  }
})

const searchCurrentMap = () => {
  // 마커 정보를 설정할 함수
  // 장소 검색 객체를 생성합니다
  const ps = new kakao.maps.services.Places(mapObject.value)

  // 카테고리로 은행을 검색합니다
  ps.categorySearch('BK9', placesSearchCB, { useMapBounds: true })
}

// 카테고리 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
  markerList.value = data
  console.log(markerList.value)
  console.log(`status: ${status}`)
  if (status === kakao.maps.services.Status.OK) {
    for (let i = 0; i < data.length; i++) {
      // 조건문으로 ATM 제거
      if (!data[i].place_name.includes('ATM')) {
        displayMarker(data[i])
      }
    }
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
    // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
    // 인포윈도우 표시
    console.log(place.place_name)
    infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>')
    infowindow.open(mapObject.value, marker)
  })
}
</script>

<style scoped></style>
