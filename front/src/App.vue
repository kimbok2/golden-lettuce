<template>
  <div>
    <NavigationBar />

    <main style="margin-top: 175px;">
      <!-- 창 크기 고정형 -->
      <div class="d-flex flex-row main-sheet justify-content-center">
        <div class="text-center" style="min-height: 800px; width:1000px;">
          <RouterView />
        </div>
      </div>
    </main>

    <Footer />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Chat from '@/components/Chat.vue'
import NavigationBar from '@/components/NavigationBar.vue'
import Footer from '@/components/Footer.vue'
</script>

<style scoped>
.main-sheet {
  margin: 0;
  width: 100%;
  max-width: 100% !important;
}
</style>
