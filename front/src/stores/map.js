import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'

export const useMapStore = defineStore(
  'map',
  () => {
    const searchKeyWord = ref('')

    // 선택된 은행 번호
    const selectedBank = ref('')
    // 선택된 은행 이름
    const selectedBankName = ref('')

    // 은행 번호, DB id와 동일
    let i = 1;

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

    // 선택 은행 번호가 변경되면, 선택
    watch(
      (selectedBank.value,
      (newBankNumber) => {
        if (selectedBank.value > 0) {
          selectedBankName.value = banks.find((b) => b.id == selectedBank.value)['keyword']
          console.log(selectedBankName.value)
        } else {
          selectedBankName.value = ''
        }
      })
    )

    const updateSearchKeyWord = function (newKeyWord) {
      searchKeyWord.value = newKeyWord
      console.log('mapStore : searchKeyWord 변경 완료')
    }

    return { searchKeyWord, selectedBank, selectedBankName, updateSearchKeyWord }
  },
  { persist: true }
)
