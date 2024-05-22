<template>
  <div class="container mt-4">
    <h3>
      {{
        savingPeriod
          ? "적금 희망 기간 : " + savingPeriod + "개월"
          : "적금 희망 기간을 입력해주세요."
      }}
    </h3>
    <div class="form-group row align-items-center">
      <label for="term" class="col-sm-2 offset-3 col-form-label"
        >희망 기간 선택 :
      </label>
      <div class="col-sm-3">
        <select
          id="term"
          v-model="savingPeriod"
          class="form-select form-select-sm"
        >
          <option disabled value="null">
            <span class="text-secondary">희망기간을 선택하세요</span>
          </option>
          <option value="1">1개월</option>
          <option value="3">3개월</option>
          <option value="6">6개월</option>
          <option value="12">12개월</option>
          <option value="24">24개월</option>
          <option value="36">36개월</option>
        </select>
      </div>
    </div>

    <div>
      <div class="container">
        <div class="row bg-light">
          <div class="col-2 font-weight-bold border-col">상품명</div>
          <div class="col-2 font-weight-bold border-col">담당 은행</div>
          <div class="col-2 font-weight-bold border-col">최고 한도</div>
          <div class="col-2 font-weight-bold border-col">저축 금리</div>
          <div class="col-2 font-weight-bold border-col">최고 우대 금리</div>
          <div class="col-2 font-weight-bold border-col">저축 금리 유형</div>
        </div>

        <div
          v-for="(saving, index) in user?.compare_saving"
          :key="index"
          class="row"
        >
          <div class="col-2 border-col">
            <RouterLink
              :to="{
                name: 'products-detail',
                params: { id: saving.id, type: 'saving' },
              }"
              class="custom-link"
              >{{ saving.fin_prdt_nm }}</RouterLink
            >
          </div>
          <div class="col-2 border-col">
            <RouterLink
              :to="{
                name: 'bank-detail',
                params: { id: saving.bank },
              }"
              class="custom-link"
              >{{ saving.kor_co_nm }}</RouterLink
            >
          </div>
          <div class="col-2 border-col">
            {{
              saving.max_limit
                ? formatNumber(saving.max_limit) + " 원"
                : "최고 한도 없음"
            }}
          </div>
          <div :class="['col-2 border-col', getRateClass(saving, 'intr_rate')]">
            {{
              getInterestRate(saving, "intr_rate")
                ? getInterestRate(saving, "intr_rate")
                : "-"
            }}
          </div>
          <div
            :class="['col-2 border-col', getRateClass(saving, 'intr_rate2')]"
          >
            {{
              getInterestRate(saving, "intr_rate2")
                ? getInterestRate(saving, "intr_rate2")
                : "-"
            }}
          </div>
          <div class="col-2 border-col">
            {{
              getInterestRate(saving, "intr_rate_type_nm")
                ? getInterestRate(saving, "intr_rate_type_nm")
                : "-"
            }}
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
  const rates = user.value.compare_saving
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

.border-col {
  border: 1px solid #1b1b1b;
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
  font-weight: bolder;
}
.custom-link {
  color: inherit; /* 부모 요소의 색상 상속 */
  text-decoration: none; /* 밑줄 제거 */
}
.custom-link:hover {
  color: gray; /* 호버 시 색상 변경 (원하는 색상으로 변경 가능) */
}
</style>
