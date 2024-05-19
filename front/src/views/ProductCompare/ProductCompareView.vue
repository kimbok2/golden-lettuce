<template>
  <div>
    <h1>ProductCompareView</h1>
    <RouterLink :to="{ name: 'compare' }">예금 비교</RouterLink> |
    <RouterLink :to="{ name: 'compare-saving' }">적금 비교</RouterLink>
    <hr />
    <RouterView />
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
const depositPeriod = ref(null);
const savingPeriod = ref(null);

onMounted(() => {
  store.getUserInfo();
  user.value = store.userInfo;
  depositPeriod.value = user.value.deposit_period;
});

const goProfile = function () {
  router.push({ name: "profile" });
};

const formatNumber = (value) => {
  if (typeof value !== "number") return "최고 한도 없음";
  return new Intl.NumberFormat().format(value);
};
const getInterestRate = (deposit, field) => {
  const option = deposit.depositoption_set.find(
    (option) => option.save_trm == depositPeriod.value
  );
  return option ? option[field] : "";
};

const getRateClass = (deposit, field) => {
  const rates = user.value.join_deposit
    .map((d) => {
      const option = d.depositoption_set.find(
        (option) => option.save_trm == depositPeriod.value
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
