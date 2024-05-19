<template>
  <nav class="fixed-top" style="background-color: #ffcd39">
    <div class="d-flex justify-content-end align-items-center pe-2" id="navbarNav" style="height: 50px">
      <span class="material-symbols-outlined" style="font-size: 50px"> search </span>
      <!-- 프로필 관련 버튼 목록 -->
      <template class="nav-item" v-for="navProfileItem in navProfileItems" :key="navProfileItem.id">
        <RouterLink v-if="isLogin === navProfileItem.isLogin" :to="{ name: navProfileItem.name }">
          <button type="button" class="btn m-1 btn-secondary d-inline-flex align-items-center" :class="{'rounded': navProfileItem.isLogin}">
            <a class="nav-link d-inline-flex align-items-center" href="#" v-html="navProfileItem.itemName"></a>
          </button>
        </RouterLink>
      </template>
      <!-- 로그아웃 버튼 반복문 밖에 별도 생성 -->
      <button @click="userStore.logOut" v-if="isLogin" type="button" class="btn m-1 btn-secondary">
        <a class="nav-link" href="#">로그아웃</a>
      </button>
    </div>

    <div class="p-0">
      <div class="container-fluid my-0 d-flex justify-content-between" style="height: 100px">
          <RouterLink to="/" class="d-flex align-items-center">
            <img src="@/assets/LOGO_GL.png" alt="Logo" style="height: 75px" />
          </RouterLink>

        <!-- 네비게이션 버튼 목록 -->
          <div style="background-color: #ffcd39" class="d-flex align-items-center">
            <template class="" v-for="navItem in navItems" :key="navItem.id">
              <RouterLink :to="{ name: navItem.name }">
                <button type="button" class="nav-item btn btn-lg m-1 btn-outline-warning text-dark" style="">
                  <a class="nav-link" href="#">{{ navItem.itemName }}</a>
                </button>
              </RouterLink>
            </template>
          </div>
          <!-- 빈 태그 생성 -->
          <div></div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// 현재 유저 로그인 여부 확인
const isLogin = ref(null)
watch(
  () => userStore.isLogin,
  (newIsLogin) => {
    isLogin.value = newIsLogin
  }
)

// 네비게이션바 버튼 목록 정보 저장
// id : 1 ~
// itemName : 버튼에 작성할 이름
// itemLink : RouterLink 시킬 url name
let item_id = 1

const navItems = ref([
  { id: item_id++, itemName: '상품 검색', name: 'products', isMain: true },
  { id: item_id++, itemName: '상품 비교', name: 'compare', isMain: true },
  { id: item_id++, itemName: '커뮤니티', name: 'community', isMain: true },
  { id: item_id++, itemName: '은행 찾기', name: 'maps', isMain: true },
  { id: item_id++, itemName: '환율 계산', name: 'exchange', isMain: true },
  { id: item_id++, itemName: '나의 정보', name: 'user', isMain: true },
])

const navProfileItems = ref([
  { id: item_id++, itemName: '<span class="material-symbols-outlined">person</span><span class="ms-2">  내 프로필</span>', name: 'profile', isMain: false, isLogin: true },
  // { id: item_id++, itemName: '로그아웃', name: 'logOut', isMain: false, isLogin: true },
  { id: item_id++, itemName: '로그인', name: 'login', isMain: false, isLogin: false },
  { id: item_id++, itemName: '회원가입', name: 'signup', isMain: false, isLogin: false },
])

onMounted(() => {
  isLogin.value = userStore.isLogin
})
</script>

<style scoped></style>
