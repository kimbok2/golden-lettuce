<template>
  <div>
    <h1>ProductListView</h1>
    <hr />

    <div class="container">
      <h3>제품 검색 조건 바</h3>
      <form @submit.prevent="selectSort">
        <span>상품 종류 : </span>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="radio"
            id="deposit"
            name="fruit"
            value="deposit"
            v-model="selectedType"
          />
          <label class="form-check-label" for="deposit"> 예금 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="radio"
            id="saving"
            name="fruit"
            value="saving"
            v-model="selectedType"
          />
          <label class="form-check-label" for="saving">적금</label>
        </div>
        <br /><br />

        <button type="submit" class="btn btn-primary">제출</button>
      </form>
    </div>
    <hr />
    <div>
      <ul class="text-start ps-0">
        <li class="card rounded-0">
          <div class="row m-0">
            <div class="col-1">상품번호</div>
            <div class="col-5">상품명</div>
            <div class="col-3">담당 은행</div>
            <div class="col-1">가입 방법</div>
            <div class="col-2">공시기준월</div>
          </div>
        </li>
        <div v-if="products">
          <div v-for="product in products">
            <li class="card border border-0 border-bottom rounded-0">
              <div class="row m-0">
                <div class="col-1">{{ product.id }}</div>
                <div class="col-5">
                  {{ product.fin_prdt_nm }}
                </div>
                <div class="col-3">{{ product.kor_co_nm }}</div>
                <div class="col-1">{{ product.join_deny }}</div>
                <div class="col-2 text-center">{{ product.dcls_month }}</div>
              </div>
            </li>
          </div>
        </div>
      </ul>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const store = useUserStore();
const router = useRouter();
const products = ref(null);
const selectedType = ref(null);
// 옵션 선택 시 해당 옵션을 토대로 예.적금 리스트를 반환하는 함수
const selectSort = function () {
  if (selectedType.value) {
    axios({
      method: "get",
      url: `${store.API_URL}/finances/get_${selectedType.value}_all/`,
      // headers: {
      //   Authorization: `Token ${store.token}`,
      // },
    })
      .then((response) => {
        products.value = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  }
};
</script>

<style scoped></style>
