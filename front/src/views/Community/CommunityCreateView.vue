<template>
  <div class="text-start card p-3 rounded-0">
    <form @submit.prevent="createArticle">
      <!-- 카테고리 선택 -->

      <!-- 제목 바 -->
      <!-- <div>
        <h1>{{ article.title }}</h1>
        <img
          src="@/assets/userdefault.png"
          alt="Logo"
          width="50"
          height="50"
          class="d-inline-block align-text-top border rounded-circle"
        />
        <span class="fw-bolder">{{ article.user.nickname }}</span> -->
        <!-- 게시글 작성일, 게시글 수정일 표시 -->
        <!-- <div class="text-end">
          <span>작성 : {{ formattedDate(article.created_at) + ' ' + formattedTime(article.created_at) }}</span>
          <span> | </span>
          <span>수정 : {{ formattedDate(article.updated_at) + ' ' + formattedTime(article.updated_at) }}</span>
        </div>
      </div> -->
      
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
      <input type="submit" value="게시글 작성" />
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useCommunityStore } from '@/stores/community'
import { useUserStore } from '@/stores/user'

// 제목과 내용 : input 태그에 v-model로 양방향 바인딩
const title = ref(null)
const content = ref(null)
const category = ref('free')

const store = useCommunityStore()
const userStore = useUserStore()
const router = useRouter()

const token = userStore.token

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/communities/`,
    data: {
      title: title.value,
      content: content.value,
      category: category.value,
    },
    headers: {
      Authorization: `Token ${token}`,
    },
  })
    .then((response) => {
      console.log('게시글 작성 성공')
      router.push({ name: 'community' })
    })
    .catch((error) => {
      console.log(error)
    })

  title.value = ''
  content.value = ''
}
</script>

<style scoped></style>
