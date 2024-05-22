<template>
  <div>
    <h1 class="main-h1-container">
      <span>메인 페이지</span>
      <span class="material-symbols-outlined"> domain </span>
    </h1>

    <main class="main-container container py-3">
      <div class="row">
        <div class="col-7 p-3 main-column">
          <h3>주 기능<span class="material-symbols-outlined ms-2"> category </span></h3>
          <div class="row g-3 m-3">
            <div class="min-col">
              <h3>금상추 이용자를 위한 Best 추천 상품</h3>
            </div>
            <div class="min-col"></div>
            <div class="min-col">
              <h3>금상추 커뮤니티</h3>
            </div>
          </div>
        </div>
        <div class="col-5" ref="scrollElement" :style="scrollStyle">
          <div class="row g-4 mx-2">
            <h5>
              바로가기
              <span class="material-symbols-outlined ms-2"> shortcut </span>
            </h5>
            <div class="col-6">
              <RouterLink :to="{ name: 'maps' }" class="text-decoration-none text-black">
                <div class="sub-col">
                  <h5>은행 지도</h5>
                  <img src="@/assets/mainpage_map_img.png" alt="#" style="width: 95%; border-radius: 25px" />
                </div>
              </RouterLink>
            </div>
            <div class="col-6">
              <div class="sub-col">
                <RouterLink :to="{ name: 'user' }" class="text-decoration-none text-black">
                  <h5>나의 정보</h5>
                  <template v-if="store.userInfo.credit_score">
                    <DoughnutChart :score="userInfo.credit_score" />
                  </template>
                  <template v-else-if="store.userInfo">
                    <DoughnutChart :score="userInfo.credit_score" />
                  </template>
                  <template v-else>
                    <div class="d-flex align-items-center justify-content-center" style="height: 150px">
                      <div style="margin-bottom: 50px">
                        로그인이<br />
                        필요한 서비스에요
                      </div>
                    </div>
                  </template>
                </RouterLink>
              </div>
            </div>
            <div class="col-12">
              <div class="sub-col" style="height: 275px">
                <RouterLink :to="{ name: 'exchange' }" class="text-decoration-none text-black">
                  <h5>환율 계산기</h5></RouterLink
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useUserStore } from '@/stores/user'
import DoughnutChart from '@/components/MyAccount/DoughnutChart.vue'

const store = useUserStore()
const userInfo = computed(() => store.userInfo)

const scrollElement = ref(null)
const scrollStyle = ref({ paddingTop: '0px' })
const threshold = 175 // 특정 값 (원하는 임계값을 설정하세요)

const handleScroll = () => {
  const offsetTop = scrollElement.value.getBoundingClientRect().top

  if (offsetTop < threshold) {
    const paddingTop = threshold - offsetTop
    scrollStyle.value = { paddingTop: `${paddingTop}px` }
  } else {
    scrollStyle.value = { paddingTop: '0px' }
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.main-container {
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.main-column {
  min-height: 1000px;
}

.min-col {
  height: 300px;

  padding: 20px;

  border-radius: 10px;
  /* background-color: #f0f0f0; */

  /* opacity: 0.5; */

  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.sub-col {
  height: 200px;

  padding: 5px;
  padding-top: 10px;

  border-radius: 10px;

  /* opacity: 0.5; */

  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}
</style>
