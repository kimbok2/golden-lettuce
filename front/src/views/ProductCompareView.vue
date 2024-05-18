<template>
  <div>
    <h1>ProductCompareView</h1>
    <h3>
      예금 희망 기간 :
      {{
        user?.deposit_period
          ? user?.deposit_period + "개월"
          : "희망 기간을 입력해주세요."
      }}
    </h3>
    <button @click="goProfile" class="btn btn-primary mx-1">
      입력하러 가기
    </button>
    <p>
      희망 기간 선택 : select만들어 입력 받기, 기본 값은 user_period로 내일 아침
      구현
    </p>
    <div>
      <div class="container">
        <div class="row border bg-light">
          <div class="col-2 font-weight-bold border">상품명</div>
          <div class="col-2 font-weight-bold border">담당 은행</div>
          <div class="col-2 font-weight-bold border">최고 한도</div>
          <div class="col-2 font-weight-bold border">저축 금리</div>
          <div class="col-2 font-weight-bold border">최고 우대 금리</div>
          <div class="col-2 font-weight-bold border">저축 금리 유형</div>
        </div>

        <div
          v-for="(deposit, index) in user?.join_deposit"
          :key="index"
          class="row"
        >
          <div class="col-2 border">{{ deposit.fin_prdt_nm }}</div>
          <div class="col-2 border">{{ deposit.kor_co_nm }}</div>
          <div class="col-2 border">
            {{
              deposit.max_limit
                ? formatNumber(deposit.max_limit) + " 원"
                : "최고 한도 없음"
            }}
          </div>
          <div :class="['col-2 border', getRateClass(deposit, 'intr_rate')]">
            {{ getInterestRate(deposit, "intr_rate") }}
          </div>
          <div :class="['col-2 border', getRateClass(deposit, 'intr_rate')]">
            {{ getInterestRate(deposit, "intr_rate2") }}
          </div>
          <div class="col-2 border">
            {{ getInterestRate(deposit, "intr_rate_type_nm") }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref, watch } from "vue";
import router from "@/router";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const user = ref(null);
const store = useUserStore();
const period = ref(null);

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

const goProfile = function () {
  router.push({ name: "profile" });
};

const formatNumber = (value) => {
  if (typeof value !== "number") return "최고 한도 없음";
  return new Intl.NumberFormat().format(value);
};
const getInterestRate = (deposit, field) => {
  const option = deposit.depositoption_set.find(
    (option) => option.save_trm == user.value.deposit_period
  );
  return option ? option[field] : "";
};

const getRateClass = (deposit, field) => {
  const rates = user.value.join_deposit
    .map((d) => {
      const option = d.depositoption_set.find(
        (option) => option.save_trm == user.value.deposit_period
      );
      return option ? parseFloat(option[field]) : null;
    })
    .filter((rate) => rate !== null);

  const maxRate = Math.max(...rates);
  const minRate = Math.min(...rates);
  const rate = parseFloat(getInterestRate(deposit, field));

  if (rate === maxRate) {
    return "text-success"; // Green for the highest rate
  } else if (rate === minRate) {
    return "text-danger"; // Red for the lowest rate
  } else {
    return "";
  }
};
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

.text-success {
  color: green;
  font-weight: bolder;
}

.text-danger {
  color: red;
}
</style>
