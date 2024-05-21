<template>
  <div>
    <div class="my-container mt-4">
      <div class="row mb-3">
        <div class="col-md-7 border mx-1 p-3 col-container">
          <ComparedProducts />
        </div>
        <div class="col-md-4 border mx-1 p-3 col-container">
          <CreditScore />
        </div>
      </div>
      <div class="row">
        <div class="col-md-7 border mx-1 p-3 col-container">
          <JoinProducts />
        </div>
        <div class="col-md-4 border mx-1 p-3 col-container">
          <RecommendProducts />
        </div>
      </div>
    </div>
    <button @click="logOut" class="btn btn-primary mx-1">로그아웃</button>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import ComparedProducts from "@/components/MyAccount/ComparedProducts.vue";
import CreditScore from "@/components/MyAccount/CreditScore.vue";
import JoinProducts from "@/components/MyAccount/JoinProducts.vue";
import RecommendProducts from "@/components/MyAccount/RecommendProducts.vue";

const store = useUserStore();
const logOut = function () {
  store.logOut();
};
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
