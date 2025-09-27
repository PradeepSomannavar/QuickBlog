<template>
  <div class="flex items-center justify-center min-h-screen bg-gradient-to-br from-indigo-200 via-blue-100 to-indigo-200 px-4">
    <div class="bg-white shadow-2xl rounded-2xl p-10 w-full max-w-md transform transition-all duration-300 hover:scale-105">
      <!-- Logo + Title -->
      <div class="flex flex-col items-center mb-8">
        <img src="../assets/admin.png" alt="QuickBlog Logo" class="w-20 h-20 mb-4 rounded-full shadow-lg" />
        <h2 class="text-3xl font-extrabold text-gray-900">Welcome Back</h2>   
      </div>

      <!-- Form -->
      <form @submit.prevent="handleLogin" class="space-y-6">
        <!-- Username -->
        <div>
          <label class="block text-gray-700 mb-2 font-semibold">Username</label>
          <input
            v-model="username"
            type="text"
            placeholder="Enter your username"
            class="w-full px-5 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-4 focus:ring-indigo-300 focus:border-transparent transition-all duration-300 shadow-sm"
            required
          />
        </div>

        <!-- Password -->
        <div>
          <label class="block text-gray-700 mb-2 font-semibold">Password</label>
          <div class="relative">
            <input
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="Enter your password"
              class="w-full px-5 py-3 pr-14 border border-gray-300 rounded-xl focus:outline-none focus:ring-4 focus:ring-indigo-300 focus:border-transparent transition-all duration-300 shadow-sm"
              required
            />
            <button
              type="button"
              class="absolute right-3 top-1/2 transform -translate-y-1/2 bg-gray-400 rounded-md p-2 text-white hover:bg-gray-600 transition-colors shadow-md"
              @click="showPassword = !showPassword"
              :aria-label="showPassword ? 'Hide password' : 'Show password'"
            >
              <i :class="showPassword ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
            </button>
          </div>
        </div>

        <!-- Login Button -->
        <button
          type="submit"
          class="w-full bg-indigo-600 text-white py-3 rounded-xl hover:bg-indigo-700 transition-all duration-300 font-bold shadow-lg hover:shadow-xl transform hover:scale-105"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const showPassword = ref(false)
const router = useRouter()

async function handleLogin() {
  try {
    const res = await axios.post('http://127.0.0.1:5000/api/auth/login', {
      username: username.value,
      password: password.value,
    })
    localStorage.setItem('token', res.data.access_token)
    alert('Login successful!')
    router.push('/admin') // redirect to admin dashboard
  } catch (err) {
    alert('Invalid credentials!')
  }
}
</script>
