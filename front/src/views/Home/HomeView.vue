<template>
  <div>
    <h1 class="main-h1-container">
      <span>메인 페이지</span>
      <span class="material-symbols-outlined"> domain </span>
    </h1>

    <main class="main-container container">
      <div class="row">
        <div class="col-7 p-3 main-column">
          <h1>Main Column</h1>
          <div class="row g-3 m-3">
            <div class="min-col"></div>
            <div class="min-col"></div>
            <div class="min-col"></div>
          </div>
        </div>
        <div class="col-5 p-3">
          <div class="row g-3 m-3">
            <h1>Sub Column</h1>
            <div class="col-6">
              <div class="min-col"></div>
            </div>
            <div class="col-6">
              <div class="min-col"></div>
            </div>
            <div class="col-12">
              <div class="min-col"></div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup></script>

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
  border-radius: 10px;
  background-color: #f0f0f0;

  opacity: 0.5;

  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
</style>
