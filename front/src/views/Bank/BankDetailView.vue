<template>
  <div class="container mt-4">
    <div v-if="bank" class="bank-card shadow-lg rounded">
      <div class="bank-card-header">
        <h4 class="bank-title">{{ bank.kor_co_nm }}</h4>
        <a :href="bank.homp_url" class="bank-link">
          {{ bank.kor_co_nm }} 홈페이지로 이동
        </a>
      </div>
      <div class="bank-card-body">
        <p><strong>대표 번호:</strong> {{ bank.cal_tel }}</p>
        <p><strong>담당자:</strong> {{ bank.dcls_chrg_man }}</p>
        <div class="product-section">
          <h5>예금 상품</h5>
          <ul class="product-list">
            <li
              v-for="deposit in bank.depositproduct_set"
              :key="deposit.id"
              class="product-item"
            >
              <RouterLink
                :to="{
                  name: 'products-detail',
                  params: { id: deposit.id, type: 'deposit' },
                }"
                class="product-link"
              >
                {{ deposit.fin_prdt_nm }}
              </RouterLink>
            </li>
          </ul>
        </div>
        <div class="product-section">
          <h5>적금 상품</h5>
          <ul class="product-list">
            <li
              v-for="saving in bank.savingproduct_set"
              :key="saving.id"
              class="product-item"
            >
              <RouterLink
                :to="{
                  name: 'products-detail',
                  params: { id: saving.id, type: 'saving' },
                }"
                class="product-link"
              >
                {{ saving.fin_prdt_nm }}
              </RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <p v-else class="text-muted">은행 정보가 없습니다.</p>
  </div>
</template>

<script setup>
import { RouterLink, useRoute } from "vue-router";
import { onMounted, ref } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";

const route = useRoute();
const store = useUserStore();
const bankId = ref(null);
const bank = ref(null);

const fetchBank = () => {
  axios
    .get(`${store.API_URL}/finances/get_bank/${bankId.value}/`)
    .then((response) => {
      bank.value = response.data;
    })
    .catch((err) => {
      console.log(err);
    });
};

onMounted(() => {
  bankId.value = route.params.id;
  fetchBank();
});
</script>

<style scoped>
.bank-card {
  border: 1px solid #e2e2e2;
  border-radius: 0.75rem;
  background-color: #ffffff;
  overflow: hidden;
}

.bank-card-header {
  background-color: #f8f9fa;
  padding: 1rem;
  border-bottom: 1px solid #e2e2e2;
}

.bank-title {
  font-size: 1.75rem;
  font-weight: bold;
  margin: 0;
}

.bank-link {
  display: inline-block;
  margin-top: 0.5rem;
  color: #007bff;
  text-decoration: none;
}

.bank-link:hover {
  text-decoration: underline;
}

.bank-card-body {
  padding: 1.5rem;
}

.product-section {
  margin-top: 2rem;
}

.product-list {
  list-style: none;
  padding: 0;
}

.product-item {
  padding: 0.75rem 1.25rem;
  background-color: #f8f9fa;
  margin-bottom: 0.5rem;
  border-radius: 0.5rem;
}

.product-item:hover {
  background-color: #e9ecef;
}

.product-link {
  color: #343a40;
  text-decoration: none;
  font-weight: 500;
}

.product-link:hover {
  text-decoration: underline;
}

.text-muted {
  color: #6c757d;
}
</style>
