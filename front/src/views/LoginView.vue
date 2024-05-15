<template>
  <div>
    <h1 class="text-center mb-4">LoginView</h1>
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
      <button type="submit" class="btn btn-primary btn-block mt-3">
        Login
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";

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
</script>

<style scoped></style>
