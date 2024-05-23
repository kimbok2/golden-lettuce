<template>
  <div class="password-change-container">
    <form @submit.prevent="updatePassword">
      <div class="form-group row align-items-center mb-3">
        <label
          for="newPassword1"
          class="col-sm-4 col-form-label text-right font-weight-bold"
        >
          새 비밀번호
        </label>
        <div class="col-sm-1 d-flex justify-content-center">
          <div
            class="border-right"
            style="height: 2rem; border-color: red"
          ></div>
        </div>
        <div class="col-sm-7">
          <input
            type="password"
            v-model.trim="newPassword1"
            id="newPassword1"
            class="form-control"
          />
        </div>
      </div>
      <div class="form-group row align-items-center mb-3">
        <label
          for="newPassword2"
          class="col-sm-4 col-form-label text-right font-weight-bold"
        >
          새 비밀번호 확인
        </label>
        <div class="col-sm-1 d-flex justify-content-center">
          <div
            class="border-right"
            style="height: 2rem; border-color: red"
          ></div>
        </div>
        <div class="col-sm-7">
          <input
            type="password"
            v-model.trim="newPassword2"
            id="newPassword2"
            class="form-control"
          />
        </div>
      </div>
      <div class="d-flex justify-content-center mt-3">
        <button type="submit" class="btn btn-primary mx-1">
          비밀번호 변경
        </button>
      </div>
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
      console.log(err.response.data.new_password2);
      alert(`${err.response.data.new_password2[0]}`);
    });
};
</script>

<style scoped>
.password-change-container {
  margin: auto;
  max-width: 600px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
.form-group {
  margin-bottom: 15px;
}
label {
  font-weight: bold;
}
input {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}
button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
</style>
