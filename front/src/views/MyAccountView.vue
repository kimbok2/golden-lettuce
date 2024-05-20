<template>
  <div>
    <h1>MyAccountView</h1>
    <div class="container mt-4">
      <div class="row mb-3">
        <div class="col-md-7 border mx-1 p-3">
          <ComparedProducts />
        </div>
        <div class="col-md-4 border mx-1 p-3">
          <CreditScore />
        </div>
      </div>
      <div class="row">
        <div class="col-md-7 border mx-1 p-3">
          <JoinProducts />
        </div>
        <div class="col-md-4 border mx-1 p-3">
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

<style scoped></style>
