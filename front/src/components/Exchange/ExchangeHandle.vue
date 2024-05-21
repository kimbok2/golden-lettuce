<template>
  <div class="handle-box col-2">
    <button @click="addHandleClick" class="btn btn-secondary">
      <span class="material-symbols-outlined"> add </span>
    </button>
    <button @click="removeHandleClick" class="btn btn-secondary mx-1">
      <span class="material-symbols-outlined"> remove </span>
    </button>
    <!-- <button class="btn btn-secondary"><span class="material-symbols-outlined"> menu </span></button> -->
  </div>
</template>

<script setup>

const emit = defineEmits(['add-handle', 'remove-handle'])
const props = defineProps({
  handleId: {
    type: Number,
    required: true
  }
})

const addHandleClick = function () {
  console.log('Add button clicked')
  emit('add-handle', props.handleId)
}

const removeHandleClick = function () {
  console.log('Remove button clicked')
  emit('remove-handle', props.handleId)
}

</script>

<style scoped>
.handle-box {
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.material-symbols-outlined {
  font-size: 20px;
}
</style>
