<template>
  <div>
    <RouterLink :to="{ name: 'community' }">
      <h1>CommunityView</h1>
    </RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
import { ref} from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useCommunityStore } from '@/stores/community'

import CommunityCreateView from '@/views/Community/CommunityCreateView.vue'
import CommunityHomeView from '@/views/Community/CommunityHomeView.vue'

</script>

<style scoped></style>
