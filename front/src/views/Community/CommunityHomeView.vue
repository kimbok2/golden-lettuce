<template>
  <div>
    <h1>CommunityHomeView</h1>
    <p>게시글 수 : {{ store.article_count }}</p>
    <ul class="text-start">
      <template v-for="article in store.articles" :key="article.pk">
        <RouterLink :to="{ name: 'community-detail', params: {id: article.id}}">
          <li class="card">
            <p>제목 : {{ article.title }} | 작성자 : {{ article.user.username }} | 카테고리 : {{ article.category }} | 댓글 수 : {{ article.comment_count }}</p>
          </li>
        </RouterLink>
      </template>
    </ul>
    <RouterLink :to="{ name: 'community-create' }">
      <button class="btn btn-primary">게시글 작성</button>
    </RouterLink>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useCommunityStore } from '@/stores/community'

import CommunityCreateView from '@/views/Community/CommunityCreateView.vue'
import CommunityDetailView from '@/views/Community/CommunityDetailView.vue'

const store = useCommunityStore()
const selectedCategory = ref(null)

onMounted(() => {
  store.getArticleList()
})
</script>

<style scoped></style>
