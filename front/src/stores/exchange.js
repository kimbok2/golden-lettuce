import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useExchangeStore = defineStore(
  "exchange",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const currencies = [
      {
        pk: 1,
        cur_unit: "AED",
        cur_nm: "아랍에미리트 디르함",
      },
      {
        pk: 2,
        cur_unit: "AUD",
        cur_nm: "호주 달러",
      },
      {
        pk: 3,
        cur_unit: "BHD",
        cur_nm: "바레인 디나르",
      },
      {
        pk: 4,
        cur_unit: "BND",
        cur_nm: "브루나이 달러",
      },
      {
        pk: 5,
        cur_unit: "CAD",
        cur_nm: "캐나다 달러",
      },
      {
        pk: 6,
        cur_unit: "CHF",
        cur_nm: "스위스 프랑",
      },
      {
        pk: 7,
        cur_unit: "CNH",
        cur_nm: "위안화",
      },
      {
        pk: 8,
        cur_unit: "DKK",
        cur_nm: "덴마아크 크로네",
      },
      {
        pk: 9,
        cur_unit: "EUR",
        cur_nm: "유로",
      },
      {
        pk: 10,
        cur_unit: "GBP",
        cur_nm: "영국 파운드",
      },
      {
        pk: 11,
        cur_unit: "HKD",
        cur_nm: "홍콩 달러",
      },
      {
        pk: 12,
        cur_unit: "IDR(100)",
        cur_nm: "인도네시아 루피아",
      },
      {
        pk: 13,
        cur_unit: "JPY(100)",
        cur_nm: "일본 옌",
      },
      {
        pk: 14,
        cur_unit: "KRW",
        cur_nm: "한국 원",
      },
      {
        pk: 15,
        cur_unit: "KWD",
        cur_nm: "쿠웨이트 디나르",
      },
      {
        pk: 16,
        cur_unit: "MYR",
        cur_nm: "말레이지아 링기트",
      },
      {
        pk: 17,
        cur_unit: "NOK",
        cur_nm: "노르웨이 크로네",
      },
      {
        pk: 18,
        cur_unit: "NZD",
        cur_nm: "뉴질랜드 달러",
      },
      {
        pk: 19,
        cur_unit: "SAR",
        cur_nm: "사우디 리얄",
      },
      {
        pk: 20,
        cur_unit: "SEK",
        cur_nm: "스웨덴 크로나",
      },
      {
        pk: 21,
        cur_unit: "SGD",
        cur_nm: "싱가포르 달러",
      },
      {
        pk: 22,
        cur_unit: "THB",
        cur_nm: "태국 바트",
      },
      {
        pk: 23,
        cur_unit: "USD",
        cur_nm: "미국 달러",
      },
    ];

    // 환율 정보 저장 (각각 가장 최신 환율)
    const exchangeRates = ref([]);

    // 현재 선택한 통화의 입력값
    const inputAmount = ref(null);

    // 현재 선택된 통화의 번호
    const selectedCurrent = ref(14);
    // 현재 선택된 통화 이름
    const selectedCurrentName = computed(() => {
      console.log(currencies[selectedCurrent.value - 1]["cur_nm"]);
      return currencies[selectedCurrent.value - 1]["cur_nm"];
    });

    const selectedChartCurrent = ref(null);
    const updateChartTrigger = ref(0);
    const selectedHandle = ref(0);

    // 차트 정보는 장고 서버에서 불러옴
    // 최근 ~ 일 간의 정보를 DB에서 확인
    const chartData = ref([]);

    // 선택한 통화의 환율 정보는 computed로
    const selectedRate = computed(() => {
      const index = exchangeRates.value.findIndex(
        (rate) => rate.current_id === selectedCurrent.value
      );
      if (index !== -1) {
        return exchangeRates.value[index]["latest_exchange_deal_bas_r"];
      } else {
        return 0;
      }
    });

    // DB에서 각 통화별로 마지막으로 저장된 환율을 받아옴
    // exchangeRates의 value에 배열로 저장
    const get_exchange_rate = function () {
      axios({
        method: "get",
        url: `${API_URL}/exchanges/get_current_info`,
      })
        .then((response) => {
          exchangeRates.value = response.data;
          console.log(
            "exchangeStore.get_exchange_rate : ",
            exchangeRates.value
          );
        })
        .catch((error) => {
          console.log(error);
        });
    };

    // 장고 서버에서 chartData를 불러오는 요청
    const getChartData = function () {
      axios({
        method: "get",
        url: `${API_URL}/exchanges/get_graph_data/${selectedChartCurrent.value}/`,
      })
        .then((response) => {
          console.log("exchangeStore.getChartData : ", response.data);
          chartData.value = response.data;
        })
        .then((response) => {
          updateChartTrigger.value += 1;
          console.log(updateChartTrigger.value);
        })
        .catch((error) => {
          console.log(error);
        });

      return chartData.value;
    };

    return {
      currencies,
      inputAmount,
      selectedCurrent,
      selectedCurrentName,
      selectedRate,
      exchangeRates,
      selectedHandle,
      selectedChartCurrent,
      chartData,
      updateChartTrigger,
      get_exchange_rate,
      getChartData,
    };
  },
  { persist: true }
);
