<template>
  <div class="text-start">
    <h1>CommunityDetailView</h1>
    <button class="btn btn-primary" @click="goBack">뒤로가기</button>
    <!-- 제목 바 -->
    <p>
      <span>제목 : {{ article.title }}</span>
      <span> | </span>
      <span>작성자 : {{ article.user.username }}</span>
      <span> | </span>
      <span>작성일 : {{ article.created_at }}</span>
      <span> | </span>
      <span>최종 수정일 : {{ article.updated_at }}</span>
    </p>
    <!-- 카테고리 바 -->
    <p>카테고리 : {{ article.category }}</p>
    <!-- 내용 박스 -->
    <p>내용 : {{ article.content }}</p>
    <hr />
    <!-- 댓글 박스 -->
    <div>
      <h3>댓글</h3>
      <!-- 댓글이 있으면 출력 -->
      <template v-if="article.comments.length">
        <p>댓글 수 : {{ comment_count }}</p>
        <hr />
        <!-- 댓글 리스트  -->
        <ol>
          <template v-for="comment in article.comment_set">
            <li>
              <p>내용 : {{ comment.content }} | 작성자 : {{ comment.user }}</p>
            </li>
            <hr />
          </template>
        </ol>
      </template>
      <!-- 댓글이 없으면 출력 -->
      <template v-else>
        <p>작성된 댓글이 없습니다.</p>
      </template>
      <!-- 댓글 작성 창 -->
      <form @submit.prevent class="border  rounded-3">
        <!-- 라벨. 접속한 유저의 아이디 출력 -->
        <p>
          <label for="">{{ userId }}</label>
        </p>
        <input class="w-100 border border-0" type="text" id="" />
        <p class="text-end m-0">
          <input type="submit" value="등록" class="btn btn-primary" />
        </p>
      </form>
    </div>
    <!-- 게시글 수정 / 삭제 버튼 -->
    <p class="text-end">
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
import { useUserStore } from '@/stores/user'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useCommunityStore()
const userStore = useUserStore()

const articleId = route.params.id
const article = ref(store.article)
const userId = ref(userStore.name)

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

const createComment = function () {}

onMounted(() => {
  store.getArticle(articleId)
})

// store.article의 변화를 감지하며, 변화가 있는 경우 반응형 변수 article의 값을 바뀐 새 article(newArticle)의 값으로 바꿔줌
watch(
  () => store.article,
  (newArticle) => {
    article.value = newArticle
  }
)
</script>
<style scoped></style>
