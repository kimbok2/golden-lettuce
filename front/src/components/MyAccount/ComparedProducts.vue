<template>
  <div>
    <h2 class="text-center mb-4">관심 있는 상품</h2>
    <div class="text-center mb-3">
      <button
        @click="toggleType('deposit')"
        :class="{ active: selectedType === 'deposit' }"
        class="btn btn-outline-primary mx-1"
      >
        예금 상품
      </button>
      <button
        @click="toggleType('saving')"
        :class="{ active: selectedType === 'saving' }"
        class="btn btn-outline-primary mx-1"
      >
        적금 상품
      </button>
    </div>
    <div id="carouselCompare" class="carousel slide">
      <div class="carousel-inner">
        <div
          v-for="(product, index) in products"
          :key="product.id"
          class="carousel-item"
          :class="{ active: index === activeIndex }"
        >
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">{{ product.fin_prdt_nm }}</h5>
              <p class="card-text">{{ product.kor_co_nm }}</p>
              <p class="card-text">
                최고 한도:
                {{
                  product.max_limit
                    ? formatNumber(product.max_limit) + "원"
                    : "최고 한도가 없는 상품입니다."
                }}
              </p>
              <p class="card-text">
                저축 금리: {{ getInterestRate(product, "intr_rate") }}%
              </p>
              <p class="card-text">
                최고 우대 금리: {{ getInterestRate(product, "intr_rate2") }}%
              </p>
              <RouterLink
                :to="{
                  name: 'products-detail',
                  params: { id: product.id, type: selectedType },
                }"
                class="btn btn-primary"
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
        data-bs-target="#carouselCompare"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselCompare"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter, RouterLink } from "vue-router";

const store = useUserStore();
const router = useRouter();
const selectedType = ref("deposit"); // 초기값을 'deposit'으로 설정
const products = ref([]);
const activeIndex = ref(0); // 활성 슬라이드 인덱스

// watch를 사용하여 selectedType이 변경될 때마다 제품 목록을 업데이트합니다.
watch(
  selectedType,
  () => {
    if (selectedType.value === "deposit") {
      products.value = store.userInfo.compare_deposit || [];
    } else if (selectedType.value === "saving") {
      products.value = store.userInfo.compare_saving || [];
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
</script>

<style scoped>
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
}

.carousel-control-prev,
.carousel-control-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  z-index: 10;
  width: 5%;
  height: 100%;
}

.carousel-control-prev {
  left: 0;
}

.carousel-control-next {
  right: 0;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-size: 100%, 100%;
}

.btn.active {
  background-color: #007bff;
  color: white;
}
</style>
