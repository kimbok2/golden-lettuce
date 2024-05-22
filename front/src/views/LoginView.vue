<template>
  <div>
    <h1 class="main-h1-container">
      <span>로그인</span>
      <span class="material-symbols-outlined"> login </span>
    </h1>
    <div>
      <form @submit.prevent="logIn" class="mx-auto" style="max-width: 400px">
        <div class="form-group row align-items-center mb-3">
          <label
            for="username"
            class="col-sm-4 col-form-label text-right font-weight-bold"
            style="text-align: right"
          >
            ID
          </label>
          <div class="col-sm-1 d-flex justify-content-center">
            <div
              class="border-right"
              style="height: 2rem; border-color: red"
            ></div>
          </div>
          <div class="col-sm-7">
            <input
              type="text"
              v-model.trim="username"
              id="username"
              class="form-control"
              required
            />
          </div>
        </div>
        <div class="form-group row align-items-center mb-3">
          <label
            for="password"
            class="col-sm-4 col-form-label text-right font-weight-bold"
            style="text-align: right"
          >
            비밀번호
          </label>
          <div class="col-sm-1 d-flex justify-content-center">
            <div class="border-right" style="height: 2rem"></div>
          </div>
          <div class="col-sm-7">
            <input
              type="password"
              v-model.trim="password"
              id="password"
              class="form-control"
              required
            />
          </div>
        </div>

        <div class="d-flex justify-content-center mt-3">
          <button type="submit" class="btn btn-primary mx-1">로그인</button>
          <button @click="goSignup" class="btn btn-primary mx-1">
            회원가입
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";
import router from "@/router";

const username = ref(null);
const password = ref(null);
const store = useUserStore();

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};

const goSignup = function () {
  router.push({ name: "signup" });
};
</script>

<style scoped>
.login-container {
  margin: auto;
  max-width: 400px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
</style>
