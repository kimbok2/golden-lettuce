<template>
  <div>
    <h1 class="main-h1-container">
      <span>상품 비교</span>
      <span class="material-symbols-outlined"> balance </span>
    </h1>
    <div class="compare-container mt-4">
      <ul class="nav nav-tabs">
        <li class="nav-item">
          <RouterLink class="nav-link" :class="{ active: $route.name === 'compare' }" :to="{ name: 'compare' }">
            예금 비교
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink
            class="nav-link"
            :class="{ active: $route.name === 'compare-saving' }"
            :to="{ name: 'compare-saving' }"
          >
            적금 비교
          </RouterLink>
        </li>
      </ul>
      <div class="tab-content mt-3">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'

const user = ref(null)
const store = useUserStore()
const route = useRoute()
const depositPeriod = ref(null)

const fetchUserInfo = async () => {
  await store.getUserInfo()
  user.value = store.userInfo
  depositPeriod.value = user.value.deposit_period
}

onMounted(async () => {
  await fetchUserInfo()
})

watch(
  () => route.path,
  async () => {
    await fetchUserInfo()
  }
)

const formatNumber = (value) => {
  if (typeof value !== 'number') return '최고 한도 없음'
  return new Intl.NumberFormat().format(value)
}
</script>

<style scoped>
.compare-container {
  max-width: 1000px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
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
  font-weight: bolder;
}
</style>
