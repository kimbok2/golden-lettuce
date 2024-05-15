<template>
  <div>
    <h1>CommunityCreateView</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" v-model.trim="title" id="title" />
      <br />
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

const title = ref(null)
const content = ref(null)

const store = useCommunityStore()
const userStore = useUserStore()
const router = useRouter()

const token = userStore.token
console.log(userStore.token)

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/communities/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${token}`,
    },
  })
    .then((response) => {
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
