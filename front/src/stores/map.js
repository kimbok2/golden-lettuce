import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMapStore = defineStore('map', () => {
  const searchKeyWord = ref('')


  const updateSearchKeyWord = function (newKeyWord) {
    searchKeyWord.value = newKeyWord
    console.log('mapStore : searchKeyWord 변경 완료')
  }

  return { searchKeyWord, updateSearchKeyWord }
}, {persist: true})