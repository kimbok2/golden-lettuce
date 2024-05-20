<template>
  <div>
    <h1>ProductDetailView</h1>
    <hr />
    <div v-if="product">
      <h4>{{ product.fin_prdt_nm }}</h4>

      <span>가입자 수 : {{ product.join_user_count }}명</span>
      <p>{{ product.join_user }}</p>
      <button
        v-if="!isUserJoined"
        @click="joinProduct('post')"
        class="btn btn-primary mx-2"
      >
        가입하기
      </button>
      <button v-else @click="joinProduct('delete')" class="btn btn-danger mx-2">
        해지하기
      </button>
      <button
        v-if="!isUserCompared"
        @click="compareProduct('post')"
        class="btn btn-primary mx-2"
      >
        비교 등록
      </button>
      <button
        v-else
        @click="compareProduct('delete')"
        class="btn btn-danger mx-2"
      >
        비교 해제
      </button>

      <hr />
      <h5>담당 회사 : {{ product.kor_co_nm }}</h5>
      <p>
        공시제출월 : {{ product.dcls_month.substring(0, 4) }}년
        {{ product.dcls_month.substring(5) }}월
      </p>
      <p>공시시작일 : {{ product.dcls_strt_day }}</p>
      <p>
        공시종료일 : {{ product.dcls_end_day ? product.dcls_end_day : "없음" }}
      </p>
      <p>가입 방법 : {{ product.join_way }}</p>
      <p>
        최고 한도 :
        {{
          product.max_limit
            ? formatNumber(product.max_limit) + " 원"
            : "최고 한도 없음"
        }}
      </p>
      <p>우대 조건 : {{ product.spcl_cnd }}</p>
      <p>만기 후 이자율 : {{ product.mtrt_int }}</p>
      <p>유의사항 : {{ product.etc_note }}</p>
      <div>
        <h5>옵션 정보</h5>
        <div>
          <ul class="text-start ps-0">
            <li class="card rounded-0">
              <div class="row m-0">
                <div class="col-1 text-center">번호</div>
                <div class="col-3 text-center">저축기간</div>
                <div class="col-3 text-center">저축 금리</div>
                <div class="col-3 text-center">최고 우대 금리</div>
                <div class="col-2 text-center">저축금리 유형</div>
              </div>
            </li>
            <div v-if="route.params.type === 'deposit'">
              <div
                v-for="(option, index) in product.depositoption_set"
                :key="option.id"
              >
                <li class="card border border-0 border-bottom rounded-0">
                  <div class="row m-0">
                    <div class="col-1 text-center">{{ index + 1 }}</div>
                    <div class="col-3 text-center">{{ option.save_trm }}</div>
                    <div class="col-3 text-center">{{ option.intr_rate }}</div>
                    <div class="col-3 text-center">{{ option.intr_rate2 }}</div>
                    <div class="col-2 text-center">
                      {{ option.intr_rate_type_nm }}
                    </div>
                  </div>
                </li>
              </div>
            </div>
            <div v-else-if="route.params.type === 'saving'">
              <div
                v-for="(option, index) in product.savingoption_set"
                :key="option.id"
              >
                <li class="card border border-0 border-bottom rounded-0">
                  <div class="row m-0">
                    <div class="col-1 text-center">{{ index + 1 }}</div>
                    <div class="col-3 text-center">{{ option.save_trm }}</div>
                    <div class="col-3 text-center">{{ option.intr_rate }}</div>
                    <div class="col-3 text-center">{{ option.intr_rate2 }}</div>
                    <div class="col-2 text-center">
                      {{ option.intr_rate_type_nm }}
                    </div>
                  </div>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </div>
    </div>
    <p v-else>상품 정보가 없습니다.</p>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { onMounted, ref, computed } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const store = useUserStore();
const productType = ref(null);
const productId = ref(null);
const product = ref(null);

const fetchProduct = () => {
  axios({
    method: "get",
    url: `${store.API_URL}/finances/get_${productType.value}/${productId.value}/`,
  })
    .then((response) => {
      product.value = response.data;
    })
    .catch((err) => {
      console.log(err);
    });
};

onMounted(() => {
  productType.value = route.params.type;
  productId.value = route.params.id;
  fetchProduct();
});

const formatNumber = (value) => {
  if (typeof value !== "number") return "최고 한도 없음";
  return new Intl.NumberFormat().format(value);
};

const joinProduct = (apiMethod) => {
  axios({
    method: apiMethod,
    url: `${store.API_URL}/finances/join_${productType.value}/${productId.value}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("가입/해지");
      fetchProduct(); // 업데이트 후 데이터를 다시 가져옴
    })
    .catch((err) => {
      console.log(err);
    });
};

const compareProduct = (apiMethod) => {
  axios({
    method: apiMethod,
    url: `${store.API_URL}/finances/compare_${productType.value}/${productId.value}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("비교/해제");
      fetchProduct(); // 업데이트 후 데이터를 다시 가져옴
    })
    .catch((err) => {
      console.log(err);
    });
};

const isUserJoined = computed(() => {
  return product.value && product.value.join_user.includes(store.userInfo.id);
});

const isUserCompared = computed(() => {
  return (
    product.value && product.value.compare_user.includes(store.userInfo.id)
  );
});
</script>

<style scoped></style>
