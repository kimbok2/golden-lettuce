import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBankStore = defineStore(
  'bank',
  () => {
    const banks = ref([])
    const API_URL = 'http://127.0.0.1:8000'

    const bankDataFetched = ref(false)

    const fetchBankDatas = () => {
      if (bankDataFetched.value === false) {
        banks.value = []

        for (let i = 1; i < 19; i++) {
          axios
            .get(`${API_URL}/finances/get_bank_map/${i}/`)
            .then((response) => {
              banks.value.push(response.data)
            })
            .then((response) => {
              if (i == 18) {
                bankDataFetched.value = true
                console.log(bankDataFetched.value)
              }
            })
            .catch((err) => {
              console.log(err)
            })
        }

        console.log('bankStore', banks.value)
      }
    }
    return { banks, bankDataFetched, fetchBankDatas }
  },
  { persist: true }
)
