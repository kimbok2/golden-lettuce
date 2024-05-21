<template>
  <div>
    <RouterLink :to="{ name: 'community' }" class="text-decoration-none text-black">
      <h1 class="main-h1-container">
        <span>커뮤니티</span><span class="material-symbols-outlined"> forum </span>
      </h1>
    </RouterLink>
    <div class="community-container">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useCommunityStore } from '@/stores/community'

import CommunityCreateView from '@/views/Community/CommunityCreateView.vue'
import CommunityHomeView from '@/views/Community/CommunityHomeView.vue'
</script>

<style scoped>
.community-container {
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

</style>
