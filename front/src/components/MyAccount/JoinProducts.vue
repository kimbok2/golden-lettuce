<template>
  <div>
    <h2 class="text-center mb-4">내가 가입한 상품</h2>
    <div
      class="d-flex justify-content-center mb-0 w-100 bg-white tab-container"
      role="tablist"
    >
      <div class="flex-fill text-center" role="presentation">
        <button
          class="w-100 btn tab-button"
          :class="{ active: selectedType === 'deposit' }"
          id="deposit-tab"
          @click="toggleType('deposit')"
          type="button"
          role="tab"
          aria-controls="deposit-tab-pane"
          :aria-selected="selectedType === 'deposit'"
        >
          예금 상품
        </button>
      </div>
      <div class="flex-fill text-center" role="presentation">
        <button
          class="w-100 btn tab-button"
          :class="{ active: selectedType === 'saving' }"
          id="saving-tab"
          @click="toggleType('saving')"
          type="button"
          role="tab"
          aria-controls="saving-tab-pane"
          :aria-selected="selectedType === 'saving'"
        >
          적금 상품
        </button>
      </div>
    </div>
    <div class="tab-content" id="productTabContent">
      <div
        class="tab-pane fade show active"
        id="carouselTabPane"
        role="tabpanel"
        aria-labelledby="carousel-tab"
      >
        <div id="carouselJoin" class="carousel slide no-top-border-radius">
          <div class="carousel-inner" @click="handleCarouselClick">
            <div v-if="!products.length" class="carousel-item active">
              <div class="card no-top-border-radius">
                <div class="card-body vertical-align">
                  <p>아직 가입 상품이 없어요...</p>
                  <p>가입 상품을 찾으러 가보시겠어요?</p>
                  <RouterLink :to="{ name: 'products' }" class="btn btn-warning"
                    >상품 찾으러 가기</RouterLink
                  >
                </div>
              </div>
            </div>
            <div
              v-for="(product, index) in products"
              :key="product.id"
              class="carousel-item"
              :class="{ active: index === activeIndex }"
            >
              <div class="card no-top-border-radius">
                <div class="card-body">
                  <h5 class="card-title"><br />{{ product.fin_prdt_nm }}</h5>
                  <p class="card-text">{{ product.kor_co_nm }}</p>
                  <p class="card-text">
                    {{
                      product.max_limit
                        ? "최고 한도:" + formatNumber(product.max_limit) + "원"
                        : "최고 한도가 없는 상품입니다."
                    }}
                  </p>
                  <p class="card-text">
                    저축 금리: {{ getInterestRate(product, "intr_rate") }}%
                  </p>
                  <p class="card-text">
                    최고 우대 금리:
                    {{ getInterestRate(product, "intr_rate2") }}%
                  </p>
                  <RouterLink
                    :to="{
                      name: 'products-detail',
                      params: { id: product.id, type: selectedType },
                    }"
                    class="btn btn-warning"
                  >
                    상세 보기
                  </RouterLink>
                </div>
              </div>
            </div>
          </div>
          <button
            class="carousel-control-prev"
            type="button"
            data-bs-target="#carouselJoin"
            data-bs-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button
            class="carousel-control-next"
            type="button"
            data-bs-target="#carouselJoin"
            data-bs-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter, RouterLink } from "vue-router";

const store = useUserStore();
const selectedType = ref("deposit"); // 초기값을 'deposit'으로 설정
const products = ref([]);
const activeIndex = ref(0); // 활성 슬라이드 인덱스

onMounted(() => {
  store.getUserInfo()
})

// watch를 사용하여 userInfo가 변경될 때마다 제품 목록을 업데이트합니다.
watch(
  () => store.userInfo,
  (newUserInfo) => {
    if (selectedType.value === "deposit") {
      products.value = newUserInfo.join_deposit || [];
    } else if (selectedType.value === "saving") {
      products.value = newUserInfo.join_saving || [];
    }
    activeIndex.value = 0; // 슬라이드 인덱스를 초기화합니다.
  },
  { immediate: true, deep: true } // 즉시 실행하여 초기값도 반영되도록 하고, deep 옵션 추가
);

