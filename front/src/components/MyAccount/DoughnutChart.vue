<template>
  <!-- <div>
    <Doughnut :data="chartData" :options="chartOptions" />
  </div> -->
  <div v-if="userInfo?.credit_score" class="text-center mb-3">
    <Doughnut :data="chartData" :options="chartOptions" />
  </div>
  <div v-else class="d-flex justify-content-center align-items-center">
    <a>더 많은 상품을 추천받으시려면 내 정보를 입력해주세요</a>
  </div>
</template>

<script setup>
import { ref, watch, computed, onMounted, onUnmounted } from 'vue'
import { Doughnut } from 'vue-chartjs'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const userInfo = computed(() => userStore.userInfo)

ChartJS.register(ArcElement, Tooltip, Legend)

const props = defineProps({
  score: {
    type: Number,
    required: true,
  },
})

const animatedScore = ref(0)
const isAnimatingChart = ref(false)
let animationFrameId = null

const chartData = computed(() => {
  return {
    labels: ['Score', 'Remaining'],
    datasets: [
      {
        data: [animatedScore.value, 1000 - animatedScore.value],
        backgroundColor: ['#3b82f6', '#d1d5db'],
        hoverBackgroundColor: ['#2563eb', '#9ca3af'],
      },
    ],
  }
})

const chartOptions = ref({
  responsive: true,
  cutout: '70%',
  plugins: {
    tooltip: {
      enabled: false,
    },
    legend: {
      display: false,
    },
    centerText: {
      display: true,
      text: '0점', // 초기 텍스트 설정
    },
  },
})

// 중심에 텍스트를 그리기 위한 커스텀 플러그인
const centerTextPlugin = {
  id: 'centerText',
  beforeDraw: function (chart) {
    const centerConfig = chart.config.options.plugins?.centerText
    if (centerConfig?.display) {
      const ctx = chart.ctx
      const fontStyle = centerConfig.fontStyle || 'Arial'
      const txt = centerConfig.text
      const color = centerConfig.color || '#000'
      const sidePadding = centerConfig.sidePadding || 20
      const sidePaddingCalculated = (sidePadding / 100) * (chart.innerRadius * 2)
      ctx.font = `30px ${fontStyle}`

      // 문자열의 너비와 요소의 전체 너비를 얻습니다.
      const stringWidth = ctx.measureText(txt).width
      const elementWidth = chart.innerRadius * 2 - sidePaddingCalculated

      // 폰트가 얼마나 넓어질 수 있는지 확인합니다.
      const widthRatio = elementWidth / stringWidth
      const newFontSize = Math.floor(30 * widthRatio)
      const elementHeight = chart.innerRadius * 2

      // 레이블의 높이보다 크지 않도록 새로운 폰트 크기를 선택합니다.
      const fontSizeToUse = Math.min(newFontSize, elementHeight)

      // 올바르게 그리기 위한 폰트 설정을 합니다.
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      const centerX = (chart.chartArea.left + chart.chartArea.right) / 2
      const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 2
      ctx.font = `${fontSizeToUse}px ${fontStyle}`
      ctx.fillStyle = color

      // 중심에 텍스트를 그립니다.
      ctx.fillText(txt, centerX, centerY)
    }
  },
}

// Chart.js에 커스텀 플러그인을 등록합니다.
ChartJS.register(centerTextPlugin)

// 점수를 애니메이션하는 함수
const animateChart = (start, end, duration) => {
  return new Promise((resolve) => {
    const startTime = performance.now()
    const step = (currentTime) => {
      const progress = Math.min((currentTime - startTime) / duration, 1)
      animatedScore.value = Math.floor(progress * (end - start) + start)
      if (progress < 1) {
        animationFrameId = requestAnimationFrame(step)
      } else {
        resolve()
      }
    }
    animationFrameId = requestAnimationFrame(step)
  })
}

// 텍스트를 애니메이션하는 함수
const animateText = (start, end, duration) => {
  const startTime = performance.now()
  const step = (currentTime) => {
    const progress = Math.min((currentTime - startTime) / duration, 1)
    chartOptions.value.plugins.centerText.text = `${Math.floor(progress * (end - start) + start)} 점`
    if (progress < 1) {
      animationFrameId = requestAnimationFrame(step)
    }
  }
  animationFrameId = requestAnimationFrame(step)
}

// 컴포넌트가 마운트될 때 애니메이션을 초기화합니다.
onMounted(() => {
  animateChart(0, props.score, 1000) // 0에서 props.score까지 1초 동안 애니메이션합니다.
  // animateText(0, props.score, 1000) // 텍스트를 0에서 props.score까지 1초 동안 애니메이션합니다.
})

// 컴포넌트가 언마운트될 때 애니메이션 프레임을 취소합니다.
onUnmounted(() => {
  if (animationFrameId) {
    cancelAnimationFrame(animationFrameId)
  }
})

// score prop을 감시하고 애니메이션을 트리거합니다.
watch(
  () => props.score,
  async (newScore) => {
    isAnimatingChart.value = true
    await animateChart(0, newScore, 1000) // 0에서 newScore까지 1초 동안 애니메이션합니다.
    isAnimatingChart.value = false
    animateText(0, newScore, 1000) // 텍스트를 0에서 newScore까지 1초 동안 애니메이션합니다.
  },
  { immediate: true }
)
</script>

<style scoped>
canvas {
  max-width: 100%;
  height: auto;
}
</style>
