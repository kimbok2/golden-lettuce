<template>
  <div v-if="article" class="text-start p-3 rounded-0">
    <p class="text-end">
      <button class="btn btn-secondary" @click="goBack">> {{ article.category }}</button>
    </p>
    <!-- 제목 바 -->
    <div>
      <h1>{{ article.title }}</h1>
      <img
        src="@/assets/userdefault.png"
        alt="Logo"
        width="50"
        height="50"
        class="d-inline-block align-text-top border rounded-circle"
      />
      <span class="ms-3 fw-bolder">{{ article.user.username }}</span>
      <!-- 게시글 작성일, 게시글 수정일 표시 -->
      <div class="text-end">
        <span>작성 : {{ formattedDate(article.created_at) + ' ' + formattedTime(article.created_at) }}</span>
        <span> | </span>
        <span>수정 : {{ formattedDate(article.updated_at) + ' ' + formattedTime(article.updated_at) }}</span>
      </div>
    </div>
    <hr />
    <!-- 내용 박스 -->
    <div class="article-content-box">
      <p>{{ article.content }}</p>
    </div>
    <!-- 게시글 수정 / 삭제 버튼 -->
    <p class="text-end">
      <RouterLink :to="{ name: 'community-update', params: { id: article.id } }">
        <button class="btn btn-primary" @click="updateArticle">게시글 수정</button>
      </RouterLink>
      <span> | </span>
      <button class="btn btn-primary" @click="deleteArticle">게시글 삭제</button>
    </p>
    <hr />
    <!-- 댓글 박스 -->
    <Comment />
  </div>
  <div v-else>Loading...</div>
</template>

<script setup>
import { onMounted, computed, watch, ref } from 'vue'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import { useCommunityStore } from '@/stores/community'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
import Comment from '@/components/Comment.vue'

const route = useRoute()
const router = useRouter()
const store = useCommunityStore()
const userStore = useUserStore()

const articleId = ref(null)
const article = ref(null)
const username = ref(null)

const goBack = function () {
  router.back()
}

const formattedDate = function (date) {
  return date.substring(0, 10)
}

const formattedTime = function (date) {
  return date.substring(11, 19)
}

const deleteArticle = function () {
  if (confirm('게시글을 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/communities/${articleId.value}/`,
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
  articleId.value = route.params.id
  article.value = store.getArticle(articleId.value)
  username.value = userStore.name
})

// store.article의 변화를 감지하며, 변화가 있는 경우 반응형 변수 article의 값을 바뀐 새 article(newArticle)의 값으로 바꿔줌
watch(
  () => store.article,
  (newArticle) => {
    article.value = newArticle
  }
)
</script>
<style scoped>
.article-content-box {
  min-height: 100px;
}
</style>
