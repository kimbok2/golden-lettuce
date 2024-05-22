<template>
  <div class="container mt-4">
    <div v-if="product" class="card">
      <div class="card-body">
        <h4 class="card-title">{{ product.fin_prdt_nm }}</h4>
        <div class="d-flex justify-content-between align-items-center mb-3">
          <span class="badge bg-secondary"
            >가입자 수 : {{ product.join_user_count }}명</span
          >
          <div>
            <button
              v-if="!isUserJoined"
              @click="joinProduct('post')"
              class="btn btn-primary mx-2"
            >
              가입하기
            </button>
            <button
              v-else
              @click="joinProduct('delete')"
              class="btn btn-danger mx-2"
            >
              해지하기
            </button>
            <button
              v-if="!isUserCompared"
              @click="compareProduct('post')"
              class="btn btn-outline-primary mx-2"
            >
              비교 등록
            </button>
            <button
              v-else
              @click="compareProduct('delete')"
              class="btn btn-outline-danger mx-2"
            >
              비교 해제
            </button>
          </div>
        </div>
        <hr />
        <div class="product-details">
          <div class="detail-item">
            <h5 class="detail-title">담당 회사</h5>
            <p class="detail-content">
              <RouterLink
                :to="{ name: 'bank-detail', params: { id: product.bank } }"
                class="custom-link"
              >
                <img :src="`/media/bank/${product.bank}.png`" alt="" />
                {{ product.kor_co_nm }}
              </RouterLink>
            </p>
          </div>
          <div class="detail-item">
            <h5 class="detail-title">공시제출월</h5>
            <p class="detail-content">
              {{ product.dcls_month.substring(0, 4) }}년
              {{ product.dcls_month.substring(5) }}월
            </p>
          </div>
          <div class="detail-item">
            <h5 class="detail-title">공시시작일</h5>
            <p class="detail-content">
              {{
                formattedDate(product.dcls_strt_day, "공시 시작일 정보 없음")
              }}
            </p>
          </div>
          <div class="detail-item">
            <h5 class="detail-title">공시종료일</h5>
            <p class="detail-content">
              {{ formattedEndDate(product.dcls_end_day) }}
            </p>
          </div>
          <div class="detail-item">
            <h5 class="detail-title">가입 방법</h5>
            <p class="detail-content">{{ product.join_way }}</p>
          </div>
          <div class="detail-item">
            <h5 class="detail-title">가입 대상</h5>
            <p class="detail-content">{{ product.join_member }}</p>
          </div>
          <div class="detail-item">
            <h5 class="detail-title">최고 한도</h5>
            <p class="detail-content">
              {{
                product.max_limit
                  ? formatNumber(product.max_limit) + " 원"
                  : "최고 한도가 없는 상품입니다."
              }}
            </p>
          </div>
          <div class="detail-item">
            <h5 class="detail-title">우대 조건</h5>
            <p class="detail-content">{{ product.spcl_cnd }}</p>
          </div>
          <div class="detail-item">
            <h5 class="detail-title">만기 후 이자율</h5>
            <p class="detail-content">{{ product.mtrt_int }}</p>
          </div>
          <div class="detail-item">
            <h5 class="detail-title">유의사항</h5>
            <p class="detail-content">{{ product.etc_note }}</p>
          </div>
        </div>

        <div class="mt-4">
          <h5 class="card-subtitle mb-3">옵션 정보</h5>
          <div class="table-responsive">
            <table class="table table-bordered">
              <thead>
                <tr>
                  <th scope="col" class="text-center">번호</th>
                  <th scope="col" class="text-center">저축기간</th>
                  <th scope="col" class="text-center">저축 금리</th>
                  <th scope="col" class="text-center">최고 우대 금리</th>
                  <th scope="col" class="text-center">저축금리 유형</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(option, index) in productOptions" :key="option.id">
                  <th scope="row" class="text-center">{{ index + 1 }}</th>
                  <td class="text-center">{{ option.save_trm }}</td>
                  <td class="text-center">{{ option.intr_rate }}</td>
                  <td class="text-center">{{ option.intr_rate2 }}</td>
                  <td class="text-center">{{ option.intr_rate_type_nm }}</td>
                </tr>
              </tbody>
            </table>
          </div>
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
  const joinOrNot = ref(null);
  if (apiMethod === "post") {
    joinOrNot.value = window.confirm("가입하시겠습니까?");
  } else {
    joinOrNot.value = window.confirm("정말 해지하시겠습니까?");
  }
  if (joinOrNot.value === true) {
    axios({
      method: apiMethod,
      url: `${store.API_URL}/finances/join_${productType.value}/${productId.value}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then((res) => {
        if (apiMethod === "post") {
          alert("성공적으로 가입되었어요.");
        } else {
          alert("해지가 완료되었어요.");
        }
        console.log("가입/해지");
        fetchProduct(); // 업데이트 후 데이터를 다시 가져옴
      })
      .catch((err) => {
        console.log(err);
      });
  }
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

const productOptions = computed(() => {
  if (route.params.type === "deposit") {
    return product.value ? product.value.depositoption_set : [];
  } else if (route.params.type === "saving") {
    return product.value ? product.value.savingoption_set : [];
  }
  return [];
});

const formattedDate = (date, defaultText) => {
  if (!date) return defaultText;
  return date.replace(/(\d{4})(\d{2})(\d{2})/, "$1-$2-$3");
};

const formattedEndDate = (date) => {
  if (!date || date === "99991231") return "공시 종료일 미정";
  return formattedDate(date, "공시 종료일 정보 없음");
};
</script>

<style scoped>
.card {
  border: 1px solid #e2e2e2;
  border-radius: 0.5rem;
}

.card-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.card-subtitle {
  font-size: 1.25rem;
  font-weight: bold;
}

.product-details {
  margin-top: 1rem;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #e2e2e2;
  align-items: center;
  padding: 12px 0;
}

.detail-title {
  flex: 1;

  margin: 8px 0;
}

.detail-content {
  flex: 2;
  margin: 8px 0;
}
.table {
  margin-top: 1rem;
}

.table th,
.table td {
  vertical-align: middle;
}
.custom-link {
  color: inherit; /* 부모 요소의 색상 상속 */
  text-decoration: none; /* 밑줄 제거 */
}
.custom-link:hover {
  color: gray; /* 호버 시 색상 변경 (원하는 색상으로 변경 가능) */
}
</style>
