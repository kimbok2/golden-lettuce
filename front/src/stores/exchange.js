import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeStore = defineStore(
  'exchange',
  () => {
    const API_URL = 'http://127.0.0.1:8000'
    const currencies = [
      {
        pk: 1,
        cur_unit: 'AED',
        cur_nm: '아랍에미리트 디르함',
      },
      {
        pk: 2,
        cur_unit: 'AUD',
        cur_nm: '호주 달러',
      },
      {
        pk: 3,
        cur_unit: 'BHD',
        cur_nm: '바레인 디나르',
      },
      {
        pk: 4,
        cur_unit: 'BND',
        cur_nm: '브루나이 달러',
      },
      {
        pk: 5,
        cur_unit: 'CAD',
        cur_nm: '캐나다 달러',
      },
      {
        pk: 6,
        cur_unit: 'CHF',
        cur_nm: '스위스 프랑',
      },
      {
        pk: 7,
        cur_unit: 'CNH',
        cur_nm: '위안화',
      },
      {
        pk: 8,
        cur_unit: 'DKK',
        cur_nm: '덴마아크 크로네',
      },
      {
        pk: 9,
        cur_unit: 'EUR',
        cur_nm: '유로',
      },
      {
        pk: 10,
        cur_unit: 'GBP',
        cur_nm: '영국 파운드',
      },
      {
        pk: 11,
        cur_unit: 'HKD',
        cur_nm: '홍콩 달러',
      },
      {
        pk: 12,
        cur_unit: 'IDR(100)',
        cur_nm: '인도네시아 루피아',
      },
      {
        pk: 13,
        cur_unit: 'JPY(100)',
        cur_nm: '일본 옌',
      },
      {
        pk: 14,
        cur_unit: 'KRW',
        cur_nm: '한국 원',
      },
      {
        pk: 15,
        cur_unit: 'KWD',
        cur_nm: '쿠웨이트 디나르',
      },
      {
        pk: 16,
        cur_unit: 'MYR',
        cur_nm: '말레이지아 링기트',
      },
      {
        pk: 17,
        cur_unit: 'NOK',
        cur_nm: '노르웨이 크로네',
      },
      {
        pk: 18,
        cur_unit: 'NZD',
        cur_nm: '뉴질랜드 달러',
      },
      {
        pk: 19,
        cur_unit: 'SAR',
        cur_nm: '사우디 리얄',
      },
      {
        pk: 20,
        cur_unit: 'SEK',
        cur_nm: '스웨덴 크로나',
      },
      {
        pk: 21,
        cur_unit: 'SGD',
        cur_nm: '싱가포르 달러',
      },
      {
        pk: 22,
        cur_unit: 'THB',
        cur_nm: '태국 바트',
      },
      {
        pk: 23,
        cur_unit: 'USD',
        cur_nm: '미국 달러',
      },
    ]

    const exchangeRates = ref([])

    const inputAmount = ref(null)

    const selectedCurrent = ref(14)
    const selectedHandle = ref(0)

    const selectedRate = computed(() => {
      const index = exchangeRates.value.findIndex((rate) => rate.current_id === selectedCurrent.value)
      if (index !== -1) {

        return exchangeRates.value[index]['latest_exchange_deal_bas_r']
      } else {
        return 0
      }
    })

    // DB에서 각 통화별로 마지막으로 저장된 환율을 받아옴
    const get_exchange_rate = function () {
      axios({
        method: 'get',
        url: `${API_URL}/exchanges/get_current_info`,
      })
        .then((response) => {
          exchangeRates.value = response.data
          console.log(exchangeRates.value)
        })
        .catch((error) => {
          console.log(error)
        })
    }

    return { currencies, inputAmount, selectedCurrent, selectedRate, exchangeRates, selectedHandle, get_exchange_rate }
  },
  { persist: true }
)
