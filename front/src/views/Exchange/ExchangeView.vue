<template>
  <h1 class="main-h1-container">
    <span>환율 계산</span>
    <span class="material-symbols-outlined"> currency_exchange </span>
  </h1>
  <div class="exchange-main-container">
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
        <ExchangeGraphItem />
      </div>
    </div>
  </div>
</template>

<script setup>
import ExchangeList from '@/components/Exchange/ExchangeList.vue'
import ExchangeGraph from '@/components/Exchange/ExchangeGraph.vue'
import ExchangeGraphItem from '@/components/Exchange/ExchangeGraphItem.vue'
import { useExchangeStore } from '@/stores/exchange'
import { onMounted } from 'vue'

const exchangeStore = useExchangeStore()

const getRate = function () {
  exchangeStore.get_exchange_rate()
}

onMounted(() => {
  exchangeStore.selectedCurrent = null
})
</script>

<style scoped>
.exchange-main-container {
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
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
