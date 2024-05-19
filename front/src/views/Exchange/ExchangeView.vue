<template>
  <div>
    <h1>환율 계산</h1>
    <div class="exchange-container">
      <div class="exchange-box">
        <ExchangeList />
      </div>
    </div>
    <div class="exchange-container">
      <div class="exchange-box">
        <ExchangeGraph />
      </div>
    </div>
  </div>
</template>

<script setup>
import ExchangeList from '@/components/Exchange/ExchangeList.vue'
import ExchangeGraph from '@/components/Exchange/ExchangeGraph.vue';
</script>

<style scoped>
.exchange-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.exchange-box {
  width: 800px;
  min-height: 200px;

  /* border: 1px solid #dee2e6; */
}

</style>
