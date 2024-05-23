<template>
  <footer class="">
    <div>
      <img src="@/assets/LOGO_LITE.png" alt="" class="bot-logo" />
      <p>Copyright Golden Lettuce. All Rights Reserved.</p>
    </div>
    <div class="d-flex align-items-center">
      <span class="material-symbols-outlined ms-2"> list_alt </span>
      <template v-for="navItem in navItems" :key="navItem.id">
        <RouterLink :to="{ name: navItem.name }">
          <button class="btn footer-button">
            {{ navItem.itemName }}
          </button>
        </RouterLink>
      </template>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'

let item_id = 0
const navItems = ref([
  { id: item_id++, itemName: '상품 검색', name: 'products', isMain: true },
  { id: item_id++, itemName: '상품 비교', name: 'compare', isMain: true },
  { id: item_id++, itemName: '커뮤니티', name: 'community', isMain: true },
  { id: item_id++, itemName: '은행 찾기', name: 'maps', isMain: true },
  { id: item_id++, itemName: '환율 계산', name: 'exchange', isMain: true },
  { id: item_id++, itemName: '나의 정보', name: 'user', isMain: true },
])
</script>

<style scoped>
footer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 200px;
  text-align: center;

  background-color: rgb(255, 255, 220);
}

.bot-logo {
  width: 30px;
}

.footer-button {
  transition: 0.5s ease !important;
}

.footer-button:hover {
  transform: scale(1.2);
}
</style>
