<template>
  <div>
    <!-- 댓글이 있으면 출력 -->
    <template v-if="article?.comments.length">
      <div class="d-flex justify-content-between">
        <h3>댓글</h3>
        <p class="text-end">댓글 수 : {{ comment_count }}</p>
      </div>
      <!-- 댓글 리스트  -->
      <ul class="list-group">
        <template v-for="comment in article.comments" :key="comment.id">
          <li v-if="comment?.parent_comment === null" class="list-group-item border border-0 rounded-0">
            <!-- 댓글 정보 -->
            <div class="d-flex">
              <!-- 댓글 작성자 -->
              <!-- 댓글 작성자 프로필 이미지 // 수정 필요 // 현재는 기본 이미지로 돼있음-->
              <img
                src="@/assets/userdefault.png"
                alt="Logo"
                width="50"
                height="50"
                class="d-inline-block align-text-top border rounded-circle"
              />
              <div class="ms-3">
                <p class="fw-bolder comment-username">
                  <!-- 댓글 작성자 -->
                  <span>{{ comment.user.username }}</span>
                </p>
                <!-- 댓글 박스 -->
                <div class="comment-content">
                  <span>{{ comment.content }}</span>
                  <!-- 접속자와 댓글 작성자가 같으면 댓글 삭제 버튼 활성화 -->
                  <template v-if="username === comment.user.username">
                    <!-- 댓글 삭제 버튼 -->
                    <span>
                      <button @click.prevent="deleteComment(comment.id)" class="btn text-danger py-0">X</button>
                    </span>
                  </template>
                </div>
              </div>
            </div>
            <!-- 대댓글 작성 -->
            <div>
              <span class="text-secondary">{{
                formattedDate(comment.created_at) + ' ' + formattedTime(comment.created_at)
              }}</span>
              <!-- 답글 작성 form 토글 버튼 -->
              <button @click.prevent="toggleReplyForm(comment.id)" class="text-decoration-none text-secondary btn py-0">
                [답글 작성]
              </button>
            </div>
            <!-- 대댓글 작성 form -->
            <form
              v-show="replyFormVisible[comment.id]"
              @submit.prevent="createReply(comment.id)"
              class="border rounded-0 p-3 inline-block"
              style="width: 100%"
            >
              <!-- 라벨. 접속한 유저의 아이디 출력 -->
              <p>
                <label for="comment-content" class="fw-bolder">{{ username }}</label>
              </p>
              <input
                class="w-100 border border-0"
                type="text"
                id="comment-content"
                placeholder="댓글을 남겨보세요"
                v-model="replyContent"
              />
              <p class="text-end m-0">
                <input type="submit" value="등록" class="btn btn-primary" />
              </p>
            </form>
            <!-- 대댓글 리스트 -->
            <template v-if="comment.replies">
              <ul>
                <li v-for="reply in comment.replies" :key="reply.id" class="list-group-item border border-0 rounded-0">
                  <hr />
                  <!-- 댓글 작성자 프로필 이미지 // 수정 필요 // 현재는 기본 이미지로 돼있음-->
                  <div class="d-flex">
                    <img
                      src="@/assets/userdefault.png"
                      alt="Logo"
                      width="50"
                      height="50"
                      class="d-inline-block align-text-top border rounded-circle"
                    />
                    <div class="ms-3">
                      <p class="fw-bolder comment-username">{{ reply.user.username }}</p>
                      <span class="comment-content">{{ reply.content }}</span>
                      <template v-if="username === reply.user.username">
                        <!-- 대댓글 삭제 버튼 -->
                        <span>
                          <button @click.prevent="deleteComment(reply.id)" class="btn text-danger py-0">X</button>
                        </span>
                      </template>
                    </div>
                  </div>
                  <div>
                    <span class="text-secondary">{{
                      formattedDate(reply.created_at) + ' ' + formattedTime(reply.created_at)
                    }}</span>
                  </div>
                </li>
              </ul>
            </template>
            <hr />
          </li>
        </template>
      </ul>
    </template>
    <!-- 댓글이 없으면 출력 -->
    <template v-else> </template>
    <!-- 댓글 작성 창 -->
    <form @submit.prevent="createComment" class="border rounded-0 p-3">
      <!-- 라벨. 접속한 유저의 아이디 출력 -->
      <p>
        <label for="comment-content" class="fw-bolder">{{ username }}</label>
      </p>
      <input
        class="w-100 border border-0"
        type="text"
        id="comment-content"
        placeholder="댓글을 남겨보세요"
        v-model="commentContent"
      />
      <p class="text-end m-0">
        <input type="submit" value="등록" class="btn btn-primary" />
      </p>
    </form>
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

const articleId = ref(null)
const article = ref(null)
const username = ref(null)

const commentContent = ref(null)
const replyContent = ref(null)

// 대댓글 작성 form 토글을 위한 변수 및 함수 선언
const replyFormVisible = ref({})
const toggleReplyForm = function (commentId) {
  replyFormVisible.value[commentId] = !replyFormVisible.value[commentId]
}

const token = userStore.token

const comment_count = computed(() => {
  // article에 달린 댓글 (comments)가 없으면 0을 반환,
  // 댓글이 있는 경우 댓글의 수를 세서 반환함
  return article.value.comments ? article.value.comments.length : 0
})

const formattedDate = function (date) {
  return date.substring(0, 10)
}

const formattedTime = function (date) {
  return date.substring(11, 19)
}

const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/communities/${articleId.value}/comment/`,
    data: {
      content: commentContent.value,
    },
    headers: {
      Authorization: `Token ${token}`,
    },
  })
    .then((response) => {
      article.value = store.getArticle(articleId.value)
      console.log('댓글 작성 완료')
    })
    .catch((error) => {
      console.log(error)
    })

  commentContent.value = ''
}

const deleteComment = function (commentId) {
  if (confirm('댓글을 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/communities/comment/${commentId}/`,
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => {
        article.value = store.getArticle(articleId.value)
        console.log('댓글 삭제 완료')
      })
      .catch((error) => {
        console.log(error)
      })

    commentContent.value = ''
  }
}

const createReply = function (commentId) {
  axios({
    method: 'post',
    url: `${store.API_URL}/communities/${articleId.value}/comment/`,
    data: {
      parent_comment: commentId,
      content: replyContent.value,
    },
    headers: {
      Authorization: `Token ${token}`,
    },
  })
    .then((response) => {
      article.value = store.getArticle(articleId.value)
      replyFormVisible.value[commentId] = !replyFormVisible.value[commentId]
      console.log('대댓글 작성 완료')
    })
    .catch((error) => {
      console.log(error)
    })

  replyContent.value = ''
}

watch(
  () => store.article,
  (newArticle) => {
    article.value = newArticle
  },
  { deep: true }
)

onMounted(() => {
  articleId.value = route.params.id
  article.value = store.getArticle(articleId.value)
  username.value = userStore.name
})
</script>

<style scoped>
.comment-username {
  margin: 0;
}

.comment-content {
  margin: 0;
}

hr {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
