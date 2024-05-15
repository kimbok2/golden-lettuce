<template>
  <div>
    <h1>ProfileUpdateView</h1>

    <form @submit.prevent="updateProfile">
      <div>
        <label for="dateOfBirth"> 생년월일 : </label>
        <input type="date" v-model.trim="dateOfBirth" id="dateOfBirth" />
      </div>
      <div>
        <label for="budget"> 보유자산 : </label>
        <input type="number" v-model.trim="budget" id="budget" />
      </div>
      <div>
        <label for="salary"> 월급 : </label>
        <input type="number" v-model.trim="salary" id="salary" />
      </div>
      <div>
        <label for="depositAble"> 예금 가능액 : </label>
        <input type="number" v-model.trim="depositAble" id="depositAble" />
      </div>
      <div>
        <label for="savingAble"> 적금 가능액 : </label>
        <input type="number" v-model.trim="savingAble" id="savingAble" />
      </div>
      <div>
        <label for="depositPeriod"> 예금 희망기간 : </label>
        <input type="number" v-model.trim="depositPeriod" id="depositPeriod" />
      </div>
      <div>
        <label for="savingPeriod"> 적금 희망기간 : </label>
        <input type="number" v-model.trim="savingPeriod" id="savingPeriod" />
      </div>
      <div>
        <label for="profileimage"> 이미지(구현대기) : </label>
        <input type="file" accept="image/*" id="profileimage" />
      </div>
      <input type="submit" value="프로필 정보 저장" />
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const dateOfBirth = ref(null);
const budget = ref(null);
const salary = ref(null);
const depositAble = ref(null);
const savingAble = ref(null);
const depositPeriod = ref(null);
const savingPeriod = ref(null);

const store = useUserStore();
const router = useRouter();
const user = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/accounts/profile/${store.name}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      // user.value = response.data;
      dateOfBirth.value = response.data.date_of_birth;
      budget.value = response.data.budget;
      salary.value = response.data.salary;
      depositAble.value = response.data.deposit_able;
      savingAble.value = response.data.saving_able;
      depositPeriod.value = response.data.deposit_period;
      savingPeriod.value = response.data.saving_period;
    })
    .catch((err) => {
      console.log(err);
    });
});

const updateProfile = function () {
  axios({
    method: "put",
    url: `${store.API_URL}/accounts/profile/${store.name}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      date_of_birth: dateOfBirth.value,
      budget: budget.value,
      salary: salary.value,
      deposit_able: depositAble.value,
      saving_able: savingAble.value,
      deposit_period: depositPeriod.value,
      saving_period: savingPeriod.value,
    },
  })
    .then((response) => {
      console.log(response);
      router.push({ name: "profile" });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style>
