<template>
  <div class="credit-score-container">
    <h2 class="text-center mb-4">내 신용 점수</h2>
    <div class="text-center mb-3">
      <DoughnutChart :score="userInfo.credit_score" />
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useUserStore } from "@/stores/user";
import DoughnutChart from "@/components/MyAccount/DoughnutChart.vue";

const store = useUserStore();
const userInfo = computed(() => store.userInfo);
</script>

<style scoped>
.credit-score-container {
  max-width: 200px;
  margin: auto;
}

.text-center {
  text-align: center;
}
</style>
