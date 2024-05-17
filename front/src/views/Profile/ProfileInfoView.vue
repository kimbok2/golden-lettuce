<template>
  <div>
    <h1>ProfileInfoView</h1>

    <h4>{{ user?.username }}의 프로필</h4>
    <hr />
    <p>생년월일 : {{ user?.date_of_birth }}</p>
    <p>주소 : {{ user?.address }}</p>
    <p>보유자산 : {{ user?.budget }}</p>
    <p>월 수입 : {{ user?.salary }}</p>
    <p>예금 가능액 : {{ user?.deposit_able }}</p>
    <p>적금 가능액 : {{ user?.saving_able }}</p>
    <p>예금 희망 기간 : {{ user?.deposit_period }}</p>
    <p>적금 희망 기간 : {{ user?.saving_period }}</p>
    <p>신용 점수 : {{ user?.credit_score }}</p>
    <div class="d-flex justify-content-center mt-3">
      <button class="btn btn-primary mx-1" @click="goUpdate">
        프로필 정보 수정
      </button>
      <button class="btn btn-primary mx-1" @click="goChangePassword">
        비밀번호 변경
      </button>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";
import { RouterLink, RouterView } from "vue-router";

const router = useRouter();
const user = ref(null);
const store = useUserStore();

onMounted(() => {
  store.getUserInfo();
  user.value = store.userInfo;
});

const goUpdate = function () {
  router.push({ name: "profile-update" });
};
const goChangePassword = function () {
  router.push({ name: "profile-password-change" });
};
</script>

<style scoped></style>
