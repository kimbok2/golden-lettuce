<template>
  <!-- 지도 그림 및 목록을 출력할 태그 -->
  <div class="d-flex">
    <!-- 지도 그림 태그 -->
    <div id="map" ref="mapContainer" style="width: 600px; height: 600px"></div>

    <!-- 은행 리스트 태그 -->
    <ul v-if="bankSearchList" class="list-group overflow-y-scroll border rounded-0" style="height: 600px; width: 400px">
      <template v-for="bank in bankSearchList" :key="`${bank.id}`">
        <li class="list-group-item p-0" style="min-height: 175px">
          <div class="bg-primary-subtle py-1 px-3" style="min-height: 50px">
            <!-- 은행 이름 -->
            <p class="fw-bold m-0">{{ bank.place_name }}</p>
            <!-- 은행까지의 거리 -->
            <div class="d-flex justify-content-between align-items-center">
              <span class="text-primary"> {{ bank?.distance }} km</span>
              <!-- 은행 전화번호 -->
              <span v-show="bank.phone" class="text-body-tertiary">{{ bank.phone }}</span>
            </div>
          </div>
          <hr />
        </li>
      </template>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useMapStore } from '@/stores/map'

const API_KEY_MAP = import.meta.env.VITE_API_KEY_MAP
const mapScriptSrc = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY_MAP}&libraries=services`

// mapStore 선언
const mapStore = useMapStore()
const userStore = useUserStore()

// 지도 컨테이너
const mapContainer = ref(null)

// 지도 객체 선언
const mapObject = ref(null)
let infowindow
const bankSearchList = ref([])

// 지도 검색을 위한 변수 설정
// const mapCenter = ref(null)
const mapCenter = ref({ y: 36.3549777, x: 127.2983403 })
const mapLevel = ref(5)

// 지도 검색 인자에 전달할 키워드
const searchKeyWordDefault = ref('은행')
const searchKeyWordInput = computed(() => mapStore.searchKeyWord)
const selectedBank = ref('')

// mapStore의 선택 은행이 변경됨을 감시하는 함수
watch(
  () => mapStore.selectedBank,
  (newBank) => {
    initMap()
    selectedBank.value = newBank
  }
)

// mapCenter가 변경됐을 때를 보는 감시하는 함수
watch(
  mapCenter,
  (newMapCenter) => {
    searchCurrentMap()
    console.log('지도 중심 위도 / 경도 : ', mapCenter.value)
    console.log(bankSearchList.value)
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

// 사용자의 검색어가 변경되었을 때를 감시하는 함수 - 검색어로 지도 조회
watch(
  searchKeyWordInput,
  (newKeyWord) => {
    searchKeyWordMap()
    console.log('searchKeyWord : ', newKeyWord)
  },
  { deep: true }
)

const kakaoMapScript = ref(null)

// 지도의 Script를 Load하는 함수
// script 태그를 별도로 생성해서, html의 head 안에 넣어줌
const loadScript = function () {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script')
    script.src = mapScriptSrc
    kakaoMapScript.value = script
    document.head.appendChild(script)

    script.onload = function () {
      kakao.maps.load(() => {
        if (userStore.userInfo.address) {
          console.log(userStore.userInfo.address)
          const geocoder = new kakao.maps.services.Geocoder()

          geocoder.addressSearch(userStore.userInfo.address, function (result, status) {
            if (status === kakao.maps.services.Status.OK) {
              // 검색 성공시 지도 중심 좌표를 변경 후 해당 좌표로 지도 검색
              mapCenter.value = {
                y: result[0].y,
                x: result[0].x,
              }
              kakao.maps.load(initMap)
            } else {
              console.log(status)
            }
          })
        } else {
          kakao.maps.load(initMap)
        }
      })
    }
    // 로드 완료 메세지
    resolve(console.log('loadScript 함수 실행 완료'))
  })
}

// 초기 지도를 실제로 띄워주는 함수
const initMap = () => {
  clearMarkers()
  markerList.value = []

  const mapOptions = {
    //
    center: new kakao.maps.LatLng(mapCenter.value.y, mapCenter.value.x),
    level: mapLevel.value,
  }
  mapObject.value = new kakao.maps.Map(mapContainer.value, mapOptions)
  console.log('initMap 함수 실행 완료')

  infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })

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

  // 현재 지도 검색 함수 실행
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

// Unmount 훅에서 클린업 작업 수행
onUnmounted(() => {
  if (mapObject.value) {
    // 지도와 관련된 리소스 해제
    kakao.maps.event.removeListener(mapObject.value, 'dragend')
    kakao.maps.event.removeListener(mapObject.value, 'zoom_changed')
    mapObject.value = null
    console.log('onUnmounted : 지도 관련 리소스 해제 완료')
  }

  if (kakaoMapScript.value) {
    // 스크립트 태그를 제거
    document.head.removeChild(kakaoMapScript.value)
    kakaoMapScript.value = null
    console.log('onUnmounted : 스크립트 태그 제거 완료')
  }

  if (window.kakao) {
    // window.kakao 객체와 하위 객체 제거
    delete window.kakao
    console.log('onUnmounted : window.kakao 객체 제거 완료')
  }
})

// 현재 위치 및 검색어를 받아서 지도를 불러올 함수
const searchCurrentMap = () => {
  // 장소 검색 객체를 생성합니다
  const ps = new kakao.maps.services.Places(mapObject.value)

  // 검색 키워드 출력
  // console.log('검색 키워드 :', searchKeyWordDefault.value)
  ps.keywordSearch(searchKeyWordDefault.value, placesSearchCB, { useMapBounds: true })
}

// 사용자가 입력한 검색어에 따라서 지도를 불러올 함수
const searchKeyWordMap = () => {
  // 주소 - 좌표 반환 객체 생성

  const geocoder = new kakao.maps.services.Geocoder()

  geocoder.addressSearch(searchKeyWordInput.value, function (result, status) {
    if (status === kakao.maps.services.Status.OK) {
      // 검색 성공시 지도 중심 좌표를 변경 후 해당 좌표로 지도 검색
      mapCenter.value = {
        y: result[0].y,
        x: result[0].x,
      }
      initMap()
    } else {
      alert('주소 검색에 실패했습니다. 올바른 주소를 입력해주세요.')
    }
  })
}

// 카테고리 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
  console.log(`placesSearchCB 함수 호출 : ${status}`)
  if (status === kakao.maps.services.Status.OK) {
    bankSearchList.value = []
    for (let i = 0; i < data.length; i++) {
      if (
        // 조건문으로 ATM, 365 제거
        data[i].place_name.includes('ATM') ||
        data[i].place_name.includes('365') ||
        !data[i].place_name.includes(selectedBank.value)
      ) {
      } else {
        const distance = getDistance(mapCenter.value.y, mapCenter.value.x, data[i].y, data[i].x)
        data[i]['distance'] = parseFloat(distance.toFixed(2)).toString()
        // 지도 출력 확인
        bankSearchList.value.push(data[i])
        displayMarker(data[i])
      }
    }

    bankSearchList.value = bankSearchList.value.sort((a, b) => {
      return a.distance - b.distance
    })
  }
}

// 마커를 저장할 배열
const markerList = ref([])

// 마커를 제거하는 함수
const clearMarkers = () => {
  for (let i = 0; i < markerList.value.length; i++) {
    markerList.value[i].setMap(null)
  }
  markerList.value = []
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {
  // 마커를 생성하고 지도에 표시합니다
  const marker = new kakao.maps.Marker({
    map: mapObject.value,
    position: new kakao.maps.LatLng(place.y, place.x),
  })

  markerList.value.push(marker)

  // 마커에 클릭이벤트를 등록합니다
  kakao.maps.event.addListener(marker, 'click', function () {
    mapCenter.value = {
      y: place.y,
      x: place.x,
    }
    // console.log(mapCenter.value)
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
</style>
