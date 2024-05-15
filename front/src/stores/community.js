import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCommunityStore = defineStore(
  'community',
  () => {
    const API_URL = 'http://127.0.0.1:8000'

    const router = useRouter()

    const categoryOptions = {
      notice: '공지사항',
      faq: 'FAQ',
      free: '자유게시판',
    }

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
          router.push({ name: 'community' })
        })
        .catch((error) => {
          console.log(error)
        })
    }

    const getArticle = function (articleId) {
      axios({
        method: 'get',
        url: `${API_URL}/communities/${articleId}`,
      })
        .then((response) => {
          article.value = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    }

    return { article, articles, article_count, API_URL, categoryOptions, getArticle, getArticleList }
  },
  { persist: true }
)
