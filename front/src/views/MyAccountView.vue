<template>
  <div>
    <h1 class="main-h1-container">
      <span>나의 정보</span>
      <span class="material-symbols-outlined"> inventory </span>
    </h1>
    <div class="my-container mt-4">
      <div class="row mb-3 d-flex justify-content-center">
        <div class="col-md-7 border mx-1 p-3 col-container">
          <ComparedProducts />
        </div>
        <div class="col-md-4 border mx-1 p-3 col-container">
          <CreditScore />
        </div>
      </div>
      <div class="row mb-3 d-flex justify-content-center">
        <div class="col-md-6 border mx-1 p-3 col-container">
          <JoinProducts />
        </div>
        <div class="col-md-5 border mx-1 p-3 col-container">
          <RecommendProducts />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import ComparedProducts from "@/components/MyAccount/ComparedProducts.vue";
import CreditScore from "@/components/MyAccount/CreditScore.vue";
import JoinProducts from "@/components/MyAccount/JoinProducts.vue";
import RecommendProducts from "@/components/MyAccount/RecommendProducts.vue";

const store = useUserStore();
</script>

<style scoped>
.my-container {
  max-width: 1000px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
.col-container {
  border-radius: 10px;
}
</style>
