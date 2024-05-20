<template>
  <div class="col-10 d-flex align-items-center">
    <div class="input-group">
      <span class="input-group-text">
        <select @change="currentSelectChange" class="form-select" v-model="selectedItemCurrent">
          <option disabled value="null"><span class="text-secondary">통화를 선택하세요</span></option>
          <option v-for="currency in currencies" :value="currency.pk">
            {{ currency.cur_unit }} ({{ currency.cur_nm }})
          </option>
        </select>
      </span>
      <div class="form-control input-group">
        <input
          v-if="isSelected"
          ref="inputIf"
          @input="onlyNumbers"
          class="form-control text-end"
          type="text"
          placeholder="값"
          v-model="inputValue"
        />
        <input
          v-else
          ref="inputElse"
          @click="focusInputIf"
          @input="onlyNumbers"
          class="form-control text-end"
          type="text"
          placeholder="값"
          v-model="computedValue"
        />
        <span class="input-group-text" style="width: 90px">{{
          exchangeStore.currencies[selectedItemCurrent - 1]?.cur_unit
        }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed, nextTick, defineProps, onMounted } from 'vue'
import { useExchangeStore } from '@/stores/exchange'

// 선택된 경우의 boolean을 반환해주는 값
const isSelected = computed(() => {
  return props.handleId === exchangeStore.selectedHandle
})

// 상위 컴포넌트에서 넘겨주는 props 정의
const props = defineProps({
  handleId: {
    type: Number,
    required: true,
  },
})

const exchangeStore = useExchangeStore()
const currencies = exchangeStore.currencies

const selectedItemCurrent = ref(null)
const inputValue = ref('')

// 기준 금액 입력값을 감시, 값이 바뀌면 exchangeStore의 입력값을 수정해줌
watch(
  () => inputValue.value,
  (newValue) => {
    exchangeStore.inputAmount = newValue
    exchangeStore.selectedCurrent = selectedItemCurrent.value
  },
  { deep: true }
)

// 계산된 값을 반환, 선택됟ㄴ 기준 금액 이외의 값들만 해당됨
const computedRate = computed(() => {
  const index = parseInt(selectedItemCurrent.value) - 1
  if (!isNaN(index) && exchangeStore.exchangeRates[index]) {
    return exchangeStore.exchangeRates[index]['latest_exchange_deal_bas_r']
  }
  return null
})

const computedValue = computed(() => {
  console.log(computedRate.value)
  return computedRate.value * exchangeStore.inputAmount
})

// select form에서 통화를 선택하면, 해당 통화를 현재 선택된 통화로 수정
const currentSelectChange = function () {
  if (selectedItemCurrent.value) {
    // exchangeStore의 현재 선택된 통화 값을 현재 선택 통화로 변경
    exchangeStore.selectedCurrent = selectedItemCurrent.value
    // exchangeStore의 현재 선택된 핸들 값 변경
    exchangeStore.selectedHandle = props.handleId
    // 현재 input의 값을 기존의 computed 값으로 변경
    // inputValue.value = computedValue.value
  }
}

const onlyNumbers = function (event) {
  const value = event.target.value
  const numericValue = value.replace(/\D/g, '') // 숫자가 아닌 문자를 제거
  if (numericValue !== inputValue.value) {
    inputValue.value = numericValue
  }
  currentSelectChange()
}

const inputIf = ref(null)
const inputElse = ref(null)

// v-else 상태일 때, v-else 태그의 input을 클릭하면 현재의 통화를 기준 통화로 바꾸어주기
// 클릭과 동시에 현재 선택 상태를 현재 통화로, focus도 함께 바꿔줌
const focusInputIf = () => {
  inputValue.value = 0
  currentSelectChange()
  exchangeStore.selectedHandle = props.handleId // 상태 변경하여 v-if를 true로 설정
  nextTick(() => {
    if (inputIf.value) {
      console.log('click')
      inputIf.value.focus()
    }
  })
}

onMounted(() => {
  exchangeStore.inputAmount = ''
})
</script>

<style scoped>
.btn {
  padding: 10px;
  width: 40px;
  height: 40px;
}

.multi-line-option {
  white-space: pre-line;
}

.exchange-bar {
  height: 75px;
}

/* .select-currency {
} */
</style>
