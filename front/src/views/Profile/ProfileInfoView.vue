<template>
  <div>
    <h1 class="text-center mb-4">ProfileInfoView</h1>
    <div class="mx-auto" style="max-width: 600px">
      <h4 class="text-center">{{ user?.username }}의 프로필</h4>
      <div class="text-center my-3">
        <img
          :src="user?.profile_img"
          alt="이미지없음"
          class="img-thumbnail"
          style="max-width: 200px"
        />
      </div>
      <hr />
      <div class="row mb-3">
        <label class="col-sm-4 col-form-label text-right font-weight-bold"
          >생년월일 :</label
        >
        <div class="col-sm-8">
          <p class="form-control-plaintext">{{ user?.date_of_birth }}</p>
        </div>
      </div>
      <div class="row mb-3">
        <label class="col-sm-4 col-form-label text-right font-weight-bold"
          >주소 :</label
        >
        <div class="col-sm-8">
          <p class="form-control-plaintext">{{ user?.address }}</p>
        </div>
      </div>
      <div class="row mb-3">
        <label class="col-sm-4 col-form-label text-right font-weight-bold"
          >보유자산 :</label
        >
        <div class="col-sm-8">
          <p class="form-control-plaintext">
            {{
              user?.budget
                ? formatNumber(user?.budget) + "원"
                : "보유 자산을 입력해주세요."
            }}
          </p>
        </div>
      </div>
      <div class="row mb-3">
        <label class="col-sm-4 col-form-label text-right font-weight-bold"
          >월 수입 :</label
        >
        <div class="col-sm-8">
          <p class="form-control-plaintext">
            {{
              user?.salary
                ? formatNumber(user?.salary) + "원"
                : "월 수입을 입력해주세요."
            }}
          </p>
        </div>
      </div>
      <div class="row mb-3">
        <label class="col-sm-4 col-form-label text-right font-weight-bold"
          >예금 가능액 :</label
        >
        <div class="col-sm-8">
          <p class="form-control-plaintext">
            {{
              user?.deposit_able
                ? formatNumber(user?.deposit_able) + "원"
                : "예금 가능액을 입력해주세요."
            }}
          </p>
        </div>
      </div>
      <div class="row mb-3">
        <label class="col-sm-4 col-form-label text-right font-weight-bold"
          >적금 가능액 :</label
        >
        <div class="col-sm-8">
          <p class="form-control-plaintext">
            {{
              user?.saving_able
                ? formatNumber(user?.saving_able) + "원"
                : "적금 가능액을 입력해주세요."
            }}
          </p>
        </div>
      </div>
      <div class="row mb-3">
        <label class="col-sm-4 col-form-label text-right font-weight-bold"
          >예금 희망 기간 :</label
        >
        <div class="col-sm-8">
          <p class="form-control-plaintext">{{ user?.deposit_period }}개월</p>
        </div>
      </div>
      <div class="row mb-3">
        <label class="col-sm-4 col-form-label text-right font-weight-bold"
          >적금 희망 기간 :</label
        >
        <div class="col-sm-8">
          <p class="form-control-plaintext">{{ user?.saving_period }}개월</p>
        </div>
      </div>
      <div class="row mb-3">
        <label class="col-sm-4 col-form-label text-right font-weight-bold"
          >신용 점수 :</label
        >
        <div class="col-sm-8">
          <p class="form-control-plaintext">
            {{
              user?.credit_score
                ? user.credit_score
                : "신용 점수를 입력해주세요."
            }}
          </p>
        </div>
      </div>
      <div v-if="user?.join_deposit" class="mb-3">
        <h4 class="font-weight-bold">
          내가 가입한 예금 상품
          <span class="badge badge-primary">
            {{ user.join_deposit.length }}개</span
          >
        </h4>
        <ul class="list-group">
          <li
            v-for="deposit in user.join_deposit"
            :key="deposit.id"
            class="list-group-item"
          >
            <RouterLink
              :to="{
                name: 'products-detail',
                params: { id: deposit.id, type: 'deposit' },
              }"
              class="custom-link"
              >{{ deposit.fin_prdt_nm }}</RouterLink
            >
          </li>
        </ul>
      </div>
      <div v-if="user?.join_saving" class="mb-3">
        <h4 class="font-weight-bold">
          내가 가입한 적금 상품
          <span class="badge badge-primary"
            >{{ user.join_saving.length }}개</span
          >
        </h4>
        <ul class="list-group">
          <li
            v-for="saving in user.join_saving"
            :key="saving.id"
            class="list-group-item"
          >
            <RouterLink
              :to="{
                name: 'products-detail',
                params: { id: saving.id, type: 'saving' },
              }"
              class="custom-link"
              >{{ saving.fin_prdt_nm }}</RouterLink
            >
          </li>
        </ul>
      </div>
      <div class="d-flex justify-content-center mt-3">
        <button class="btn btn-primary mx-1" @click="goUpdate">
          프로필 정보 수정
        </button>
        <button class="btn btn-secondary mx-1" @click="goChangePassword">
          비밀번호 변경
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref, watch } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const router = useRouter();
const user = ref(null);
const store = useUserStore();

watch(
  () => store.userInfo,
  (newUser) => {
    user.value = newUser;
  }
);

onMounted(() => {
  store.getUserInfo();
  user.value = store.userInfo;
});

const formatNumber = (value) => {
  if (typeof value !== "number") return "";
  return new Intl.NumberFormat().format(value);
};

const goUpdate = function () {
  router.push({ name: "profile-update" });
};

const goChangePassword = function () {
  router.push({ name: "profile-password-change" });
};
</script>

<style scoped>
.img-thumbnail {
  max-width: 200px;
}

.custom-link {
  color: inherit; /* 부모 요소의 색상 상속 */
  text-decoration: none; /* 밑줄 제거 */
}
.custom-link:hover {
  color: gray; /* 호버 시 색상 변경 (원하는 색상으로 변경 가능) */
}
</style>
