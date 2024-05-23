<template>
  <div>
    <h1 class="text-center mb-4">내 프로필 수정</h1>
    <div class="text-center my-3">
      <img
        v-if="!imageUpdated"
        :src="apiUrl + profileImageUrl"
        alt="프로필 이미지 없음"
        class="img-thumbnail rounded-circle"
        style="width: 120px; height: 120px; object-fit: cover"
      />
      <img
        v-else
        :src="profileImageUrl"
        alt="프로필 이미지 없음"
        class="img-thumbnail rounded-circle"
        style="width: 120px; height: 120px; object-fit: cover"
      />
    </div>
    <form
      @submit.prevent="updateProfile"
      class="mx-auto"
      style="max-width: 600px"
    >
      <div class="form-group row align-items-center mb-3">
        <label
          for="profileimage"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >프로필 이미지</label
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
          for="email"
          class="col-sm-4 col-form-label text-right font-weight-bold"
          >이메일</label
        >
        <div class="col-sm-1 d-flex justify-content-center">
          <div class="border-right" style="height: 2rem"></div>
        </div>
        <div class="col-sm-7">
          <input
            type="email"
            v-model.trim="email"
            id="email"
            class="form-control"
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

      <button type="submit" class="btn btn-warning btn-block mt-3">
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
const email = ref(null);
const creditScore = ref(null);
const apiUrl = "https://kgarrry.pythonanywhere.com";
const profileImage = ref(null); // 파일 객체를 저장할 ref
const profileImageUrl = ref(null); // 이미지 URL을 저장할 ref
const imageUpdated = ref(false);
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
      address.value = response.data.address;
      email.value = response.data.email;
      budget.value = response.data.budget;
      salary.value = response.data.salary;
      depositAble.value = response.data.deposit_able;
      savingAble.value = response.data.saving_able;
      depositPeriod.value = response.data.deposit_period;
      savingPeriod.value = response.data.saving_period;
      creditScore.value = response.data.credit_score;
      profileImageUrl.value = response.data.profile_img;
    })
    .catch((err) => {
      console.log(err);
    });
});

const onFileChange = (event) => {
  const file = event.target.files[0];
  // console.log(file);
  console.log(file.name);
  if (file) {
    profileImage.value = file;
    profileImageUrl.value = URL.createObjectURL(file);
    imageUpdated.value = true;
  }
};

const updateProfile = async () => {
  const formData = new FormData();
  // 음이 아닌 정수인지 확인하는 유틸리티 함수
  const isNonNegativeInteger = (value) => {
    return Number.isInteger(value) && value >= 0;
  };

  // 필수 유효성 검사
  if (budget.value && !isNonNegativeInteger(Number(budget.value))) {
    alert("보유자산은 음이 아닌 정수여야 합니다.");
    return;
  }
  if (salary.value && !isNonNegativeInteger(Number(salary.value))) {
    alert("월급은 음이 아닌 정수여야 합니다.");
    return;
  }
  if (depositAble.value && !isNonNegativeInteger(Number(depositAble.value))) {
    alert("예금 가능액은 음이 아닌 정수여야 합니다.");
    return;
  }
  if (savingAble.value && !isNonNegativeInteger(Number(savingAble.value))) {
    alert("적금 가능액은 음이 아닌 정수여야 합니다.");
    return;
  }
  if (dateOfBirth.value) formData.append("date_of_birth", dateOfBirth.value);
  if (email.value) formData.append("email", email.value);
  if (address.value) formData.append("address", address.value);
  if (budget.value) formData.append("budget", budget.value);
  if (salary.value) formData.append("salary", salary.value);
  if (depositAble.value) formData.append("deposit_able", depositAble.value);
  if (savingAble.value) formData.append("saving_able", savingAble.value);
  if (depositPeriod.value)
    formData.append("deposit_period", depositPeriod.value);
  if (savingPeriod.value) formData.append("saving_period", savingPeriod.value);
  if (creditScore.value) formData.append("credit_score", creditScore.value);
  if (profileImage.value) formData.append("profile_img", profileImage.value);

  try {
    const response = await axios.put(
      `${store.API_URL}/accounts/profile/${store.name}/`,
      formData,
      {
        headers: {
          Authorization: `Token ${store.token}`,
          "Content-Type": "multipart/form-data",
        },
      }
    );
    console.log(response);
    router.push({ name: "profile" });
  } catch (err) {
    console.log(err);
    let messages = "";
    for (const field in err.response.data) {
      if (err.response.data.hasOwnProperty(field)) {
        // 각 필드의 오류 메시지를 messages 문자열에 추가
        messages += `${field} : ${err.response.data[field]}\n`;
      }
    }
    alert(messages);
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
}
.img-thumbnail {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 50%;
}
</style>
