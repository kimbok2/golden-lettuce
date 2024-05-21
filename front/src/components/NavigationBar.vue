<template>
  <nav class="fixed-top row" style="background-color: #ffcd39">
    <RouterLink to="/" class="col-1 d-flex align-items-center justify-content-center">
      <img src="@/assets/LOGO_GL.png" alt="Logo" style="height: 100px" class="logo-gl"/>
    </RouterLink>
    <div class="col-10">
      <div class="d-flex justify-content-between align-items-center pe-2" id="navbarNav" style="height: 50px">
        <div style="width: 300px"></div>
        <div>
          <div class="input-group mt-4">
            <input class="form-control text-center" type="text" style="width: 500px" placeholder="금상추와 대화하기" />
            <span class="material-symbols-outlined ms-3" style="font-size: 50px"> chat </span>
          </div>
        </div>
        <!-- 프로필 관련 버튼 목록 -->
        <div>
          <template class="nav-item" v-for="navProfileItem in navProfileItems" :key="navProfileItem.id">
            <RouterLink v-if="isLogin === navProfileItem.isLogin" :to="{ name: navProfileItem.name }">
              <button
                type="button"
                class="btn m-1 btn-secondary d-inline-flex align-items-center"
                :class="{ rounded: navProfileItem.isLogin }"
              >
                <a class="nav-link d-inline-flex align-items-center" href="#" v-html="navProfileItem.itemName"></a>
              </button>
            </RouterLink>
          </template>

          <!-- 로그아웃 버튼 반복문 밖에 별도 생성 -->
          <button @click="userStore.logOut" v-if="isLogin" type="button" class="btn m-1 btn-secondary">
            <a class="nav-link" href="#">로그아웃</a>
          </button>
        </div>
      </div>

      <div class="container-fluid my-0 d-flex justify-content-between" style="height: 100px">
        <!-- 네비게이션 버튼 목록 -->
        <div></div>
        <div class="d-flex align-items-center">
          <!-- <div style="background-color: #ffcd39" class="d-flex align-items-center"> -->
          <template class="" v-for="navItem in navItems" :key="navItem.id">
            <RouterLink :to="{ name: navItem.name }">
              <button type="button" class="nav-item btn btn-lg m-1 btn-outline-warning text-dark" style="">
                <a class="nav-link single-line-text" href="#">{{ navItem.itemName }}</a>
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
  {
    id: item_id++,
    itemName: '<span class="material-symbols-outlined">person</span><span class="ms-2">  내 프로필</span>',
    name: 'profile',
    isMain: false,
    isLogin: true,
  },
  { id: item_id++, itemName: '로그인', name: 'login', isMain: false, isLogin: false },
  { id: item_id++, itemName: '회원가입', name: 'signup', isMain: false, isLogin: false },
])

onMounted(() => {
  isLogin.value = userStore.isLogin
})
</script>

<style scoped>
.form-control {
  border-radius: 20px !important;
}


.material-symbols-outlined {
  color: #333;
}


.material-symbols-outlined:hover {
  color: #ffffff;
}
</style>
