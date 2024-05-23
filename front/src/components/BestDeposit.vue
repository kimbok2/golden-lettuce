<template>
  <div>
    <div class="tab-content" id="productTabContent">
      <div
        class="tab-pane fade show active"
        id="carouselTabPane"
        role="tabpanel"
        aria-labelledby="carousel-tab"
      >
        <div id="carouselDeposit" class="carousel slide no-top-border-radius">
          <div class="carousel-inner" @click="handleCarouselClick">
            <div v-if="!bankInfos.length" class="carousel-item active">
              <div class="card no-top-border-radius">
                <div class="card-body vertical-align">
                  <p>아무도 상품에 가입하지 않았어요...</p>
                  <p>가입할 상품을 찾으러 가보시겠어요?</p>
                  <RouterLink :to="{ name: 'products' }" class="btn btn-warning"
                    >상품 찾으러 가기</RouterLink
                  >
                </div>
              </div>
            </div>
            <div
              v-for="(bank, index) in bankInfos"
              :key="bank.id"
              class="carousel-item"
              :class="{ active: index === activeIndex }"
            >
              <div class="card no-top-border-radius">
                <div class="card-body vertical-align">
                  
                  <h4 class="card-title">
                    <RouterLink :to="{name : 'bank-detail', params : {id : bank.bank_id} }"
                    class="custom-link">
                    <img :src="`/media/bank/${bank.bank_id}.png`" alt="이미지">
                    {{ bank.bank_name }}</RouterLink>
                </h4>
                  <h6 class="card-text">{{ bank.top_deposit_product.fin_prdt_nm }}</h6>
                  <p class="card-text">가입자 수 : {{ bank.top_deposit_product.user_count }}명</p>
                  <p class="card-text">
                    
                  </p>
                 
                  <RouterLink
                    :to="{
                      name: 'products-detail',
                      params: { id: bank.top_deposit_product.id, type: 'deposit' },
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
            data-bs-target="#carouselDeposit"
            data-bs-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button
            class="carousel-control-next"
            type="button"
            data-bs-target="#carouselDeposit"
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
import { ref, watch, computed, onMounted, onUnmounted } from "vue";
import { useBankStore } from "@/stores/bank";
import { useRouter, RouterLink } from "vue-router";

const bankStore = useBankStore()
const activeIndex = ref(0); // 활성 슬라이드 인덱스

// 은행 목록 저장
let i = 1
const banks = [
  { id: i++, name: '우리은행', keyword: '우리' },
  { id: i++, name: '한국스탠다드차타드은행', keyword: '제일은행' },
  { id: i++, name: '대구은행', keyword: '대구은행' },
  { id: i++, name: '부산은행', keyword: '부산은행' },
  { id: i++, name: '광주은행', keyword: '광주은행' },
  { id: i++, name: '제주은행', keyword: '제주은행' },
  { id: i++, name: '전북은행', keyword: '전북은행' },
  { id: i++, name: '경남은행', keyword: '경남은행' },
  { id: i++, name: '중소기업은행', keyword: '기업' },
  { id: i++, name: '한국산업은행', keyword: '산업' },
  { id: i++, name: '국민은행', keyword: '국민은행' },
  { id: i++, name: '신한은행', keyword: '신한은행' },
  { id: i++, name: '농협은행주식회사', keyword: '농협' },
  { id: i++, name: '하나은행', keyword: '하나은행' },
  { id: i++, name: '주식회사 케이뱅크', keyword: '케이뱅크' },
  { id: i++, name: '수협은행', keyword: '수협' },
  { id: i++, name: '주식회사 카카오뱅크', keyword: '카카오' },
  { id: i++, name: '토스뱅크 주식회사', keyword: '토스' },
]

const bankInfos = computed(() => {
  return bankStore.banks.map(bank => {
    const bankInfo = banks.find(b => b.id === bank.bank_id);
    return {
      ...bank,
      bank_name: bankInfo ? bankInfo.name : "알 수 없음"
    };
  });
});

// 진입 시 bank 데이터 불러오기
onMounted(() => {
    bankStore.fetchBankDatas()
})

const handleCarouselClick = (event) => {
  const carousel = document.getElementById("carouselDeposit");
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
.carousel-inner {
  min-height: 200px;
}
.card-body {
  height: 220px;
}
.vertical-align {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.custom-link {
  color: inherit; /* 부모 요소의 색상 상속 */
  text-decoration: none; /* 밑줄 제거 */
}
.custom-link:hover {
  color: gray; /* 호버 시 색상 변경 (원하는 색상으로 변경 가능) */
}
</style>
