<template>
  <div>
    <h1>상품 추천</h1>
    <button @click="Recommend" class="btn btn-primary">상품 추천 받기</button>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, computed, watch } from "vue";
import { useUserStore } from "@/stores/user";

const store = useUserStore();
const recomDeposits = ref([]);
const recomSavings = ref([]);

const Recommend = function () {
  axios({
    method: "get",
    url: `${store.API_URL}/finances/recommend_deposit1/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      recomDeposits.value = response.data;
      alert("추천 성공");
    })
    .catch((err) => {
      console.log(err);
      alert("추천 실패. 잠시 후 다시 시도해 주세요.");
    });
};
</script>

<style scoped></style>
