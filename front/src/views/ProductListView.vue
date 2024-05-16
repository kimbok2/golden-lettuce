<template>
  <div>
    <h1>ProductListView</h1>
    <div>
      <h3>제품 검색 바</h3>
    </div>
    <hr />
    <div v-if="products">
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
      </ul>
    </div>
    <p v-else>오오류</p>
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

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/finances/get_deposit_all/`,
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
});
</script>

<style scoped></style>
