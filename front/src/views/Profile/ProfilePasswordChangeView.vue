<template>
  <div>
    <h1>ProfilePasswordChangeView</h1>

    <form @submit.prevent="updatePassword">
      <div>
        <label for="newPassword1"> 새 비밀번호 : </label>
        <input type="password" v-model.trim="newPassword1" id="newPassword1" />
      </div>
      <div>
        <label for="newPassword2"> 새 비밀번호 확인 : </label>
        <input type="password" v-model.trim="newPassword2" id="newPassword2" />
      </div>

      <button type="submit" class="btn btn-primary mx-1">비밀번호 변경</button>
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const newPassword1 = ref(null);
const newPassword2 = ref(null);
const store = useUserStore();
const user = ref(null);
const router = useRouter();
const updatePassword = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/accounts/password/change/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      new_password1: newPassword1.value,
      new_password2: newPassword2.value,
    },
  })
    .then((response) => {
      console.log("비밀번호 변경 성공");
      router.push({ name: "profile" });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style>
