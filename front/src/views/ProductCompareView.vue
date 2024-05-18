<template>
  <div>
    <h1>ProductCompareView</h1>
    <div>
      <div class="container">
        <div class="row mb-3 border bg-light">
          <div class="col-3 font-weight-bold border py-2">Product Name</div>
          <div class="col-3 font-weight-bold border py-2">Join Deny</div>
          <div class="col-3 font-weight-bold border py-2">Company Name</div>
          <div class="col-3 font-weight-bold border py-2">
            Comparison Result
          </div>
        </div>
        <div
          v-for="(deposit, index) in user.join_deposit"
          :key="index"
          class="row mb-3"
        >
          <div class="col-3 border py-2">{{ deposit.fin_prdt_nm }}</div>
          <div class="col-3 border py-2">{{ deposit.join_deny }}</div>
          <div class="col-3 border py-2">{{ deposit.kor_co_nm }}</div>
          <div class="col-3 border py-2">
            {{ compareFields(deposit) ? "Match" : "No Match" }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref, watch } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const user = ref(null);
const store = useUserStore();

onMounted(() => {
  store.getUserInfo();
  user.value = store.userInfo;
});
const compareFields = (deposit) => {
  // Add your comparison logic here
  // Example: Compare if fin_prdt_nm contains 'Savings' and join_deny is 'No' and kor_co_nm is 'ABC Bank'
  if (
    deposit.fin_prdt_nm.includes("예금") &&
    deposit.join_deny === "No" &&
    deposit.kor_co_nm.includes("Bank")
  ) {
    return true;
  }
  return false;
};
// 필드 정의
const fields = ref(["상품명", "가입 기간", "기본 금리", "우대 금리"]);

// 레코드 데이터
const data = ref([
  {
    상품명: "예금",
    "가입 기간": "3개월",
    "기본 금리": "2.3%",
    "우대 금리": "2.6%",
  },
  {
    상품명: "적금",
    "가입 기간": "6개월",
    "기본 금리": "3.1%",
    "우대 금리": "3.6%",
  },
  {
    상품명: "대출",
    "가입 기간": "12개월",
    "기본 금리": "2.6%",
    "우대 금리": "2.7%",
  },
]);
</script>

<style scoped>
.container {
  margin-top: 60px;
}

.font-weight-bold {
  font-weight: bold;
}

.mb-3 {
  margin-bottom: 1rem;
}

.border {
  border: 1px solid #ccc;
}

.bg-light {
  background-color: #f8f9fa;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}
</style>
