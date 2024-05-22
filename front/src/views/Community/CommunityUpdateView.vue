<template>
  <div class="p-5 text-start">
    <p class="text-end">
      <button class="btn btn-primary" @click="goBack">뒤로가기</button>
    </p>
    <form @submit.prevent="updateArticle">
      <div>
        <h1>
          <textarea type="text" style="width: 100%; height: 50px; text-align: middle !important;" v-model.trim="title" id="title" placeholder="제목을 입력하세요" />
        </h1>
        <div class="mt-3 d-flex justify-content-between">
          <div>
            <img
              :src="article.user?.profile_img ? apiUrl + article.user.profile_img : '@/assets/userdefault.png'"
              alt="Logo"
              width="50"
              height="50"
              class="d-inline-block align-text-top border rounded-circle"
            />
            <span class="ms-3 fw-bolder">{{ article.user.nickname }}</span>
          </div>
          <!-- 게시글 작성일, 게시글 수정일 표시 -->
          <!-- <div class="text-end">
            <p>최초 작성일 : {{ formattedDate(article.created_at) + ' ' + formattedTime(article.created_at) }}</p>
            <p v-if="article.created_at !== article.updated_at">
              <span>수정됨 : {{ formattedDate(article.updated_at) + ' ' + formattedTime(article.updated_at) }}</span>
            </p>
            <p v-else></p>
          </div> -->
        </div>
      </div>
      <hr />
      <!-- 카테고리 선택 -->
      <!-- <select v-model="category" id="category">
        <option value="free">자유게시판</option>
        <option value="faq">FAQ</option>
        <option value="notice">공지사항</option>
      </select> -->
      <br />

      <br />
      <!-- 내용 -->
      <textarea type="text" style="width: 100%; min-height: 100px;"  v-model.trim="content" id="content" placeholder="댓글을 입력하세요" />
      <br />
      <p class="text-end">
        <button class="btn btn-primary" @click="updateArticle">게시글 수정</button>
        <button class="btn btn-primary ms-2" @click="deleteArticle">게시글 삭제</button>
      </p>
    </form>
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCommunityStore } from '@/stores/community'
import axios from 'axios'

const apiUrl = 'http://127.0.0.1:8000'

const title = ref(null)
const content = ref(null)
const category = ref(null)

const route = useRoute()
const router = useRouter()
const store = useCommunityStore()

const articleId = route.params.id
const article = store.article

const comment_count = computed(() => {
  return article.comment_set.length
})

const goBack = function () {
  router.back()
}

const updateArticle = function () {
  if (confirm('게시글을 수정하시겠습니까?')) {
    axios({
      method: 'put',
      url: `${store.API_URL}/communities/${articleId}/`,
      data: {
        title: title.value,
        content: content.value,
        category: category.value,
      },
    })
      .then((response) => {
        router.push({ name: 'community-detail', params: { id: `${articleId}` } })
      })
      .catch((error) => {
        console.log(error)
      })
  }
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
  ;(title.value = store.article.title),
    (category.value = store.article.category),
    (content.value = store.article.content)
})
</script>
<style scoped>

textarea {

  border: none;
  border-radius: 10px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}

</style>
