<template>
  <div>
    <h1 class="text-center mb-4">LoginView</h1>
    <form @submit.prevent="logIn" class="mx-auto" style="max-width: 400px">
      <div class="form-group">
        <label for="username">ID:</label>
        <input
          type="text"
          v-model.trim="username"
          id="username"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input
          type="password"
          v-model.trim="password"
          id="password"
          class="form-control"
          required
        />
      </div>
      <button type="submit" class="btn btn-primary btn-block">Login</button>
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
