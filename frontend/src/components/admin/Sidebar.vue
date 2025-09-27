<template>
  <aside class="bg-gradient-to-b from-gray-800 to-gray-900 text-white w-64 min-h-screen p-6 shadow-xl">
    <div class="flex items-center mb-8">
      <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-orange-500 rounded-lg flex items-center justify-center mr-3">
        <i class="fas fa-cog text-white"></i>
      </div>
      <h2 class="text-2xl font-bold">Admin Panel</h2>
    </div>
    <nav>
      <ul class="space-y-2">
        <li @click="currentSection='dashboard'" :class="['flex items-center p-4 rounded-lg cursor-pointer transition-all duration-300 transform', currentSection==='dashboard' ? 'bg-gradient-to-r from-blue-600 to-blue-700 text-white shadow-lg scale-105' : 'hover:bg-gray-700 hover:scale-102']">
          <i class="fas fa-tachometer-alt mr-3 text-lg"></i> Dashboard
        </li>
        <li @click="currentSection='addBlog'" :class="['flex items-center p-4 rounded-lg cursor-pointer transition-all duration-300 transform', currentSection==='addBlog' ? 'bg-gradient-to-r from-blue-600 to-blue-700 text-white shadow-lg scale-105' : 'hover:bg-gray-700 hover:scale-102']">
          <i class="fas fa-plus mr-3 text-lg"></i> Add Blog
        </li>
        <li @click="currentSection='blogList'" :class="['flex items-center p-4 rounded-lg cursor-pointer transition-all duration-300 transform', currentSection==='blogList' ? 'bg-gradient-to-r from-blue-600 to-blue-700 text-white shadow-lg scale-105' : 'hover:bg-gray-700 hover:scale-102']">
          <i class="fas fa-list mr-3 text-lg"></i> Blog List
        </li>
        <li @click="currentSection='comments'" :class="['flex items-center p-4 rounded-lg cursor-pointer transition-all duration-300 transform', currentSection==='comments' ? 'bg-gradient-to-r from-blue-600 to-blue-700 text-white shadow-lg scale-105' : 'hover:bg-gray-700 hover:scale-102']">
          <i class="fas fa-comments mr-3 text-lg"></i> Comments
        </li>
        <li @click="currentSection='subscribers'" :class="['flex items-center p-4 rounded-lg cursor-pointer transition-all duration-300 transform', currentSection==='subscribers' ? 'bg-gradient-to-r from-blue-600 to-blue-700 text-white shadow-lg scale-105' : 'hover:bg-gray-700 hover:scale-102']">
          <i class="fas fa-users mr-3 text-lg"></i> Subscribers
        </li>
        <li @click="logout" class="flex items-center p-4 rounded-lg cursor-pointer hover:bg-gradient-to-r hover:from-red-600 hover:to-red-700 transition-all duration-300 transform hover:scale-102">
          <i class="fas fa-sign-out-alt mr-3 text-lg"></i> Logout
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script setup>
import { ref, watch } from 'vue'
import { defineEmits } from 'vue'
const emits = defineEmits(['update-section'])

const currentSection = ref('dashboard')

import { useRouter } from 'vue-router'
const router = useRouter()

function logout() {
  console.log('Logging out...')
  localStorage.removeItem('token')
  router.push('/login')
}

watch(currentSection, (newSection) => {
  emits('update-section', newSection)
})
</script>

<style scoped>
.sidebar {
  width: 220px;
  height: 100vh;
  background: #1f1f1f;
  color: white;
  padding: 20px;
  display: flex;
  flex-direction: column;
}
.logo {
  font-size: 24px;
  margin-bottom: 40px;
  font-weight: bold;
  text-align: center;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  padding: 12px 15px;
  margin-bottom: 10px;
  cursor: pointer;
  border-radius: 8px;
  transition: 0.2s;
}
li:hover, .active {
  background: #333;
}
</style>
