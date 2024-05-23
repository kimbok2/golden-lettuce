import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBankStore = defineStore(
  'bank',
  () => {
    const banks = ref([])
    const API_URL = 'https://kgarrry.pythonanywhere.com'

    const bankDataFetched = ref(false)


    const fetchBankDatas = () => {
      if (bankDataFetched.value === false) {
        banks.value = []

        return axios
          .get(`${API_URL}/finances/get_bank_map/`)
          .then((response) => {
            banks.value = response.data
          })
          .then((response) => {
            bankDataFetched.value = true
          })
          .catch((err) => {
            console.log(err)
          })
          
      }
    }



    return { banks, bankDataFetched, fetchBankDatas }
  },
  { persist: true }
)
