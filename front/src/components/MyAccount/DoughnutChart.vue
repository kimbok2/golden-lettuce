<template>
  <div>
    <Doughnut :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup>
import { ref, watch, computed } from "vue";
import { Doughnut } from "vue-chartjs";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

const props = defineProps({
  score: {
    type: Number,
    required: true,
  },
});

const animatedScore = ref(0);
const isAnimatingChart = ref(false);

const chartData = computed(() => {
  return {
    labels: ["Score", "Remaining"],
    datasets: [
      {
        data: [animatedScore.value, 1000 - animatedScore.value],
        backgroundColor: ["#3b82f6", "#d1d5db"],
        hoverBackgroundColor: ["#2563eb", "#9ca3af"],
      },
    ],
  };
});

const chartOptions = {
  responsive: true,
  cutout: "70%",
  plugins: {
    tooltip: {
      enabled: false,
    },
    legend: {
      display: false,
    },
    centerText: {
      display: true,
      text: "0점", // 초기 텍스트 설정
    },
  },
};

// Custom plugin to draw text in the center
const centerTextPlugin = {
  id: "centerText",
  beforeDraw: function (chart) {
    if (
      chart.config.options.plugins.centerText.display !== null &&
      typeof chart.config.options.plugins.centerText.display !== "undefined" &&
      chart.config.options.plugins.centerText.display
    ) {
      const ctx = chart.ctx;
      const centerConfig = chart.config.options.plugins.centerText;
      const fontStyle = centerConfig.fontStyle || "Arial";
      const txt = centerConfig.text;
      const color = centerConfig.color || "#000";
      const sidePadding = centerConfig.sidePadding || 20;
      const sidePaddingCalculated =
        (sidePadding / 100) * (chart.innerRadius * 2);
      ctx.font = `30px ${fontStyle}`;

      // Get the width of the string and also the total width of the element
      const stringWidth = ctx.measureText(txt).width;
      const elementWidth = chart.innerRadius * 2 - sidePaddingCalculated;

      // Find out how much the font can grow in width.
      const widthRatio = elementWidth / stringWidth;
      const newFontSize = Math.floor(30 * widthRatio);
      const elementHeight = chart.innerRadius * 2;

      // Pick a new font size so it will not be larger than the height of label.
      const fontSizeToUse = Math.min(newFontSize, elementHeight);

      // Set font settings to draw it correctly.
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
      const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 2;
      ctx.font = `${fontSizeToUse}px ${fontStyle}`;
      ctx.fillStyle = color;

      // Draw text in center
      ctx.fillText(txt, centerX, centerY);
    }
  },
};

ChartJS.register(centerTextPlugin);

// Function to animate the score
const animateChart = (start, end, duration) => {
  return new Promise((resolve) => {
    const startTime = performance.now();
    const step = (currentTime) => {
      const progress = Math.min((currentTime - startTime) / duration, 1);
      animatedScore.value = Math.floor(progress * (end - start) + start);
      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        resolve();
      }
    };
    requestAnimationFrame(step);
  });
};

const animateText = (start, end, duration) => {
  const startTime = performance.now();
  const step = (currentTime) => {
    const progress = Math.min((currentTime - startTime) / duration, 1);
    chartOptions.plugins.centerText.text = `${Math.floor(
      progress * (end - start) + start
    )}점`;
    if (progress < 1) {
      requestAnimationFrame(step);
    }
  };
  requestAnimationFrame(step);
};

// Watch for score prop and trigger animation
watch(
  () => props.score,
  async (newScore) => {
    isAnimatingChart.value = true;
    await animateChart(0, newScore, 1000); // Animate from 0 to newScore in 1 second
    isAnimatingChart.value = false;
    animateText(0, newScore, 1000); // Animate text from 0 to newScore in 1 second
  },
  { immediate: true }
);
</script>

<style scoped></style>
