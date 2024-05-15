import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCommunityStore = defineStore(
  'community',
  () => {
    const API_URL = 'http://127.0.0.1:8000'

    const article = ref([])
    const articles = ref([])
    const article_count = computed(() => {
      return articles.value.length
    })

    const getArticleList = function () {
      axios({
        method: 'get',
        url: `${API_URL}/communities/`,
      })
        .then((response) => {
            articles.value = response.data
        })
        .catch((error) => {
            console.log(error)
        })
    }

    const getArticle = function () {
      axios({
        method: 'get',
        url: `${API_URL}/communities/`,
      })
        .then((response) => {
            article.value = response.data
        })
        .catch((error) => {
            console.log(error)
        })
    }

    return { articles, article_count, API_URL, getArticle, getArticleList }
  },
  { persist: true }
)
