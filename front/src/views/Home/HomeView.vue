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
              <h3>금상추가 추천하는 은행별 BEST 예금</h3>
              <BestDeposit />
            </div>
            <div class="min-col">
              <h3>금상추가 추천하는 은행별 BEST 적금</h3>
              <BestSaving />
            </div>
            <div class="min-col" style="height: auto;">
              <h3>금상추 커뮤니티</h3>
              <div class="tab-container d-flex justify-content-center">
                <button
                  class="btn tab-button"
                  id="category-tab"
                  @click="toggleType('notice')"
                  :class="{ active: selectedCategory === 'notice' }"
                  aria-controls="category-tab-pane"
                  :aria-selected="selectedCategory === 'notice'"
                  style="width: 33%"
                >
                  공지사항
                </button>
                <button
                  class="btn tab-button"
                  id="category-tab"
                  @click="toggleType('free')"
                  :class="{ active: selectedCategory === 'free' }"
                  aria-controls="category-tab-pane"
                  :aria-selected="selectedCategory === 'free'"
                  style="width: 33%"
                >
                  자유게시판
                </button>
                <button
                  class="btn tab-button"
                  id="category-tab"
                  @click="toggleType('faq')"
                  :class="{ active: selectedCategory === 'faq' }"
                  aria-controls="category-tab-pane"
                  :aria-selected="selectedCategory === 'faq'"
                  style="width: 33%"
                >
                  FAQ
                </button>
              </div>
              <table class="table">
                <thead>
                  <tr>
                    <th scope="col" style="width: 80%">제목</th>
                    <th scope="col" style="width: 20%">작성자</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="article in articles"
                    :key="article.id"
                    @click="toDetail({ name: 'community-detail', params: { id: article.id } })"
                  >
                    <td scope="col" style="width: 80%" class="text-start ps-5">
                      {{ article.content }}
                    </td>
                    <td scope="col" style="width: 80%">{{ article.user.nickname }}</td>
                  </tr>
                </tbody>
              </table>
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
                  <template v-if="store?.userInfo?.credit_score">
                    <DoughnutChart :score="store?.userInfo?.credit_score" />
                  </template>
                  <template v-else-if="store?.userInfo">
                    <DoughnutChart :score="store?.userInfo?.credit_score" />
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
              <div class="sub-col" style="height: auto">
                <RouterLink :to="{ name: 'exchange' }" class="text-decoration-none text-black">
                  <h5>환율 계산기</h5>
                  <img src="@/assets/exchange_rate_chart.png" alt="#" style="width: 100%; border-radius: 25px" />
                </RouterLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useCommunityStore } from '@/stores/community'
import DoughnutChart from '@/components/MyAccount/DoughnutChart.vue'
import BestDeposit from '@/components/BestDeposit.vue'
import BestSaving from '@/components/BestSaving.vue'

const router = useRouter()
const store = useUserStore()
const communityStore = useCommunityStore()
const userInfo = computed(() => store.userInfo)

const scrollElement = ref(null)
const scrollStyle = ref({ paddingTop: '0px' })
const threshold = 175 // 특정 값 (원하는 임계값을 설정하세요)
const maxScrollHeight = 500 // 페이지 최대 높이

// const documentHeight = ref(document.documentElement.scrollHeight)

const selectedCategory = ref('notice')

watch(
  () => communityStore.mainArticles,
  (newArticles) => {
    articles.value = newArticles
  }
)

const toggleType = (type) => {
  selectedCategory.value = type
  communityStore.getFiveArticleList(type)
}

const articles = ref([])

const toDetail = function (routerLink) {
  router.push(routerLink)
}

const handleScroll = () => {
  const offsetTop = scrollElement.value.getBoundingClientRect().top

  if (offsetTop < threshold) {
    const paddingTop = threshold - offsetTop
    if (paddingTop > 550) {
      return
    }
    scrollStyle.value = { paddingTop: `${paddingTop}px` }
  } else {
    scrollStyle.value = { paddingTop: '0px' }
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  communityStore.getFiveArticleList('notice')
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
  height: 310px;

  padding: 20px;

  border-radius: 10px;
  /* background-color: #f0f0f0; */

  /* opacity: 0.5; */

  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.sub-col {
  background-color: white;
  height: 200px;

  padding: 5px;
  padding-top: 10px;

  border-radius: 10px;

  /* opacity: 0.5; */

  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}

.tab-container {
  border-bottom: 1px solid #dee2e6;
}

.tab-button {
  border: 1px solid transparent;
  border-top-left-radius: 0.25rem;
  border-top-right-radius: 0.25rem;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
  margin-bottom: -1px;
  color: #868f08; /* 클릭되지 않은 탭의 글씨 색 파랑 */
  background-color: #fff; /* 탭 배경 흰색 */
  border-bottom: 1px solid #dee2e6; /* 클릭되지 않은 탭의 아래쪽 보더 */
  text-decoration: none;
  display: inline-block;
  padding: 0.5rem 1rem;
  text-align: center;
}

.tab-button.active {
  color: #000; /* 클릭된 탭의 글씨 색 검정 */
  background-color: #fff;
  border-color: #dee2e6 #dee2e6 #fff;
  border-bottom-color: transparent; /* 클릭된 탭의 아래쪽 보더 투명 */
}

.tab-button:hover {
  color: #939c1888; /* 호버 시 글씨 색 파랑 */
  text-decoration: none;
}
</style>
