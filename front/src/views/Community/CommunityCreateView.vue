<template>
  <div class="m-3 p-3 text-start">
    <p class="text-end">
      <button class="btn btn-primary" @click="goBack">뒤로가기</button>
    </p>
    <form @submit.prevent="createArticle">
      <br />

      <h1>
        <textarea
          type="text"
          style="width: 100%; height: 50px; text-align: middle !important"
          v-model.trim="title"
          id="title"
          placeholder="제목을 입력하세요"
        />
      </h1>
      <div class="mt-3 d-flex justify-content-between">
        <div>
          <img
            :src="userStore.userInfo.profile_img ? apiUrl + userStore.userInfo.profile_img : '@/assets/userdefault.png'"
            alt="Logo"
            width="50"
            height="50"
            class="d-inline-block align-text-top border rounded-circle"
          />
          <div style="display: inline-flex;">
            <span class="ms-3 fw-bolder">{{ userStore.userInfo.nickname }}</span>
            <select class="ms-3" v-model="category" id="category">
              <option value="free">자유게시판</option>
              <option value="faq">FAQ</option>
              <option value="notice">공지사항</option>
            </select>
          </div>
        </div>
      </div>
      <br />
      <hr />
      <!-- 카테고리 선택 -->
      <!-- 내용 -->
      <textarea
        type="text"
        style="width: 100%; min-height: 100px"
        v-model.trim="content"
        id="content"
        placeholder="내용을 입력하세요."
      />
      <hr />
      <br />
      <p class="text-end">
        <button class="btn btn-primary" type="submit">게시글 작성</button>
      </p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useCommunityStore } from '@/stores/community'
import { useUserStore } from '@/stores/user'

const apiUrl = 'http://127.0.0:8000'

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
