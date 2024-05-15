<template>
  <div>
    <h1>CommunityDetailView</h1>
    <button class="btn btn-primary" @click="goBack">뒤로가기</button>
    <p>제목 : {{ article.title }}</p>
    <p>작성자 : {{ article.user.username }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성일 : {{ article.created_at }}</p>
    <p>최종 수정일 : {{ article.updated_at }}</p>
    <hr />
    <p>댓글 수 : {{ comment_count }}</p>
    <hr />
    <!-- 댓글 리스트  -->
    <ol>
      <template v-for="comment in article.comment_set">
        <li>
          <p>내용 : {{ comment.content }} | 작성자 : {{ comment.user.username }}</p>
        </li>
        <hr />
      </template>
    </ol>
    <p>
      <RouterLink :to="{ name: 'community-update', params: { id: article.id } }">
        <button class="btn btn-primary" @click="updateArticle">게시글 수정</button>
      </RouterLink>
      <span> / </span>
      <button class="btn btn-primary" @click="deleteArticle">게시글 삭제</button>
    </p>
  </div>
</template>

<script setup>
import { onMounted, computed, watch, ref } from 'vue'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import { useCommunityStore } from '@/stores/community'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useCommunityStore()

const articleId = route.params.id
const article = ref(store.article)

const comment_count = computed(() => {
  // article에 달린 댓글 (comments)가 없으면 0을 반환, 
  // 댓글이 있는 경우 댓글의 수를 세서 반환함
  return article.value.comments ? article.value.comments.length : 0
})

const goBack = function () {
  router.back()
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
  store.getArticle(articleId)
})

// store.article의 변화를 감지하며, 변화가 있는 경우 반응형 변수 article의 값을 바뀐 새 article(newArticle)의 값으로 바꿔줌
watch(() => store.article, (newArticle) => {
  article.value = newArticle
})
</script>
<style scoped></style>
