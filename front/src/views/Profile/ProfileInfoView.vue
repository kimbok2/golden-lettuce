<template>
  <div>
    <h1>ProfileInfoView</h1>

    <h4>{{ user?.username }}의 프로필</h4>
    <hr />
    <p>생년월일 : {{ user?.date_of_birth }}</p>
    <p>보유자산 : {{ user?.budget }}</p>
    <p>월 수입 : {{ user?.salary }}</p>
    <p>예금 가능액 : {{ user?.deposit_able }}</p>
    <p>적금 가능액 : {{ user?.saving_able }}</p>
    <p>예금 희망 기간 : {{ user?.deposit_period }}</p>
    <p>적금 희망 기간 : {{ user?.saving_period }}</p>
    <button @click="goUpdate">프로필 정보 수정</button>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";
import { RouterLink, RouterView } from "vue-router";

const store = useUserStore();
const router = useRouter();
const user = ref(null);

onMounted(() => {
  console.log(store.name);
  axios({
    method: "get",
    url: `${store.API_URL}/accounts/profile/${store.name}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      user.value = response.data;
    })
    .catch((err) => {
      console.log(err);
    });
});

const goUpdate = function () {
  router.push({ name: "profile-update" });
};
</script>

<style scoped></style>
