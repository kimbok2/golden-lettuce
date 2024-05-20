<template>
  <div class="exchange-list container">
    <div class="exchange-bar row my-1" v-for="handle in handleList" :key="handle.id">
      <ExchangeListItem :handle-id="handle.id" />
      <ExchangeHandle :handle-id="handle.id" @add-handle="addHandle" @remove-handle="removeHandle" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

import ExchangeListItem from '@/components/Exchange/ExchangeListItem.vue'
import ExchangeHandle from '@/components/Exchange/ExchangeHandle.vue'

let id = 0

const handleList = ref([{ id: id++ }, { id: id++ },])

const addHandle = function () {
  if (handleList.value.length < 5) {
    handleList.value.push({ id: id++ })
  } else {
    alert('통화를 5개 이상 선택할 수 없습니다.')
  }
}

const removeHandle = function (handleId) {
  console.log(handleId)
  const index = handleList.value.findIndex((handle) => handle.id === handleId)
  if (index !== -1) {
    handleList.value.splice(index, 1)

    if (handleList.value.length === 0) {
      addHandle()
    }
  }
}
</script>

<style scoped>
.exchange-bar {
  height: 75px;
}

.exchange-list {
  text-align: left;
}
</style>
