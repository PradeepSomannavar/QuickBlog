<template>
  <div class="p-6">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold text-gray-800 mb-6">Add New Blog</h1>
      <div class="bg-white rounded-lg shadow-md p-6">
        <form @submit.prevent="submitBlog" class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Title</label>
            <input
              type="text"
              placeholder="Enter blog title"
              v-model="title"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Subtitle</label>
            <input
              type="text"
              placeholder="Enter blog subtitle"
              v-model="subtitle"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Image</label>
            <div class="flex items-center space-x-4">
              <input
                type="file"
                @change="onFileChange"
                class="hidden"
                id="file-upload"
              />
              <label for="file-upload" class="cursor-pointer bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg transition-colors duration-200">
                <i class="fas fa-upload mr-2"></i> Choose File
              </label>
              <span class="text-gray-500">{{ fileName || 'No file chosen' }}</span>
            </div>
          </div>
          <div class="relative">
            <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
            <textarea
              placeholder="Write your blog description here..."
              v-model="description"
              rows="6"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 resize-none"
            ></textarea>
            <button
              type="button"
              @click="generateWithAI"
              class="absolute bottom-3 right-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white px-3 py-1 rounded-md text-sm font-medium hover:from-purple-600 hover:to-pink-600 transition-all duration-200 shadow-md"
            >
              <i class="fas fa-magic mr-1"></i> Generate with AI
            </button>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Category</label>
            <select
              v-model="category"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
            >
              <option value="">Select Category</option>
              <option value="1">Tech</option>
              <option value="2">AI</option>
              <option value="3">Lifestyle</option>
              <option value="4">Finance</option>
            </select>
          </div>
          <div class="flex items-center">
            <input
              type="checkbox"
              v-model="publishNow"
              id="publish-now"
              class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
            />
            <label for="publish-now" class="ml-2 block text-sm text-gray-900">
              Publish immediately
            </label>
          </div>
          <div class="flex space-x-4">
            <button
              type="submit"
              class="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white px-6 py-3 rounded-lg font-medium transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105"
            >
              <i class="fas fa-save mr-2"></i> Save Blog
            </button>
            <button
              type="button"
              @click="resetForm"
              class="bg-gradient-to-r from-gray-500 to-gray-600 hover:from-gray-600 hover:to-gray-700 text-white px-6 py-3 rounded-lg font-medium transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105"
            >
              <i class="fas fa-undo mr-2"></i> Reset
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const title = ref('')
const subtitle = ref('')
const description = ref('')
const category = ref('')
const publishNow = ref(false)
const fileName = ref('')
const isGenerating = ref(false)

function onFileChange(event) {
  const file = event.target.files[0]
  if (file) {
    fileName.value = file.name
  }
  console.log(file)
}

import API from '../../services/api.js'

async function generateWithAI() {
  if (!title.value.trim()) {
    alert('Please enter a title first!')
    return
  }

  isGenerating.value = true
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
  } finally {
    isGenerating.value = false
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

import { useRouter } from 'vue-router'
const router = useRouter()

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

        const response = await API.post('/blogs/', formData, {
          headers: {
            ...headers,
            'Content-Type': 'multipart/form-data'
          }
        })

        alert('Blog added successfully!')
        resetForm()
        // Removed redirect to blog-list page as per user request
        // router.push('/blog-list')
      } catch (error) {
        console.error('Failed to add blog:', error)
        alert(error.response && error.response.data && error.response.data.details ? `Failed to add blog: ${error.response.data.details}` : 'Failed to add blog. Please try again.')
      }
    }
</script>