// watch를 사용하여 selectedType이 변경될 때마다 제품 목록을 업데이트합니다.
watch(
  selectedType,
  () => {
    if (selectedType.value === "deposit") {
      products.value = store.userInfo.join_deposit || [];
    } else if (selectedType.value === "saving") {
      products.value = store.userInfo.join_saving || [];
    }
    activeIndex.value = 0; // 슬라이드 인덱스를 초기화합니다.
  },
  { immediate: true } // 즉시 실행하여 초기값도 반영되도록 합니다.
);

const toggleType = (type) => {
  selectedType.value = type;
};

const formatNumber = (value) => {
  if (typeof value !== "number") return "";
  return new Intl.NumberFormat().format(value);
};

// 특정 금리를 반환하는 함수
const getInterestRate = (product, rateType) => {
  let options;
  if (selectedType.value === "deposit") {
    options = product.depositoption_set;
  } else if (selectedType.value === "saving") {
    options = product.savingoption_set;
  }
  if (options && options.length > 0) {
    return options[0][rateType]; // 예를 들어 첫 번째 옵션을 사용
  }
  return "N/A";
};

const handleCarouselClick = (event) => {
  const carousel = document.getElementById("carouselJoin");
  const rect = carousel.getBoundingClientRect();
  const clickX = event.clientX - rect.left;
  const third = rect.width / 3;

  if (clickX < third) {
    carousel.querySelector(".carousel-control-prev").click();
  } else if (clickX > 2 * third) {
    carousel.querySelector(".carousel-control-next").click();
  }
};
</script>

<style scoped>
.tab-container {
  border-bottom: 1px solid #dee2e6;
}

.tab-button {
  border: 1px solid transparent;
  border-top-left-radius: 0.25rem;
  border-top-right-radius: 0.25rem;
  border-bottom-left-radius: 0; /* 아래쪽 왼쪽 모서리 둥글지 않게 */
  border-bottom-right-radius: 0; /* 아래쪽 오른쪽 모서리 둥글지 않게 */
  margin-bottom: -1px;
  color: rgba(151, 151, 88, 0.822); /* 클릭되지 않은 탭의 글씨 색 파랑 */
  background-color: #fff; /* 탭 배경 흰색 */
  border-bottom: 1px solid #dee2e6; /* 클릭되지 않은 탭의 아래쪽 보더 */
}

.tab-button.active {
  color: #000; /* 클릭된 탭의 글씨 색 검정 */
  background-color: #fff;
  border-color: #dee2e6 #dee2e6 #fff;
  border-bottom-color: transparent; /* 클릭된 탭의 아래쪽 보더 투명 */
}

.tab-button:hover {
  color: rgba(173, 173, 44, 0.822); /* 호버 시 글씨 색 파랑 */
}

.no-top-border-radius {
  border-top-left-radius: 0 !important;
  border-top-right-radius: 0 !important;
}

.carousel-container {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.carousel-wrapper {
  width: 100%;
  overflow: hidden;
}

.carousel {
  display: flex;
  transition: transform 0.5s ease;
}

.carousel-item {
  flex: 0 0 100%;
  max-width: 100%;
}

.carousel-item.active {
  opacity: 1;
  transform: scale(1);
}

.carousel-item .card {
  height: 100%;
  border-top: 0; /* 윗 부분에 border 없애기 */
  border-top-left-radius: 0; /* 위쪽 왼쪽 모서리 둥글지 않게 */
  border-top-right-radius: 0; /* 위쪽 오른쪽 모서리 둥글지 않게 */
}

.carousel-control-prev,
.carousel-control-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: transparent; /* 배경 투명 */
  color: gray; /* 화살표 색깔 회색 */
  border: none;
  font-size: 2rem;
  cursor: pointer;
  z-index: 10;
  width: 5%;
  height: 100%;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-image: none; /* 기본 아이콘 이미지 제거 */
  border-radius: 10px;
  display: inline-block;
  width: 30px;
  height: 30px;
}

.carousel-control-prev-icon::after {
  content: "‹"; /* 화살표 기호 */
  color: gray; /* 화살표 색깔 회색 */
  font-size: 30px;
  line-height: 30px;
}

.carousel-control-next-icon::after {
  content: "›"; /* 화살표 기호 */
  color: gray; /* 화살표 색깔 회색 */
  font-size: 30px;
  line-height: 30px;
}

.btn.active {
  background-color: white;
  color: black;
}
.card-body {
  height: 310px;
}
.vertical-align {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
