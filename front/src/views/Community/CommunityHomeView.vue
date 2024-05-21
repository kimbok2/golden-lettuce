<template>
  <div class="p-5">
    <p class="text-end">게시글 수 : {{ store.article_count }}</p>
    <table class="table table-hover">
      <thead>
        <tr class="">
          <th scope="col" class="col-category">카테고리</th>
          <th scope="col" class="col-title">제목</th>
          <th scope="col" class="col-user">작성자</th>
          <th scope="col" class="col-date">작성일</th>
          <th scope="col" class="col-views">조회 수</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in store.articles" :key="article.pk"
        @click="toDetail({ name: 'community-detail', params: { id: article.id } })">
          <th scope="row">{{ article.category }}</th>
          <td class="text-start">
            <span> {{ article.title }}</span> <span class="fw-bold text-danger"> [{{ article.comment_count }}]</span>
          </td>
          <th>{{ article.user.nickname }}</th>
          <td>{{ formattedDate(article.created_at) }}</td>
          <td>not yet</td>
        </tr>
      </tbody>
    </table>
    <!-- <ul class="text-center ps-0 list-group">
      <li class="list-group border rounded-0 fw-bolder">
        <div class="row my-3">
          <div class="col-2">카테고리</div>
          <div class="col-6">제목</div>
          <div class="col-1">작성자</div>
          <div class="col-2">작성일</div>
          <div class="col-1">조회 수</div>
        </div>
      </li>
      <template v-for="article in store.articles" :key="article.pk">
        <li class="list-group border border-0 rounded-0">
          <div class="row my-3">
            <div class="col-2">{{ article.category }}</div>
            <div class="col-6 text-start" @click="toDetail({ name: 'community-detail', params: { id: article.id } })">
              <span> {{ article.title }}</span>
              <span class="fw-bold text-danger"> [{{ article.comment_count }}]</span>
            </div>
            <div class="col-1 fw-bolder">{{ article.user.nickname }}</div>
            <div class="col-2">{{ formattedDate(article.created_at) }}</div>
            <div class="col-1">not yet</div>
          </div>
          <hr class="my-0" />
        </li>
      </template>
    </ul> -->
    <br />

    <RouterLink v-if="userStore.isLogin" :to="{ name: 'community-create' }">
      <p class="text-end">
        <button class="btn btn-primary">게시글 작성</button>
      </p>
    </RouterLink>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useCommunityStore } from '@/stores/community'
import { useUserStore } from '@/stores/user'

import CommunityCreateView from '@/views/Community/CommunityCreateView.vue'
import CommunityDetailView from '@/views/Community/CommunityDetailView.vue'

const router = useRouter()
const store = useCommunityStore()
const userStore = useUserStore()
const selectedCategory = ref(null)

const formattedDate = function (date) {
  return date.substring(0, 10)
}

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

<style scoped>
.col-category {
  width: 10%;
}

.col-title {
  width: 50%;
}

.col-user {
  width: 10%;
}

.col-date {
  width: 10%;
}

.col-views {
  width: 10%;
}

tbody > tr {
  height: 75px;
  vertical-align: middle;
}
</style>
