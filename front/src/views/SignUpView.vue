<template>
  <div>
    <h1 class="text-center mb-4">SignUpView</h1>
    <form @submit.prevent="signUp" class="mx-auto" style="max-width: 600px">
      <div class="form-group row align-items-center mb-3">
        <label
          for="username"
          class="col-sm-4 col-form-label text-right font-weight-bold"
        >
          ID
        </label>
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="text"
            v-model.trim="username"
            id="username"
            class="form-control"
            required
          />
          <div class="invalid-feedback">아이디를 입력해주세요.</div>
        </div>
      </div>
      <div class="form-group row align-items-center mb-3">
        <label
          for="password1"
          class="col-sm-4 col-form-label text-right font-weight-bold"
        >
          비밀번호
        </label>
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="password"
            v-model.trim="password1"
            id="password1"
            class="form-control"
            required
          />
          <div class="invalid-feedback">비밀번호를 입력해주세요.</div>
        </div>
      </div>
      <div class="form-group row align-items-center mb-3">
        <label
          for="password2"
          class="col-sm-4 col-form-label text-right font-weight-bold"
        >
          비밀번호 확인
        </label>
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="password"
            v-model.trim="password2"
            id="password2"
            class="form-control"
            required
          />
          <div class="invalid-feedback">비밀번호를 다시 입력해주세요.</div>
        </div>
      </div>
      <div class="form-group row align-items-center mb-3">
        <label
          for="dateOfBirth"
          class="col-sm-4 col-form-label text-right font-weight-bold"
        >
          생년월일
        </label>
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="date"
            v-model.trim="dateOfBirth"
            id="dateOfBirth"
            class="form-control"
            required
          />
          <div class="invalid-feedback">생년월일을 입력해주세요.</div>
        </div>
      </div>
      <div class="form-group row align-items-center mb-3">
        <label
          for="nickname"
          class="col-sm-4 col-form-label text-right font-weight-bold"
        >
          별명
        </label>
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="text"
            v-model.trim="nickname"
            id="nickname"
            class="form-control"
            required
          />
          <div class="invalid-feedback">별명을 입력해주세요.</div>
        </div>
      </div>
      <button type="submit" class="btn btn-primary btn-block mt-3">가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const dateOfBirth = ref(null);
const nickname = ref(null);
const store = useUserStore();

const signUp = function () {
  if (password1.value.length < 8) {
    alert("비밀번호는 최소 8글자 이상 입력해주세요.");
  } else if (password1.value === password2.value) {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      date_of_birth: dateOfBirth.value,
      nickname: nickname.value,
    };
    store.signUp(payload);
  } else {
    alert("비밀번호가 다릅니다.");
  }
};
</script>

<style scoped>
.container {
  max-width: 500px;
}
</style>
