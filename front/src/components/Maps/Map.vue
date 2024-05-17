<template>
  <div class="text-start">
    <!-- 지도 검색창 -->
    <div class="map-search-box p-2">
      <form class="d-flex" @submit.prevent="updateMapSearchKeyWord">
        <input
          class="form-control inline-block"
          style="width: 400px"
          type="text"
          v-model="searchKeyWordInput"
          placeholder="주소를 입력해주세요."
        />
        <button class="btn btn-secondary ms-2" type="submit">지도 검색</button>
        {{ userAddress }}
      </form>
      <div class="d-flex flex-row-reverse justify-content-end">
        <button
          class="btn btn-outline-secondary m-2 me-0"
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
    <MapList/>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import MapList from '@/components/Maps/MapList.vue'

const userStore = useUserStore()
// 사용자 주소를 받아옴
const userAddress = userStore.userInfo.address

// 검색 키워드 관련 반응형 변수
const searchKeyWordInput = ref(null)
const searchKeyWord = ref('은행')

// 검색 히스토리 관련
let searchHistoryId = 0
const searchHistoryList = ref([])

// 검색어 입력시 및 지도 검색시 검색어를 중복 검사 후
const updateMapSearchKeyWord = function () {
  // 중복 검색어 체크
  const isDuplicate = searchHistoryList.value.some((item) => item.searchKeyWord === searchKeyWordInput.value)

  if (!isDuplicate && searchKeyWordInput.value) {
    // 목록에 추가
    searchHistoryList.value.push({
      id: searchHistoryId++,
      searchKeyWord: searchKeyWordInput.value,
    })
    console.log(`${searchKeyWordInput.value} - 검색어 추가`)
  }
  // 완료 동작 출력 - 조건문과 관계 없이 현재 검색어는 바꿔줌
  searchKeyWord.value = `${searchKeyWordInput.value} 은행`
  // searchKeyWordInput.value = ''
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
}

onMounted(() => {
  searchKeyWordInput.value = userAddress
})
</script>

<style scoped>
.map-search-box {
  width: 1000px;
  height: 100px;

  border: 1px solid #dee2e6;
}
</style>
