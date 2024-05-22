<template>
  <div class="text-start">
    <!-- 지도 검색창 -->
    <div class="map-search-box p-3">
      <div class="d-flex flex-row justify-content-between">
        <form class="d-flex" @submit.prevent="updateMapSearchKeyWord">
          <input
            class="form-control inline-block"
            style="width: 400px"
            type="text"
            v-model="searchKeyWordInput"
            placeholder="주소를 입력해주세요."
            maxlength="20"
          />
          <select ref="selectBankTag" @change="selectBank" class="form-select ms-2" style="width: 150px">
            <option value="0">
              <span class="text-secondary">전체</span>
            </option>
            <option v-for="bank in banks" :key="bank.id" :value="bank.id">
              {{ bank.name }}
            </option>
          </select>
          <button class="btn btn-secondary ms-2" type="submit">지도 검색</button>
        </form>
        <div></div>
      </div>
      <div class="d-flex flex-row-reverse justify-content-end">
        <button
          class="btn btn-outline-secondary ms-2 mt-3 me-0"
          v-for="searchHistory in searchHistoryList"
          :key="searchHistory.id"
          @click="setSearchKeyWord(searchHistory)"
        >
          {{ searchHistory.searchKeyWord }}
          <button class="btn-close" @click.stop="deleteSearchKeyWord(searchHistory)"></button>
        </button>
      </div>
    </div>
    <!-- 지도 그림 및 목록을 출력할 태그 -->
    <MapList />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useMapStore } from '@/stores/map'
import MapList from '@/components/Maps/MapList.vue'

const userStore = useUserStore()
const mapStore = useMapStore()
// 사용자 주소를 받아옴
const userAddress = ref(null)
// const userAddress = ref(userStore?.userInfo.address)

// 검색 키워드 관련 반응형 변수
const searchKeyWordInput = ref(null)
const searchKeyWord = ref('은행')

// 은행 목록 저장
let i = 1
const banks = [
  { id: i++, name: '우리은행', keyword: '우리' },
  { id: i++, name: '한국스탠다드차타드은행', keyword: '제일' },
  { id: i++, name: '대구은행', keyword: '대구' },
  { id: i++, name: '부산은행', keyword: '부산' },
  { id: i++, name: '광주은행', keyword: '광주' },
  { id: i++, name: '제주은행', keyword: '제주' },
  { id: i++, name: '전북은행', keyword: '전북' },
  { id: i++, name: '경남은행', keyword: '경남' },
  { id: i++, name: '중소기업은행', keyword: '기업' },
  { id: i++, name: '한국산업은행', keyword: '산업' },
  { id: i++, name: '국민은행', keyword: '국민' },
  { id: i++, name: '신한은행', keyword: '신한' },
  { id: i++, name: '농협은행주식회사', keyword: '농협' },
  { id: i++, name: '하나은행', keyword: '하나' },
  { id: i++, name: '주식회사 케이뱅크', keyword: '케이뱅크' },
  { id: i++, name: '수협은행', keyword: '수협' },
  { id: i++, name: '주식회사 카카오뱅크', keyword: '카카오' },
  { id: i++, name: '토스뱅크 주식회사', keyword: '토스' },
]

// 저장한 은행
const selectBankTag = ref(null)

// 은행 select 변경시
const selectBank = function () {
  mapStore.selectedBank = selectBankTag.value.value
}

// 검색 히스토리 관련
let searchHistoryId = 0
const searchHistoryList = ref([])

// 검색어 입력시 및 지도 검색시 검색어를 중복 검사 후 목록에 추가
// 목록 중복과 관계 없이 반드시 검색어는 변경시켜줌
const updateMapSearchKeyWord = function () {
  // 입력 필드가 비어있는지 확인
  if (!searchKeyWordInput.value) {
    alert('검색 주소를 입력해주세요.')
    return
  }

  // 중복 검색어 체크
  const isDuplicate = searchHistoryList.value.some((item) => item.searchKeyWord === searchKeyWordInput.value)

  if (!isDuplicate && searchKeyWordInput.value) {
    // 목록에 추가
    console.log(searchKeyWordInput.value)
    searchHistoryList.value.push({
      id: searchHistoryId++,
      searchKeyWord: searchKeyWordInput.value,
    })
    console.log(`${searchKeyWordInput.value} - 검색어 추가`)
  } else {
    // 검색어 순서를 변경시켜주기 위해 인덱스를 찾고
    // 삭제 후 재등록해줌
    const index = searchHistoryList.value.findIndex((item) => item.searchKeyWord === searchKeyWordInput.value)

    if (index !== -1) {
      // 인덱스 조회 완료시 기존 항목 삭제
      searchHistoryList.value.splice(index, 1)
    }
    searchHistoryList.value.push({
      id: searchHistoryId++,
      searchKeyWord: searchKeyWordInput.value,
    })
  }
  // 완료 동작 출력 - 조건문과 관계 없이 현재 검색어는 바꿔줌

  searchKeyWord.value = `${searchKeyWordInput.value} 은행`
  mapStore.updateSearchKeyWord(searchKeyWordInput.value)
  console.log('검색어 - ', searchKeyWord.value)
  searchKeyWordInput.value = ''
}

// 버튼 검색어 목록에서 선택한 검색어를 삭제
const deleteSearchKeyWord = function (searchHistoryItem) {
  const index = searchHistoryList.value.findIndex((item) => item.id === searchHistoryItem.id)

  console.log(`${searchHistoryItem.searchKeyWord} - 검색어 삭제`)
  if (index !== -1) {
    searchHistoryList.value.splice(index, 1)
  }
}

// 버튼 검색어 목록에서 선택한 검색어를 검색
const setSearchKeyWord = function (searchHistoryItem) {
  searchKeyWordInput.value = searchHistoryItem.searchKeyWord
  updateMapSearchKeyWord()
}

onMounted(() => {
  if (userStore.userInfo) {
    userAddress.value = userStore.userInfo.address
  } else {
    searchKeyWordInput.value = null
  }

  searchKeyWordInput.value = userAddress.value
})

onUnmounted(() => {
  mapStore.selectedBank = ''
})
</script>

<style scoped>
.map-search-box {
  width: 1000px;
  min-height: 125px;
}
</style>
