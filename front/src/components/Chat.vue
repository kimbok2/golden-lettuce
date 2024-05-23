<!-- src/components/Chat.vue -->
<template>
  <div
    class="offcanvas offcanvas-end"
    data-bs-scroll="true"
    tabindex="-1"
    id="offcanvasWithBothOptions"
    ref="offcanvas"
    aria-labelledby="offcanvasWithBothOptionsLabel"
  >
    <div class="offcanvas-header">
      <h1 class="text-center mt-3 ms-5">
        <div>
          금상추 봇
          <span class="material-symbols-outlined shake" style="font-size: 50px"> robot_2 </span>
          <img class="bot-logo shake" src="@/assets/LOGO_LITE.png" alt="" />
        </div>
      </h1>
      <button class="btn" type="button" data-bs-dismiss="offcanvas" aria-label="Close">
        <span style="color: crimson; font-size: 50px" class="material-symbols-outlined"> cancel </span>
      </button>
    </div>
    <div class="offcanvas-body" ref="offcanvasBody">
      <div style="margin-top: 0px">
        <div class="chat-container">
          <div class="messages">
            <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.sender]">
              <div class="message-content">{{ msg.content }}</div>
            </div>
          </div>
          <div class="input-container">
            <textarea v-model="message" placeholder="무엇이든 물어보세요"></textarea>
            <button class="button-send" @click="sendMessage">Send</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const message = ref('')
const messages = ref([])

const offcanvas = ref(null)
const offcanvasBody = ref(null)

const sendMessage = async () => {
  if (message.value.trim() === '') return

  // Add user message to messages array
  messages.value.push({ sender: 'user', content: message.value })
  scrollToBottom()

  // Send message to Django backend
  try {
    const res = await fetch('http://localhost:8000/chat/', {
      method: 'POST',
      body: new URLSearchParams({ message: message.value }),
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    })
    const data = await res.json()

    // Add AI response to messages array
    messages.value.push({ sender: 'ai', content: data.response })
  } catch (error) {
    console.error('Error:', error)
  } finally {
    // Clear the input field
    message.value = ''
    scrollToBottom()
  }
}

const scrollToBottom = async () => {
  await nextTick()
  if (offcanvasBody.value) {
    offcanvasBody.value.scrollTop = offcanvasBody.value.scrollHeight
  }
}
</script>

<style scoped>
.bot-logo {
  width: 30px;

  position: relative;
  left: -25px;
  bottom: 40px;
}

.messages {
  flex: 1;
  padding: 16px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.message {
  margin-bottom: 16px;
  max-width: 80%;
}

.message.user {
  align-self: flex-end;
  background-color: #e0f7fa;
  border-radius: 8px 8px 0 8px;
  padding: 8px 16px;
}

.message.ai {
  align-self: flex-start;
  background-color: #e8eaf6;
  border-radius: 8px 8px 8px 0;
  padding: 8px 16px;
}

.message-content {
  word-wrap: break-word;
}

.input-container {
  display: flex;
  padding: 8px;
  border-top: 1px solid #ccc;
}

textarea {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: none;
}

.button-send {
  margin-left: 8px;
  padding: 8px 16px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}

.button-send:hover {
  background-color: #0056b3;
}
</style>
