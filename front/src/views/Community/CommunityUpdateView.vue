<template>
  <div>
    <h1>CommunityUpdateView</h1>
    <button class="btn btn-primary" @click="goBack">뒤로가기</button>
    <form @submit.prevent="updateArticle">
      <!-- 카테고리 선택 -->

      <label for="category">카테고리 : </label>
      <select v-model="category" id="category">
        <option value="free">자유게시판</option>
        <option value="faq">FAQ</option>
        <option value="notice">공지사항</option>
      </select>
      <br />

      <!-- 제목 -->
      <label for="title">제목 : </label>
      <input type="text" v-model.trim="title" id="title" />
      <br />

      <!-- 내용 -->
      <label for="content">내용 : </label>
      <input type="text" v-model.trim="content" id="content" />
      <br />
    </form>
    <p>
      <button class="btn btn-primary" @click="updateArticle">게시글 수정</button>
      <span> / </span>
      <button class="btn btn-primary" @click="deleteArticle">게시글 삭제</button>
    </p>
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCommunityStore } from '@/stores/community'
import axios from 'axios'

const title = ref(null)
const content = ref(null)
const category = ref(null)

const route = useRoute()
const router = useRouter()
const store = useCommunityStore()

const articleId = route.params.id
const article = store.article

const comment_count = computed(() => {
  return article.comment_set.length
})

const goBack = function () {
  router.back()
}

const updateArticle = function () {
  if (confirm('게시글을 수정하시겠습니까?')) {
    axios({
      method: 'put',
      url: `${store.API_URL}/communities/${articleId}/`,
      data: {
        title: title.value,
        content: content.value,
        category: category.value,
      },
    })
      .then((response) => {
        router.push({ name: 'community-detail', params: { id: `${articleId}` } })
      })
      .catch((error) => {
        console.log(error)
      })
  }
}

const deleteArticle = function () {
  if (confirm('게시글을 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/communities/${articleId}/`,
    })
      .then((response) => {
        router.push({ name: 'community' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
}

onMounted(() => {
  ;(title.value = store.article.title),
    (category.value = store.article.category),
    (content.value = store.article.content)
})
</script>
<style scoped></style>
