<template>
  <!-- <h1 @click="viewChart">GRAPH</h1> -->
  <div v-show="showCanvas">
    <div class="col">
      <div class="graph-item chart-container">
        <div>
          <h3>환율 그래프</h3>
        </div>
        <canvas ref="chartCanvas"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'
import { useExchangeStore } from '@/stores/exchange'
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

const selectedCurrencyName = ref(null)

const showCanvas = ref(false)

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
  scales: {
    x: {
      reverse: true,
      grid: {
        display: false,
      },
      ticks: {
        font: {
          size: 14, // x축 글자 크기 조절
        },
      },
    },
    y: {
      grid: {
        display: false,
      },
      ticks: {
        font: {
          size: 14, // x축 글자 크기 조절
        },
      },
    },
  },
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
  showCanvas.value = true
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

onBeforeUnmount(() => {
  destroyChart()
  showCanvas.value = false
  exchangeStore.updateChartTrigger = 0
})

// 감시
watch(
  () => exchangeStore.updateChartTrigger,
  (newChartCurrent) => {
    console.log(newChartCurrent)
    if (exchangeStore.updateChartTrigger) {
      selectedCurrencyName.value = exchangeStore.selectedCurrentName
      return viewChart()
    }
  }
)

const viewChart = () => {
  if (exchangeStore.selectedChartCurrent !== -1) {
    try {
      const chartDatas = exchangeStore.chartData

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
  height: 400px;
  width: 800px;
}
</style>
