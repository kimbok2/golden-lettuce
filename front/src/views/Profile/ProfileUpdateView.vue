<template>
  <div>
    <h1 class="text-center mb-4">ProfileUpdateView</h1>
    <form
      @submit.prevent="updateProfile"
      class="mx-auto"
      style="max-width: 600px"
    >
      <div class="form-group row align-items-center mb-3">
        <label
          for="dateOfBirth"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >생년월일</label
        >
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
        </div>
      </div>

      <div class="form-group row align-items-center mb-3">
        <label
          for="address"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >주소</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="text"
            v-model.trim="address"
            id="address"
            class="form-control"
            required
          />
        </div>
      </div>

      <div class="form-group row align-items-center mb-3">
        <label
          for="budget"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >보유자산</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="number"
            v-model.trim="budget"
            id="budget"
            class="form-control"
          />
        </div>
      </div>

      <div class="form-group row align-items-center mb-3">
        <label
          for="salary"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >월급</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="number"
            v-model.trim="salary"
            id="salary"
            class="form-control"
          />
        </div>
      </div>

      <div class="form-group row align-items-center mb-3">
        <label
          for="depositAble"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >예금 가능액</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="number"
            v-model.trim="depositAble"
            id="depositAble"
            class="form-control"
          />
        </div>
      </div>

      <div class="form-group row align-items-center mb-3">
        <label
          for="savingAble"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >적금 가능액</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="number"
            v-model.trim="savingAble"
            id="savingAble"
            class="form-control"
          />
        </div>
      </div>

      <div class="form-group row align-items-center mb-3">
        <label
          for="depositPeriod"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >예금 희망기간</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <select
            v-model.trim="depositPeriod"
            id="depositPeriod"
            class="form-control"
          >
            <option value="1">1개월</option>
            <option value="3">3개월</option>
            <option value="6">6개월</option>
            <option value="12">12개월</option>
            <option value="24">24개월</option>
            <option value="36">36개월</option>
          </select>
        </div>
      </div>

      <div class="form-group row align-items-center mb-3">
        <label
          for="savingPeriod"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >적금 희망기간</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <select
            v-model.trim="savingPeriod"
            id="savingPeriod"
            class="form-control"
          >
            <option value="1">1개월</option>
            <option value="3">3개월</option>
            <option value="6">6개월</option>
            <option value="12">12개월</option>
            <option value="24">24개월</option>
            <option value="36">36개월</option>
          </select>
        </div>
      </div>

      <div class="form-group row align-items-center mb-3">
        <label
          for="creditScore"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >신용점수</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="number"
            v-model.trim="creditScore"
            id="creditScore"
            class="form-control"
          />
        </div>
      </div>

      <div class="form-group row align-items-center mb-3">
        <label
          for="profileimage"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >이미지</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="file"
            accept="image/*"
            id="profileimage"
            @change="onFileChange"
            class="form-control"
          />
        </div>
      </div>

      <button type="submit" class="btn btn-primary btn-block mt-3">
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
const profileImage = ref(null);
const store = useUserStore();
const router = useRouter();

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/accounts/profile/${store.name}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
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
  profileImage.value = event.target.files[0];
};

const updateProfile = function () {
  const formData = new FormData();
  if (dateOfBirth.value) formData.append("date_of_birth", dateOfBirth.value);
  if (address.value) formData.append("address", address.value);
  if (budget.value) formData.append("budget", budget.value);
  if (salary.value) formData.append("salary", salary.value);
  if (depositAble.value) formData.append("deposit_able", depositAble.value);
  if (savingAble.value) formData.append("saving_able", savingAble.value);
  if (depositPeriod.value)
    formData.append("deposit_period", depositPeriod.value);
  if (savingPeriod.value) formData.append("saving_period", savingPeriod.value);
  if (creditScore.value) formData.append("credit_score", creditScore.value);
  if (profileImage.value) formData.append("profile_image", profileImage.value);
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

<style scoped>
.container {
  max-width: 600px;
}
</style>
