<template>
  <div>
    <canvas ref="chart"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

const props = defineProps(["join_product"]);
const chart = ref(null);
let chartInstance = null;

const createChart = () => {
  if (chartInstance) {
    chartInstance.destroy();
  }

  const labels = props.join_product.map((product) => product.fin_prdt_nm);
  const intrRates = props.join_product.map((product) => {
    let highestRateOption = null;
    if (product.depositoption_set) {
      highestRateOption = product.depositoption_set.reduce((max, option) =>
        parseFloat(option.intr_rate2) > parseFloat(max.intr_rate2) ? option : max
      );
    } else if (product.savingoption_set) {
      highestRateOption = product.savingoption_set.reduce((max, option) =>
        parseFloat(option.intr_rate2) > parseFloat(max.intr_rate2) ? option : max
      );
    }
    return highestRateOption ? parseFloat(highestRateOption.intr_rate) : 0;
  });
  const intrRate2s = props.join_product.map((product) => {
    let highestRateOption = null;
    if (product.depositoption_set) {
      highestRateOption = product.depositoption_set.reduce((max, option) =>
        parseFloat(option.intr_rate2) > parseFloat(max.intr_rate2) ? option : max
      );
    } else if (product.savingoption_set) {
      highestRateOption = product.savingoption_set.reduce((max, option) =>
        parseFloat(option.intr_rate2) > parseFloat(max.intr_rate2) ? option : max
      );
    }
    return highestRateOption ? parseFloat(highestRateOption.intr_rate2) : 0;
  });

  const ctx = chart.value.getContext("2d");
  chartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels,
      datasets: [
        {
          label: "저축 금리 (%)",
          data: intrRates,
          backgroundColor: "rgba(75, 192, 192, 0.6)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
        },
        {
          label: "최고 우대 금리 (%)",
          data: intrRate2s,
          backgroundColor: "rgba(153, 102, 255, 0.6)",
          borderColor: "rgba(153, 102, 255, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      maintainAspectRatio: false,
      scales: {
        x: {
          ticks: {
            font: {
              size: 10, // 글자 크기를 작게 설정
            },
            maxRotation: 90,
            minRotation: 45,
          },
        },
        y: {
          beginAtZero: true,
        },
      },
      layout: {},
    },
  });
};

onMounted(() => {
  createChart();
});

watch(
  () => props.join_product,
  (newVal) => {
    createChart();
  },
  { deep: true }
);
</script>

<style scoped>
canvas {
  max-width: 100%;
  width: 450px;
  height: 300px !important;
  margin: auto;
}
</style>
