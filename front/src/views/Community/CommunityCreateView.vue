<template>
  <div class="p-5 text-start">
    <p class="text-end">
      <button class="btn btn-primary" @click="goBack">뒤로가기</button>
    </p>
    <form @submit.prevent="createArticle">
      <!-- 카테고리 선택 -->
    
      <label for="category">카테고리 : </label>
      <select v-model="category" id="category">
        <option value="free">자유게시판</option>
        <option value="faq">FAQ</option>
        <option value="notice">공지사항</option>
      </select>
      <br />

      <h1>
          <textarea type="text" style="width: 100%; height: 50px; text-align: middle !important;" v-model.trim="title" id="title" placeholder="제목을 입력하세요" />
        </h1>
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


const goBack = function () {
  router.back()
}

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

<style scoped>

textarea {

border: none;
border-radius: 10px;
box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}


</style>
