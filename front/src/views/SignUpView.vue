<template>
  <div>
    <h1>SignUpView</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username"> ID : </label>
        <input type="text" v-model.trim="username" id="username" />
      </div>
      <div>
        <label for="password1"> 비밀번호 : </label>
        <input type="password" v-model.trim="password1" id="password1" />
      </div>
      <div>
        <label for="password2"> 비밀번호 확인 : </label>
        <input type="password" v-model.trim="password2" id="password2" />
      </div>
      <input type="submit" value="가입" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const store = useUserStore();

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
};
</script>

<style scoped></style>
