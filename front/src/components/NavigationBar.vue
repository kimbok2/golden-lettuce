<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <RouterLink to="/">
          <img src="@/assets/LOGO_GL.png" alt="Logo" width="50" height="50" class="d-inline-block align-text-top" />
        </RouterLink>
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- 네비게이션 버튼 목록 -->
      <div class="collapse navbar-collapse justify-content-center" id="navbarNav">
        <template class="nav-item" v-for="navItem in navItems" :key="navItem.id">
          <RouterLink :to="{ name: navItem.name }">
            <button type="button" class="btn  m-1" :class="{ 'btn-warning': navItem.isMain, 'btn-secondary': !navItem.isMain }">
              <a class="nav-link" href="#">{{ navItem.itemName }}</a>
            </button>
          </RouterLink>
        </template>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

// 네비게이션바 버튼 목록 정보 저장
// id : 1 ~
// itemName : 버튼에 작성할 이름
// itemLink : RouterLink 시킬 url name
let item_id = 1

const navItems = ref([
  { id: item_id++, itemName: '상품 검색', name: 'products', isMain : true },
  { id: item_id++, itemName: '상품 비교', name: 'compare', isMain : true },
  { id: item_id++, itemName: '상품 커뮤니티', name: 'community', isMain : true },
  { id: item_id++, itemName: '내 주변 은행 찾기', name: 'maps', isMain : true },
  { id: item_id++, itemName: '환율 계산기', name: 'exchange', isMain : true },
  { id: item_id++, itemName: '내 정보', name: 'user', isMain : true },
  { id: item_id++, itemName: '프로필', name: 'profile', isMain : false },
  { id: item_id++, itemName: '로그인', name: 'login', isMain : false },
  { id: item_id++, itemName: '회원가입', name: 'signup', isMain : false },
])
</script>

<style scoped></style>
