<template>
  <div>
    <h3>
      적금 희망 기간 :
      {{ savingPeriod ? savingPeriod + "개월" : "희망 기간을 입력해주세요." }}
    </h3>
    <label for="term">희망 기간 선택 : </label>
    <select id="term" v-model="savingPeriod">
      <option value="1">1개월</option>
      <option value="3">3개월</option>
      <option value="6">6개월</option>
      <option value="12">12개월</option>
      <option value="24">24개월</option>
      <option value="36">36개월</option>
    </select>

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
          v-for="(saving, index) in user?.join_saving"
          :key="index"
          class="row"
        >
          <div class="col-2 border">{{ saving.fin_prdt_nm }}</div>
          <div class="col-2 border">{{ saving.kor_co_nm }}</div>
          <div class="col-2 border">
            {{
              saving.max_limit
                ? formatNumber(saving.max_limit) + " 원"
                : "최고 한도 없음"
            }}
          </div>
          <div :class="['col-2 border', getRateClass(saving, 'intr_rate')]">
            {{ getInterestRate(saving, "intr_rate") }}
          </div>
          <div :class="['col-2 border', getRateClass(saving, 'intr_rate2')]">
            {{ getInterestRate(saving, "intr_rate2") }}
          </div>
          <div class="col-2 border">
            {{ getInterestRate(saving, "intr_rate_type_nm") }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const user = ref(null);
const store = useUserStore();
const savingPeriod = ref(null);

onMounted(() => {
  store.getUserInfo();
  user.value = store.userInfo;
  savingPeriod.value = user.value.saving_period;
});

const formatNumber = (value) => {
  if (typeof value !== "number") return "최고 한도 없음";
  return new Intl.NumberFormat().format(value);
};

const getInterestRate = (saving, field) => {
  const option = saving.savingoption_set.find(
    (option) => option.save_trm == savingPeriod.value
  );
  return option ? option[field] : "";
};

const getRateClass = (saving, field) => {
  const rates = user.value.join_saving
    .map((d) => {
      const option = d.savingoption_set.find(
        (option) => option.save_trm == savingPeriod.value
      );
      return option ? parseFloat(option[field]) : null;
    })
    .filter((rate) => rate !== null && !isNaN(rate));

  if (rates.length === 0) return "";

  const maxRate = Math.max(...rates);
  const minRate = Math.min(...rates);
  const rate = parseFloat(getInterestRate(saving, field));

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
  display: flex;
  justify-content: center;
  align-items: center;
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
