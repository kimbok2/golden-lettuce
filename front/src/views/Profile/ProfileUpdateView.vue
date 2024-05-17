<template>
  <div>
    <h1>ProfileUpdateView</h1>

    <form @submit.prevent="updateProfile">
      <div>
        <label for="dateOfBirth"> 생년월일 : </label>
        <input type="date" v-model.trim="dateOfBirth" id="dateOfBirth" />
      </div>
      <div>
        <label for="address"> 주소 : </label>
        <input type="text" v-model.trim="address" id="address" />
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
        <label for="creditScore"> 신용점수 : </label>
        <input type="number" v-model.trim="creditScore" id="creditScore" />
      </div>
      <div>
        <label for="profileimage"> 이미지 : </label>
        <input
          type="file"
          accept="image/*"
          id="profileimage"
          @change="onFileChange"
        />
      </div>
      <button type="submit" class="btn btn-primary mx-1">
        프로필 정보 저장
      </button>
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
const address = ref(null);
const creditScore = ref(null);
const profileImage = ref(null); // 이미지 파일을 저장할 ref
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
      address.value = response.data.address;
      creditScore.value = response.data.credit_score;
    })
    .catch((err) => {
      console.log(err);
    });
});

const onFileChange = (event) => {
  profileImage.value = event.target.files[0]; // 선택된 파일을 profileImage에 저장
};

const updateProfile = function () {
  const formData = new FormData();
  formData.append("date_of_birth", dateOfBirth.value);
  formData.append("address", address.value);
  formData.append("budget", budget.value);
  formData.append("salary", salary.value);
  formData.append("deposit_able", depositAble.value);
  formData.append("saving_able", savingAble.value);
  formData.append("deposit_period", depositPeriod.value);
  formData.append("saving_period", savingPeriod.value);
  formData.append("credit_score", creditScore.value);
  axios({
    method: "put",
    url: `${store.API_URL}/accounts/profile/${store.name}/`,
    headers: {
      Authorization: `Token ${store.token}`,
      "Content-Type": "multipart/form-data",
    },
    data: formData,
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
