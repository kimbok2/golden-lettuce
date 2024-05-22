<template>
  <div>
    <h1 class="main-h1-container">
      <span>상품 비교</span>
      <span class="material-symbols-outlined"> balance </span>
    </h1>
    <div class="compare-container mt-4">
      <div
        class="d-flex justify-content-center mb-0 w-100 bg-white tab-container"
        role="tablist"
      >
        <div class="flex-fill text-center" role="presentation">
          <RouterLink
            class="w-100 btn tab-button"
            :class="{ active: $route.name === 'compare' }"
            :to="{ name: 'compare' }"
            id="deposit-tab"
            type="button"
            role="tab"
            aria-controls="deposit-tab-pane"
            :aria-selected="$route.name === 'compare'"
          >
            예금 비교
          </RouterLink>
        </div>
        <div class="flex-fill text-center" role="presentation">
          <RouterLink
            class="w-100 btn tab-button"
            :class="{ active: $route.name === 'compare-saving' }"
            :to="{ name: 'compare-saving' }"
            id="saving-tab"
            type="button"
            role="tab"
            aria-controls="saving-tab-pane"
            :aria-selected="$route.name === 'compare-saving'"
          >
            적금 비교
          </RouterLink>
        </div>
      </div>
      <div class="tab-content mt-3">
        <RouterView />
      </div>
    </div>
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
</script>

<style scoped>
.tab-container {
  border-bottom: 1px solid #dee2e6;
}

.tab-button {
  border: 1px solid transparent;
  border-top-left-radius: 0.25rem;
  border-top-right-radius: 0.25rem;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
  margin-bottom: -1px;
  color: #868f08; /* 클릭되지 않은 탭의 글씨 색 파랑 */
  background-color: #fff; /* 탭 배경 흰색 */
  border-bottom: 1px solid #dee2e6; /* 클릭되지 않은 탭의 아래쪽 보더 */
  text-decoration: none;
  display: inline-block;
  padding: 0.5rem 1rem;
  text-align: center;
}

.tab-button.active {
  color: #000; /* 클릭된 탭의 글씨 색 검정 */
  background-color: #fff;
  border-color: #dee2e6 #dee2e6 #fff;
  border-bottom-color: transparent; /* 클릭된 탭의 아래쪽 보더 투명 */
}

.tab-button:hover {
  color: #939c1888; /* 호버 시 글씨 색 파랑 */
  text-decoration: none;
}
</style>
