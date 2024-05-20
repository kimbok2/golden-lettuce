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
import { ref, watch, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import { useRoute } from "vue-router";

const user = ref(null);
const store = useUserStore();
const route = useRoute();
const depositPeriod = ref(null);

const fetchUserInfo = async () => {
  await store.getUserInfo();
  user.value = store.userInfo;
  depositPeriod.value = user.value.deposit_period;
};

onMounted(async () => {
  await fetchUserInfo();
});

watch(
  () => route.path,
  async () => {
    await fetchUserInfo();
  }
);

const formatNumber = (value) => {
  if (typeof value !== "number") return "최고 한도 없음";
  return new Intl.NumberFormat().format(value);
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
