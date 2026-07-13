<template>
  <aside class="bg-slate-900 text-slate-300 w-64 min-h-screen flex flex-col shrink-0">
    <div class="flex items-center gap-3 px-6 py-5 border-b border-slate-800">
      <div class="w-9 h-9 bg-brand-600 rounded-xl flex items-center justify-center shrink-0 shadow-sm shadow-brand-600/20">
        <span class="text-white font-bold text-sm">Q</span>
      </div>
      <div>
        <h2 class="text-sm font-bold text-white">QuickBlog</h2>
        <p class="text-xs text-slate-500">Admin Panel</p>
      </div>
    </div>
    <nav class="flex-1 p-4 space-y-1">
      <button
        v-for="item in navItems"
        :key="item.id"
        @click="currentSection = item.id"
        :class="[
          'w-full flex items-center gap-3 px-4 py-2.5 text-sm font-medium rounded-xl transition-all duration-200 text-left',
          currentSection === item.id
            ? 'bg-brand-600 text-white shadow-sm shadow-brand-600/20'
            : 'text-slate-400 hover:text-white hover:bg-slate-800/50'
        ]"
      >
        <span v-html="item.icon" class="w-5 h-5 shrink-0"></span>
        {{ item.label }}
      </button>
    </nav>
    <div class="p-4 border-t border-slate-800">
      <button
        @click="logout"
        class="w-full flex items-center gap-3 px-4 py-2.5 text-sm font-medium rounded-xl text-slate-400 hover:text-white hover:bg-slate-800/50 transition-all duration-200 text-left"
      >
        <svg class="w-5 h-5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
        </svg>
        Logout
      </button>
    </div>
  </aside>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'

const emits = defineEmits(['update-section'])
const router = useRouter()

const currentSection = ref('dashboard')

const navItems = [
  { id: 'dashboard', label: 'Dashboard', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zm10 0a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zm10 0a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>' },
  { id: 'addBlog', label: 'Add Blog', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>' },
  { id: 'blogList', label: 'Blog List', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"/></svg>' },
  { id: 'comments', label: 'Comments', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>' },
  { id: 'subscribers', label: 'Subscribers', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/></svg>' },
]

function logout() {
  localStorage.removeItem('token')
  router.push('/login')
}

watch(currentSection, (newSection) => {
  emits('update-section', newSection)
})
</script>
