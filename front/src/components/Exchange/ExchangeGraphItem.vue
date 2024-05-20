<template>
  <h1 @click="viewChart">GRAPH</h1>
  <div class="col">
    <div class="graph-item chart-container">
      <!-- <Line :data="chartData" :options="chartOptions" /> -->
      <canvas ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'
import { useExchangeStore } from '@/stores/exchange'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'

const exchangeStore = useExchangeStore()

const selectedCurrency = ref(null)
const selectedCurrencyName = ref(null)

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)
// 차트 캔버스 선언
const chartCanvas = ref(null)

// 차트의 데이터 선언
const chartData = ref({
  labels: [],
  datasets: [
    {
      label: selectedCurrencyName.value,
      backgroundColor: '#f87979',
      borderColor: '#f87979',
      data: [],
      fill: false,
      tension: 0.1,
    },
  ],
})

// 차트 옵션 선언
const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
})

// 차트 인스턴스 선언
const chartInstance = ref(null)

const destroyChart = () => {
  if (chartInstance.value) {
    chartInstance.value.destroy()
    chartInstance.value = null
  }
}

const createChart = () => {
  if (chartCanvas.value) {
    const ctx = chartCanvas.value.getContext('2d')
    destroyChart()
    chartInstance.value = new ChartJS(ctx, {
      type: 'line',
      data: chartData.value,
      options: chartOptions.value,
    })
  }
}

const updateChart = () => {
  createChart()
}

onBeforeUnmount(destroyChart)

// 감시
watch(
  () => exchangeStore.selectedCurrent,
  (newChartCurrent) => {
    exchangeStore.selectedChartCurrent = newChartCurrent
    if (exchangeStore.selectedChartCurrent !== -1) {
      selectedCurrencyName.value = exchangeStore.selectedCurrentName
      viewChart()
    }
  }
)

// const viewChart = function () {
//   if (exchangeStore.selectedChartCurrent !== -1) {
//     const chartDatas = exchangeStore.getChartData()

//     chartData.value.labels = chartDatas['data_list_date']
//     chartData.value.datasets[0].data = chartDatas['data_list_rate']
//     chartData.value.datasets[0].label = selectedCurrencyName.value

//     if (chartData.value && chartData.value) {
//       updateChart()
//     }
//   } else {
//     console.error('Invalid selectedChartCurrent')
//   }
// }

const viewChart = async () => {
  exchangeStore.selectedChartCurrent = exchangeStore.selectedCurrent

  if (exchangeStore.selectedChartCurrent !== -1) {
    try {
      const chartDatas = await exchangeStore.getChartData()  // Assuming getChartData() is an async function

      chartData.value.labels = chartDatas['data_list_date']
      chartData.value.datasets[0].data = chartDatas['data_list_rate']
      chartData.value.datasets[0].label = selectedCurrencyName.value

      updateChart()
      console.log(chartData.value)
    } catch (error) {
      console.error('Error fetching chart data:', error)
    }
  } else {
    console.error('Invalid selectedChartCurrent')
  }
}


</script>

<style scoped>
.graph-item {
  /* height: 200px; */
  height: 400px;
  width: 800px;

  border: 1px solid #dee2e6;
  border-radius: 25px;
}
</style>
