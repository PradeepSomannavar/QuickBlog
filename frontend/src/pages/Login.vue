<template>
  <div class="min-h-screen bg-slate-50 dark:bg-[#020617] flex items-center justify-center px-4">
    <div class="card-premium w-full max-w-md p-8 animate-in">
      <div class="text-center mb-8">
        <button @click="$router.push('/')" class="w-14 h-14 bg-brand-600 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-sm shadow-brand-600/20 hover:shadow-md hover:shadow-brand-600/30 transition-all duration-300">
          <span class="text-white font-bold text-xl">Q</span>
        </button>
        <h1 class="text-2xl font-bold text-slate-900 dark:text-white">Welcome Back</h1>
        <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Sign in to your admin account</p>
      </div>
      <form @submit.prevent="handleLogin" class="space-y-5">
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Username</label>
          <input v-model="username" type="text" placeholder="Enter your username" class="input" required />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Password</label>
          <div class="relative">
            <input v-model="password" :type="showPassword ? 'text' : 'password'" placeholder="Enter your password" class="input pr-12" required />
            <button type="button" class="absolute right-2 top-1/2 -translate-y-1/2 p-1.5 text-slate-400 hover:text-slate-600 dark:hover:text-slate-300 transition-colors" @click="showPassword = !showPassword">
              <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
              </svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/>
              </svg>
            </button>
          </div>
        </div>
        <button type="submit" class="btn-primary w-full py-3">
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/></svg>
          Sign In
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  name: "LoginPage",
  setup() {
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
        router.push('/admin')
      } catch {
        alert('Invalid credentials!')
      }
    }

    return { username, password, showPassword, handleLogin }
  }
}
</script>
