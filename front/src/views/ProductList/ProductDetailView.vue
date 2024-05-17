<template>
  <div>
    <h1>ProductDetailView</h1>
    <hr />
    <div v-if="product">
      <h4>
        {{ product.fin_prdt_nm
        }}<button class="btn btn-primary">가입하기</button>
      </h4>
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
        <div v-if="product.depositoption_set">
          <ul class="text-start ps-0">
            <li class="card rounded-0">
              <div class="row m-0">
                <div class="col-3 text-center">저축기간</div>
                <div class="col-3 text-center">저축 금리</div>
                <div class="col-3 text-center">최고 우대 금리</div>
                <div class="col-3 text-center">저축금리 유형</div>
              </div>
            </li>
            <div>
              <div v-for="option in product.depositoption_set">
                <li class="card border border-0 border-bottom rounded-0">
                  <div class="row m-0">
                    <div class="col-3 text-center">{{ option.save_trm }}</div>
                    <div class="col-3 text-center">
                      {{ option.intr_rate }}
                    </div>
                    <div class="col-3 text-center">{{ option.intr_rate2 }}</div>
                    <div class="col-3 text-center">
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
import { RouterLink, RouterView, useRoute, useRouter } from "vue-router";
import { onMounted, computed, watch, ref } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const store = useUserStore();
const productType = ref(null);
const productId = ref(null);
const product = ref(null);
onMounted(() => {
  productType.value = route.params.type;
  productId.value = route.params.id;
  axios({
    method: "get",
    url: `${store.API_URL}/finances/get_${productType.value}/${productId.value}/`,
    // headers: {
    //   Authorization: `Token ${store.token}`,
    // },
  })
    .then((response) => {
      product.value = response.data;
    })
    .catch((err) => {
      console.log(err);
    });
});
const formatNumber = (value) => {
  if (typeof value !== "number") return "최고 한도 없음";
  return new Intl.NumberFormat().format(value);
};
</script>

<style scoped></style>
