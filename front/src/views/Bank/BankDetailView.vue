<template>
  <div class="container mt-4">
    <div v-if="bank" class="bank-card shadow-lg rounded">
      <div class="bank-card-header">
        <h4 class="bank-title d-flex align-items-center justify-content-center">
          <img :src="`/media/bank/${bank.id}.png`" alt="" />
          <span class="mx-2">{{ bank.kor_co_nm }}</span>
          <a :href="bank.homp_url" class="bank-link m-0">
            <span class="material-symbols-outlined"> home </span>
          </a>
        </h4>
      </div>
      <div class="bank-card-body">
        <div class="row mb-3">
          <div class="col-3"><strong>대표 번호</strong></div>
          <div class="col-9">{{ formattedPhoneNumber(bank.cal_tel) }}</div>
        </div>
        <hr />
        <div class="row mb-3">
          <div class="col-3"><strong>담당자</strong></div>
          <div class="col-9">{{ bank.dcls_chrg_man }}</div>
        </div>
        <hr />
        <h4>
          <b>{{ bank.kor_co_nm }}이 보유한 금융 상품을 소개합니다!</b>
        </h4>
        <hr />
        <div class="row">
          <div class="col-6">
            <div class="product-section">
              <h5>
                <b>예금 상품 {{ bank.depositproduct_set.length }}개</b>
              </h5>
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
          </div>
          <div class="col-6">
            <div class="product-section">
              <h5>
                <b> 적금 상품 {{ bank.savingproduct_set.length }}개</b>
              </h5>
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

const formattedPhoneNumber = (phone) => {
  if (!phone) return "";
  return phone.replace(/(\d{4})(\d{4})/, "$1-$2");
};

onMounted(() => {
  bankId.value = route.params.id;
  fetchBank();
});
</script>

<style scoped>
.bank-container {
  max-width: 1000px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
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
