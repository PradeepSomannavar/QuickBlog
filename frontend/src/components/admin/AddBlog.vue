<template>
  <div class="p-6 lg:p-8">
    <div class="max-w-3xl mx-auto">
      <h1 class="text-2xl font-bold text-slate-900 dark:text-white mb-8">Add New Blog</h1>
      <div class="card-premium p-6 lg:p-8">
        <form @submit.prevent="submitBlog" class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Title</label>
            <input type="text" placeholder="Enter blog title" v-model="title" required class="input">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Subtitle</label>
            <input type="text" placeholder="Enter blog subtitle" v-model="subtitle" required class="input">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Image</label>
            <div class="flex items-center gap-4">
              <input type="file" @change="onFileChange" class="hidden" id="file-upload" accept="image/*" />
              <label for="file-upload" class="btn-outline cursor-pointer">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/>
                </svg>
                Choose File
              </label>
              <span class="text-sm text-slate-500 dark:text-slate-400">{{ fileName || 'No file chosen' }}</span>
            </div>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Description</label>
            <div class="relative">
              <textarea
                placeholder="Write your blog description here..."
                v-model="description"
                rows="8"
                class="input resize-none"
              ></textarea>
              <button
                type="button"
                @click="generateWithAI"
                class="absolute bottom-3 right-3 btn text-xs bg-violet-50 dark:bg-violet-900/30 text-violet-700 dark:text-violet-300 hover:bg-violet-100 dark:hover:bg-violet-900/50 border-0 rounded-lg"
              >
                <svg class="w-3.5 h-3.5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                </svg>
                Generate with AI
              </button>
            </div>
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Category</label>
            <select v-model="category" class="input">
              <option value="">Select Category</option>
              <option value="1">Technology</option>
              <option value="2">Design</option>
              <option value="3">Business</option>
              <option value="4">Lifestyle</option>
              <option value="5">Travel</option>
              <option value="6">Food</option>
            </select>
          </div>
          <div class="flex items-center gap-2">
            <input type="checkbox" v-model="publishNow" id="publish-now" class="w-4 h-4 rounded border-slate-300 dark:border-slate-600 text-brand-600 focus:ring-brand-500">
            <label for="publish-now" class="text-sm text-slate-700 dark:text-slate-300">Publish immediately</label>
          </div>
          <div class="flex gap-3 pt-2">
            <button type="submit" class="btn-primary">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/>
              </svg>
              Save Blog
            </button>
            <button type="button" @click="resetForm" class="btn-outline">
              Reset
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import API from '../../services/api.js'

const title = ref('')
const subtitle = ref('')
const description = ref('')
const category = ref('')
const publishNow = ref(false)
const fileName = ref('')

function onFileChange(event) {
  const file = event.target.files[0]
  if (file) {
    fileName.value = file.name
  }
}

async function generateWithAI() {
  if (!title.value.trim()) {
    alert('Please enter a title first!')
    return
  }
  try {
    const response = await API.post('/ai/generate', {
      title: title.value,
      subtitle: subtitle.value,
      img: fileName.value
    })
    description.value = response.data.description
  } catch (error) {
    console.error('AI generation failed:', error)
    alert('Failed to generate content with AI. Please try again.')
  }
}

function resetForm() {
  title.value = ''
  subtitle.value = ''
  description.value = ''
  category.value = ''
  publishNow.value = false
  fileName.value = ''
}

async function submitBlog() {
  try {
    const token = localStorage.getItem('token')
    const headers = token ? { Authorization: `Bearer ${token}` } : {}

    const formData = new FormData()
    formData.append('title', title.value)
    formData.append('subtitle', subtitle.value)
    formData.append('description', description.value)
    formData.append('category_id', category.value)
    formData.append('publish_now', publishNow.value)
    const fileInput = document.getElementById('file-upload')
    if (fileInput && fileInput.files[0]) {
      formData.append('thumbnail', fileInput.files[0])
    }

    await API.post('/blogs/', formData, {
      headers: { ...headers, 'Content-Type': 'multipart/form-data' }
    })

    alert('Blog added successfully!')
    resetForm()
  } catch (error) {
    console.error('Failed to add blog:', error)
    alert(error.response?.data?.details || 'Failed to add blog. Please try again.')
  }
}
</script>
