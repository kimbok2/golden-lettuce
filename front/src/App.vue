<template>
  <div>
    <header>
      <NavigationBar />
    </header>

    <main>
      <div class="container main-sheet">
        <div class="row text-center">
          <div class="col-2 side-col">col1</div>
          <div class="col-8 main-col">
            Col - Main
            <RouterLink to="/">Home</RouterLink>
            <RouterView />
          </div>
        <div class="col-2 side-col">col2</div>
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
  min-height: 1200px;
  margin: 0;
  width: 100%;
  max-width: 100% !important;
}

.main-col {
}

.side-col {
  min-height: 1200px;
}
</style>
