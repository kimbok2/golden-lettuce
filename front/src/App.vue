<template>
  <div>
    <NavigationBar />

    <main style="margin-top: 175px;">
      <!-- 창 크기 고정형 -->
      <div class="d-flex flex-column main-sheet justify-content-center align-items-center">
        <div class="text-center" style="min-height: 800px; width:1000px">
          <RouterView />
        </div>
      </div>
      <!-- 반응형 -->
      <!-- <div class="container main-sheet">
        <div class="row text-center" style="min-height: 1000px">
          <div class="col-3 side-col">
          </div>
          <div class="col-6 main-col border">
            <RouterView />
          </div>
          <div class="col-3 side-col">
          </div>
        </div>
      </div> -->
    </main>

    <Footer />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
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
