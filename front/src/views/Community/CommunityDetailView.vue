<template>
  <div>
    <h1>CommunityDetailView</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const router = useRoute()
const articleId = router.params.id

console.log(articleId)



</script>
<style scoped></style>
