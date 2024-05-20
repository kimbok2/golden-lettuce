<template>
  <div>
    <h2 class="text-center mb-4">비교할 상품</h2>
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
    <div class="carousel-container">
      <button class="carousel-btn prev" @click="prevSlide">‹</button>
      <div class="carousel-wrapper">
        <div class="carousel" :style="carouselStyle">
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
                  최고 한도: {{ formatNumber(product.max_limit) }}원
                </p>
                <p class="card-text">저축 금리: {{ product.intr_rate }}%</p>
                <p class="card-text">
                  최고 우대 금리: {{ product.intr_rate2 }}%
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
      </div>
      <button class="carousel-btn next" @click="nextSlide">›</button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed } from "vue";
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

const nextSlide = () => {
  if (activeIndex.value < products.value.length - 1) {
    activeIndex.value++;
  } else {
    activeIndex.value = 0;
  }
};

const prevSlide = () => {
  if (activeIndex.value > 0) {
    activeIndex.value--;
  } else {
    activeIndex.value = products.value.length - 1;
  }
};

const carouselStyle = computed(() => {
  return {
    transform: `translateX(-${activeIndex.value * 100}%)`,
    transition: "transform 0.5s ease",
  };
});
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
  box-sizing: border-box;
  padding: 0 10px;
}
.carousel-item .card {
  height: 100%;
}

.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  z-index: 10;
}

.carousel-btn.prev {
  left: 0;
}

.carousel-btn.next {
  right: 0;
}

.btn.active {
  background-color: #007bff;
  color: white;
}
</style>
