<template>
  <div>
    <h1 class="d-flex justify-content-center">
      <span>환율 계산</span>
      <span class="material-symbols-outlined mx-3" style="font-size: 50px"> calculate </span>
    </h1>
    <p class="d-flex justify-content-end">
      <button @click="getRate" class="btn btn-primary d-flex">
        <span class="material-symbols-outlined"> restart_alt </span>
      </button>
    </p>
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
import ExchangeGraph from '@/components/Exchange/ExchangeGraph.vue'
import { useExchangeStore } from '@/stores/exchange'
import { onMounted } from 'vue'

const exchangeStore = useExchangeStore()

const getRate = function () {
  exchangeStore.get_exchange_rate()
}

onMounted(() => {})
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
