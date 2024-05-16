<template>
  <div>
    <h1>CommunityHomeView</h1>
    <p class="text-end">게시글 수 : {{ store.article_count }}</p>
    <ul class="text-start ps-0">
      <li class="card rounded-0">
        <div class="row m-0">
          <div class="col-2">카테고리</div>
          <div class="col-5">제목</div>
          <div class="col-1">작성자</div>
          <div class="col-3">작성시간</div>
          <div class="col-1">댓글 수</div>
        </div>
      </li>
      <template v-for="article in store.articles" :key="article.pk">
        <li class="card border border-0 border-bottom rounded-0">
          <div class="row m-0">
            <div class="col-2">{{ article.category }}</div>
            <div class="col-5" @click="toDetail({ name: 'community-detail', params: { id: article.id } })">
              {{ article.title }}
            </div>
            <div class="col-1">{{ article.user.username }}</div>
            <div class="col-3">{{ article.created_at }}</div>
            <div class="col-1 text-center">{{ article.comment_count }}</div>
          </div>
        </li>
      </template>
    </ul>
    <RouterLink :to="{ name: 'community-create' }">
      <button class="btn btn-primary">게시글 작성</button>
    </RouterLink>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useCommunityStore } from '@/stores/community'

import CommunityCreateView from '@/views/Community/CommunityCreateView.vue'
import CommunityDetailView from '@/views/Community/CommunityDetailView.vue'

const router = useRouter()
const store = useCommunityStore()
const selectedCategory = ref(null)

// toDetail 함수
// 게시글 버튼을 클릭하면, 해당 게시글의 상세 페이지로 이동하도록 하는 함수
// 인자 : RouterLink 주소를 통째로 받음
const toDetail = function (routerLink) {
  router.push(routerLink)
}

onMounted(() => {
  store.getArticleList()
})
</script>

<style scoped></style>
