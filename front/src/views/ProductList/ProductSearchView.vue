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
      <h3>상품 검색 조건 바</h3>
      <form @submit.prevent="selectSort">
        <span>상품 종류 : </span>
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
        <br />
        <span>저축 기간 : </span>
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
        <br />

        <span>정렬 기준 : </span>
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
        <br />
        <span>담당 은행 : </span>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank1"
            value="우리은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank1"> 우리은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank2"
            value="한국스탠다드차타드은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank2">
            한국스탠다드차타드은행
          </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank3"
            value="대구은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank3"> 대구은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank4"
            value="부산은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank4"> 부산은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank5"
            value="광주은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank5"> 광주은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank6"
            value="제주은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank6"> 제주은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank7"
            value="전북은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank7"> 전북은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank8"
            value="경남은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank8"> 경남은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank9"
            value="중소기업은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank9"> 중소기업은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank10"
            value="한국산업은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank10"> 한국산업은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank11"
            value="국민은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank11"> 국민은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank12"
            value="신한은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank12"> 신한은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank13"
            value="농협은행주식회사"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank13">
            농협은행주식회사
          </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank14"
            value="하나은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank14"> 하나은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank15"
            value="주식회사 케이뱅크"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank15">
            주식회사 케이뱅크
          </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank16"
            value="수협은행"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank16"> 수협은행 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank17"
            value="주식회사 카카오뱅크"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank17">
            주식회사 카카오뱅크
          </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            id="bank18"
            value="토스뱅크 주식회사"
            v-model="bankIds"
          />
          <label class="form-check-label" for="bank18">
            토스뱅크 주식회사
          </label>
        </div>

        <br /><br />
        <button type="submit" class="btn btn-primary">제출</button>
      </form>
    </div>
    <hr />
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
                      params: { id: product.id, type: selectedType },
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
import { RouterLink, RouterView } from "vue-router";
import { onMounted, ref, reactive } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const store = useUserStore();
const router = useRouter();
const products = ref(null);
const selectedType = ref("deposit");
const selectedType2 = ref(null);
const selectedPeriods = ref([1, 3, 6, 12, 24, 36]);
const bankIds = ref([
  "우리은행",
  "한국스탠다드차타드은행",
  "대구은행",
  "부산은행",
  "광주은행",
  "제주은행",
  "전북은행",
  "경남은행",
  "중소기업은행",
  "한국산업은행",
  "국민은행",
  "신한은행",
  "농협은행주식회사",
  "하나은행",
  "주식회사 케이뱅크",
  "수협은행",
  "주식회사 카카오뱅크",
  "토스뱅크 주식회사",
]);
const sorting = ref("intr_rate-");
// 옵션 선택 시 해당 옵션을 토대로 예.적금 리스트를 반환하는 함수
const selectSort = function () {
  if (selectedPeriods.value.length === 0) {
    periods.value = [1, 3, 6, 12, 24, 36];
  }
  if (bankIds.value.length === 0) {
    bankIds.value = [
      "우리은행",
      "한국스탠다드차타드은행",
      "대구은행",
      "부산은행",
      "광주은행",
      "제주은행",
      "전북은행",
      "경남은행",
      "중소기업은행",
      "한국산업은행",
      "국민은행",
      "신한은행",
      "농협은행주식회사",
      "하나은행",
      "주식회사 케이뱅크",
      "수협은행",
      "주식회사 카카오뱅크",
      "토스뱅크 주식회사",
    ];
  }
  const periods = selectedPeriods.value.slice();
  if (selectedType.value) {
    selectedType2.value = selectedType.value;
    axios({
      method: "get",
      url: `${store.API_URL}/finances/get_${selectedType.value}_products/1,3,6,12,24,36/${sorting.value}/${bankIds.value}/`,
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
</script>

<style scoped>
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
