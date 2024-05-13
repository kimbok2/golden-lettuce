<template>
  <div>
    <header>
      <NavigationBar />
    </header>

    <main>
      <div class="container main-sheet">
        <div class="row text-center" style="min-height: 1000px">
          <div class="col-2 side-col border">
            <h1>Left Column</h1>
          </div>
          <div class="col-8 main-col border">
            <RouterView />
          </div>
          <div class="col-2 side-col border">
            <h1>Right Column</h1>
          </div>
        </div>
      </div>
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
