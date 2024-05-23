<template>
  <div class="profile-container mx-auto row">
    <div class="col-md-7 text-center">
      <img
        :src="user?.profile_img ? apiUrl + user.profile_img : ''"
        alt="이미지없음"
        class="profile-img"
      />
      <div v-if="user?.join_deposit" class="mt-4">
        <h5 class="font-weight-bold">
          내가 가입한 예금 상품
          <span class="badge badge-primary"
            >{{ user.join_deposit.length }}개</span
          >
        </h5>
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
            >
              {{ deposit.fin_prdt_nm }}
            </RouterLink>
          </li>
        </ul>
        <ProfileGraphItem :join_product="user.join_deposit" />
      </div>
      <div v-if="user?.join_saving" class="mt-4">
        <h5 class="font-weight-bold">
          내가 가입한 적금 상품
          <span class="badge badge-primary"
            >{{ user.join_saving.length }}개</span
          >
        </h5>
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
            >
              {{ saving.fin_prdt_nm }}
            </RouterLink>
          </li>
        </ul>
        <ProfileGraphItem :join_product="user.join_saving" />
      </div>
    </div>
    <div class="col-md-5">
      <h4>{{ user?.nickname }}님의 프로필</h4>
      <hr />
      <div class="profile-details">
        <div
          v-for="(label, key) in profileFields"
          :key="key"
          class="row mb-3 align-items-center"
        >
          <label class="col-sm-4 col-form-label text-right font-weight-bold">
            {{ label }}
          </label>
          <div class="col-sm-8">
            <p class="form-control-plaintext">{{ formatField(key) }}</p>
          </div>
          <div class="col-12"><hr /></div>
          <!-- 구분선 추가 -->
        </div>
      </div>
      <div class="d-flex justify-content-center mt-3">
        <button class="btn btn-warning mx-1" @click="goUpdate">
          프로필 정보 수정
        </button>
        <button class="btn btn-warning mx-1" @click="goPasswordChange">
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
import ProfileGraphItem from "@/components/Profile/ProfileGraphItem.vue";

const apiUrl = "http://127.0.0:8000";
const router = useRouter();
const user = ref(null);
const store = useUserStore();

const profileFields = {
  id: "회원번호",
  nickname: "닉네임",
  date_of_birth: "생년월일",
  email: "이메일",
  address: "주소",
  budget: "보유자산",
  salary: "월 수입",
  deposit_able: "예금 가능액",
  saving_able: "적금 가능액",
  deposit_period: "예금 희망 기간",
  saving_period: "적금 희망 기간",
  credit_score: "신용 점수",
};

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

const formatField = (key) => {
  const value = user.value?.[key];
  if (
    key === "budget" ||
    key === "salary" ||
    key === "deposit_able" ||
    key === "saving_able"
  ) {
    return value ? formatNumber(value) + "원" : "정보를 입력해주세요.";
  } else if (key === "deposit_period" || key === "saving_period") {
    return value ? value + "개월" : "정보를 입력해주세요.";
  }
  return value || "정보를 입력해주세요.";
};

const goUpdate = function () {
  router.push({ name: "profile-update" });
};
const goPasswordChange = function () {
  router.push({ name: "profile-password-change" });
};
</script>

<style scoped>
.profile-container {
  max-width: 1000px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.profile-img {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 50%;
  border: 5px solid #f0f0f0;
}

.profile-details {
  margin-top: 20px;
}

.row {
  margin-bottom: 15px;
}

.custom-link {
  color: #007bff;
  text-decoration: none;
  font-weight: bold;
}

.custom-link:hover {
  color: #0056b3;
}

.btn {
  width: 200px;
}
</style>
