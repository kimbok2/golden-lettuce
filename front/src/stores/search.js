import { defineStore } from "pinia";
import { ref } from "vue";

export const useSearchStore = defineStore("search", () => {
  const selectedType = ref("deposit");
  const selectedPeriods = ref([1, 3, 6, 12, 24, 36]);
  const bankIds = ref([
    "우리은행",
    "한국스탠다드차타드은행",
    "대구은행",
    "부산은행",
    "광주은행",
    "제주은행",
    "전북은행",
    "경남은행",
    "중소기업은행",
    "한국산업은행",
    "국민은행",
    "신한은행",
    "농협은행주식회사",
    "하나은행",
    "주식회사 케이뱅크",
    "수협은행",
    "주식회사 카카오뱅크",
    "토스뱅크 주식회사",
  ]);
  const sorting = ref("intr_rate-");
  const products = ref(null);

  return {
    selectedType,
    selectedPeriods,
    bankIds,
    sorting,
    products,
  };
});
