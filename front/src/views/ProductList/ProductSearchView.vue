<template>
  <div>
    <h1>
      ProductSearchView
      <button @click="savedata" class="btn btn-primary">
        DB초기화 이후 1회만 실행
      </button>
    </h1>
    <hr />

    <div class="container">
      <h3>제품 검색 조건 바</h3>
      <form @submit.prevent="selectSort">
        <span>상품 종류 : </span>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="radio"
            id="deposit"
            name="fruit"
            value="deposit"
            v-model="selectedType"
            required
          />
          <label class="form-check-label" for="deposit"> 예금 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="radio"
            id="saving"
            name="fruit"
            value="saving"
            v-model="selectedType"
            required
          />
          <label class="form-check-label" for="saving">적금</label>
        </div>
        <br />
        <span>저축 기간 : </span>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="1"
            name="savingPeriod"
            value="1"
            v-model="selectedPeriods"
          />
          <label class="form-check-label" for="1"> 1개월 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="3"
            name="savingPeriod"
            value="3"
            v-model="selectedPeriods"
          />
          <label class="form-check-label" for="3"> 3개월 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="6"
            name="savingPeriod"
            value="6"
            v-model="selectedPeriods"
          />
          <label class="form-check-label" for="6"> 6개월 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="12"
            name="savingPeriod"
            value="12"
            v-model="selectedPeriods"
          />
          <label class="form-check-label" for="12"> 12개월 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="24"
            name="savingPeriod"
            value="24"
            v-model="selectedPeriods"
          />
          <label class="form-check-label" for="24"> 24개월 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="36"
            name="savingPeriod"
            value="36"
            v-model="selectedPeriods"
          />
          <label class="form-check-label" for="36"> 36개월 </label>
        </div>
        <br /><br />

        <button type="submit" class="btn btn-primary">제출</button>
      </form>
    </div>
    <hr />
    <div>
      <ul class="text-start ps-0">
        <li class="card rounded-0">
          <div class="row m-0">
            <div class="col-1">상품번호</div>
            <div class="col-5">상품명</div>
            <div class="col-3">담당 은행</div>
            <div class="col-1">가입 방법</div>
            <div class="col-2">공시기준월</div>
          </div>
        </li>
        <div v-if="products">
          <div v-for="product in products">
            <li class="card border border-0 border-bottom rounded-0">
              <div class="row m-0">
                <div class="col-1">{{ product.id }}</div>
                <div class="col-5">
                  <RouterLink
                    :to="{
                      name: 'products-detail',
                      params: { id: product.id, type: selectedType },
                    }"
                    class="custom-link"
                    >{{ product.fin_prdt_nm }}</RouterLink
                  >
                </div>
                <div class="col-3">{{ product.kor_co_nm }}</div>
                <div class="col-1">{{ product.join_deny }}</div>
                <div class="col-2 text-center">{{ product.dcls_month }}</div>
              </div>
            </li>
          </div>
        </div>
      </ul>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { RouterLink, RouterView } from "vue-router";
import { onMounted, ref, reactive } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const store = useUserStore();
const router = useRouter();
const products = ref(null);
const selectedType = ref(null);
const selectedPeriods = ref([]);
// 옵션 선택 시 해당 옵션을 토대로 예.적금 리스트를 반환하는 함수
const selectSort = function () {
  const URL = ref(null);
  if (selectedPeriods.value.length === 0) {
    URL.value = `${store.API_URL}/finances/get_${selectedType.value}_all/`;
  } else {
    const periods = selectedPeriods.value.slice();
    URL.value = `${store.API_URL}/finances/get_${selectedType.value}_products/${periods}/`;
  }
  if (selectedType.value) {
    axios({
      method: "get",
      url: URL.value,
      // headers: {
      //   Authorization: `Token ${store.token}`,
      // },
    })
      .then((response) => {
        products.value = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  }
};

// 데이터 불러와 저장하는 함수
const savedata = function () {
  axios({
    method: "get",
    url: `${store.API_URL}/finances/save_deposit/`,
  })
    .then((response) => {
      axios({
        method: "get",
        url: `${store.API_URL}/finances/save_saving/`,
      })
        .then((res) => {
          alert("저장 완료!");
        })
        .catch((error) => {
          console.log(error);
        });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
.custom-link {
  color: inherit; /* 부모 요소의 색상 상속 */
  text-decoration: none; /* 밑줄 제거 */
}
.custom-link:hover {
  color: gray; /* 호버 시 색상 변경 (원하는 색상으로 변경 가능) */
}
</style>
