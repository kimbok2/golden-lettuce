<template>
  <div class="search-container">
    <button @click="savedata" class="btn btn-primary">
      DB저장하는 버튼 1회만 실행
    </button>
    <div class="container">
      <form @submit.prevent="selectSort">
        <!-- 상품 종류 -->
        <div class="form-group row mb-3">
          <label class="col-sm-2 col-form-label">상품 종류</label>
          <div class="col-sm-10">
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                id="deposit"
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
                value="saving"
                v-model="selectedType"
                required
              />
              <label class="form-check-label" for="saving">적금</label>
            </div>
          </div>
        </div>

        <!-- 저축 기간 -->
        <div class="form-group row mb-3">
          <label class="col-sm-2 col-form-label">저축 기간</label>
          <div class="col-sm-10">
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="checkbox"
                id="per1"
                name="savingPeriod"
                value="1"
                v-model="selectedPeriods"
              />
              <label class="form-check-label" for="per1"> 1개월 </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="checkbox"
                id="per3"
                name="savingPeriod"
                value="3"
                v-model="selectedPeriods"
              />
              <label class="form-check-label" for="per3"> 3개월 </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="checkbox"
                id="per6"
                name="savingPeriod"
                value="6"
                v-model="selectedPeriods"
              />
              <label class="form-check-label" for="per6"> 6개월 </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="checkbox"
                id="per12"
                name="savingPeriod"
                value="12"
                v-model="selectedPeriods"
              />
              <label class="form-check-label" for="per12"> 12개월 </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="checkbox"
                id="per24"
                name="savingPeriod"
                value="24"
                v-model="selectedPeriods"
              />
              <label class="form-check-label" for="per24"> 24개월 </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="checkbox"
                id="per36"
                name="savingPeriod"
                value="36"
                v-model="selectedPeriods"
              />
              <label class="form-check-label" for="per36"> 36개월 </label>
            </div>
            <div class="mt-2">
              <button
                type="button"
                class="btn btn-secondary btn-sm"
                @click="selectAllPeriods"
              >
                전체 선택
              </button>
              <button
                type="button"
                class="btn btn-secondary btn-sm"
                @click="deselectAllPeriods"
              >
                전체 해제
              </button>
            </div>
          </div>
        </div>

        <!-- 정렬 기준 -->
        <div class="form-group row mb-3">
          <label class="col-sm-2 col-form-label">정렬 기준</label>
          <div class="col-sm-10">
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                id="intr_rate-"
                value="intr_rate-"
                v-model="sorting"
                required
              />
              <label class="form-check-label" for="intr_rate-">
                기본금리 높은 순
              </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                id="intr_rate"
                value="intr_rate"
                v-model="sorting"
                required
              />
              <label class="form-check-label" for="intr_rate">
                기본 금리 낮은 순
              </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                id="intr_rate2-"
                value="intr_rate2-"
                v-model="sorting"
                required
              />
              <label class="form-check-label" for="intr_rate2-">
                최고 우대 금리 높은 순
              </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                id="intr_rate2"
                value="intr_rate2"
                v-model="sorting"
                required
              />
              <label class="form-check-label" for="intr_rate2">
                최고 우대 금리 낮은 순
              </label>
            </div>
          </div>
        </div>

        <!-- 담당 은행 -->
        <div class="form-group row mb-3">
          <label class="col-sm-2 col-form-label">담당 은행</label>
          <div class="col-sm-10">
            <div class="row">
              <div
                class="col-6 col-md-4 col-lg-3"
                v-for="bank in banks"
                :key="bank.id"
              >
                <div class="form-check form-check-inline">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    :id="'bank' + bank.id"
                    :value="bank.name"
                    v-model="bankIds"
                  />
                  <label class="form-check-label" :for="'bank' + bank.id">{{
                    bank.name
                  }}</label>
                </div>
              </div>
            </div>
            <div class="mt-2">
              <button
                type="button"
                class="btn btn-secondary btn-sm"
                @click="selectAllBanks"
              >
                전체 선택
              </button>
              <button
                type="button"
                class="btn btn-secondary btn-sm"
                @click="deselectAllBanks"
              >
                전체 해제
              </button>
            </div>
          </div>
        </div>

        <button type="submit" class="btn btn-primary">제출</button>
      </form>
    </div>
    <hr />

    <!-- 검색 결과 -->
    <div>
      <ul class="text-start ps-0 text-center">
        <li class="card rounded-0">
          <div class="row m-0">
            <div class="col-1">
              <b>공시<br />기준월</b>
            </div>
            <div class="col-2"><b>담당 은행</b></div>
            <div class="col-3"><b>상품명</b></div>
            <div class="col-6">
              <div class="row m-0">
                <div class="col-2"><b>1개월</b></div>
                <div class="col-2"><b>3개월</b></div>
                <div class="col-2"><b>6개월</b></div>
                <div class="col-2"><b>12개월</b></div>
                <div class="col-2"><b>24개월</b></div>
                <div class="col-2"><b>36개월</b></div>
              </div>
            </div>
          </div>
        </li>
        <div v-if="products">
          <div v-for="product in products" :key="product.id">
            <li class="card border border-0 border-bottom rounded-0">
              <div class="row m-0">
                <div class="col-1">
                  {{ product.dcls_month }}
                </div>
                <div class="col-2">{{ product.kor_co_nm }}</div>

                <div class="col-3">
                  <RouterLink
                    :to="{
                      name: 'products-detail',
                      params: { id: product.id, type: selectedType2 },
                    }"
                    class="custom-link"
                    >{{ product.fin_prdt_nm }}</RouterLink
                  >
                </div>
                <div class="col-6">
                  <div class="row m-0" v-if="selectedType2 === 'deposit'">
                    <div
                      class="col-2"
                      v-for="term in ['1', '3', '6', '12', '24', '36']"
                      :key="term"
                    >
                      <div v-if="getRate(product.depositoption_set, term)">
                        {{ getRate(product.depositoption_set, term) }}%
                        <hr class="small-hr" />
                        {{ getRate2(product.depositoption_set, term) }}%
                      </div>
                    </div>
                  </div>
                  <div class="row m-0" v-else-if="selectedType2 === 'saving'">
                    <div
                      class="col-2"
                      v-for="term in ['1', '3', '6', '12', '24', '36']"
                      :key="term"
                    >
                      <div v-if="getRate(product.savingoption_set, term)">
                        {{ getRate(product.savingoption_set, term) }}%
                        <hr class="small-hr" />
                        {{ getRate2(product.savingoption_set, term) }}%
                      </div>
                    </div>
                  </div>
                </div>
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
import { RouterLink } from "vue-router";
import { onMounted, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";
import { useSearchStore } from "@/stores/search";

const store = useUserStore();
const searchStore = useSearchStore();
const router = useRouter();

const selectedType = ref(searchStore.selectedType);
const selectedType2 = ref(searchStore.selectedType);
const selectedPeriods = ref(searchStore.selectedPeriods);
const bankIds = ref(searchStore.bankIds);
const sorting = ref(searchStore.sorting);
const products = ref(searchStore.products);
let i = 1;
const banks = [
  { id: i++, name: "우리은행" },
  { id: i++, name: "한국스탠다드차타드은행" },
  { id: i++, name: "대구은행" },
  { id: i++, name: "부산은행" },
  { id: i++, name: "광주은행" },
  { id: i++, name: "제주은행" },
  { id: i++, name: "전북은행" },
  { id: i++, name: "경남은행" },
  { id: i++, name: "중소기업은행" },
  { id: i++, name: "한국산업은행" },
  { id: i++, name: "국민은행" },
  { id: i++, name: "신한은행" },
  { id: i++, name: "농협은행주식회사" },
  { id: i++, name: "하나은행" },
  { id: i++, name: "주식회사 케이뱅크" },
  { id: i++, name: "수협은행" },
  { id: i++, name: "주식회사 카카오뱅크" },
  { id: i++, name: "토스뱅크 주식회사" },
];

const selectAllPeriods = () => {
  selectedPeriods.value = ["1", "3", "6", "12", "24", "36"];
};

const deselectAllPeriods = () => {
  selectedPeriods.value = [];
};

const selectAllBanks = () => {
  bankIds.value = banks.map((bank) => bank.name);
};

const deselectAllBanks = () => {
  bankIds.value = [];
};

const selectSort = function () {
  if (selectedPeriods.value.length === 0) {
    selectedPeriods.value = [1, 3, 6, 12, 24, 36];
  }
  if (bankIds.value.length === 0) {
    bankIds.value = banks.map((bank) => bank.name);
  }
  searchStore.selectedType = selectedType.value;
  searchStore.selectedPeriods = selectedPeriods.value;
  searchStore.sorting = sorting.value;
  searchStore.bankIds = bankIds.value;
  selectedType2.value = selectedType.value;
  const periods = selectedPeriods.value.slice();
  if (selectedType.value) {
    axios({
      method: "get",
      url: `${store.API_URL}/finances/get_${selectedType.value}_products/1,3,6,12,24,36/${sorting.value}/${bankIds.value}/`,
      // headers: {
      //   Authorization: `Token ${store.token}`,
      // },
    })
      .then((response) => {
        products.value = response.data;
        searchStore.products = response.data;
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
    url: `${store.API_URL}/finances/save_bank/`,
  })
    .then((resp) => {
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
    })
    .catch((errors) => {
      console.log(errors);
    });
};

const getRate = (options, term) => {
  const option = options?.find((opt) => opt.save_trm === term);
  return option ? option.intr_rate : null;
};
const getRate2 = (options, term) => {
  const option = options?.find((opt) => opt.save_trm === term);
  return option ? option.intr_rate2 : null;
};

onMounted(() => {
  if (searchStore.products) {
    products.value = searchStore.products;
  }
});
</script>

<style scoped>
.search-container {
  max-width: 1000px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
.nowrap {
  white-space: nowrap;
  text-overflow: ellipsis;
}
.custom-link {
  color: inherit; /* 부모 요소의 색상 상속 */
  text-decoration: none; /* 밑줄 제거 */
}
.custom-link:hover {
  color: gray; /* 호버 시 색상 변경 (원하는 색상으로 변경 가능) */
}
.row {
  align-items: center; /* 수직 정렬 */
}
.small-hr {
  margin: 4px 0; /* 상하 마진을 4px로 설정 */
}
</style>
