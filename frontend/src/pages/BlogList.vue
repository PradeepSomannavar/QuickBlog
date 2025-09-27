<template>
  <div class="p-6">
    <h1 class="text-3xl font-bold mb-6">Blog List</h1>
    <BlogGrid :blogs="blogs" />
    <div v-if="loading" class="text-gray-500 mt-4">Loading blogs...</div>
    <div v-if="error" class="text-red-600 mt-4">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import BlogGrid from '../components/BlogGrid.vue'
import API from '../services/api.js'

const blogs = ref([])
const loading = ref(false)
const error = ref('')

async function fetchBlogs() {
  loading.value = true
  error.value = ''
  try {
    const response = await API.get('/blogs/')
    blogs.value = response.data
  } catch (err) {
    error.value = 'Failed to load blogs.'
    console.error('Error fetching blogs:', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchBlogs()
})
</script>

<style scoped>
/* Add any page-specific styles here */
</style>
