<template>
  <div class="exchange-list container">
    <p class="text-start">ExchangeList</p>
    <ExchangeListItem />
    <ExchangeListItem />
  </div>
</template>

<script setup>
import ExchangeListItem from '@/components/Exchange/ExchangeListItem.vue'
</script>

<style scoped>
.exchange-list {
  text-align: left;
}
</style>
