<template>
  <div class="p-6 lg:p-8">
    <h1 class="text-2xl font-bold text-slate-900 dark:text-white mb-8">Dashboard Overview</h1>

    <div v-if="loading" class="text-center py-12">
      <div class="inline-flex items-center gap-2 text-slate-400">
        <svg class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
        </svg>
        Loading dashboard data...
      </div>
    </div>

    <div v-if="error" class="text-red-500 dark:text-red-400 bg-red-50 dark:bg-red-900/20 p-4 rounded-xl text-sm border border-red-100 dark:border-red-900/30">{{ error }}</div>

    <div v-if="dashboardData" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="card-premium p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-500 dark:text-slate-400">Total Blogs</p>
            <p class="text-3xl font-bold text-slate-900 dark:text-white mt-1">{{ dashboardData.blogs }}</p>
          </div>
          <div class="w-10 h-10 bg-brand-50 dark:bg-brand-900/30 rounded-xl flex items-center justify-center border border-brand-100 dark:border-brand-900/30">
            <svg class="w-5 h-5 text-brand-600 dark:text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
            </svg>
          </div>
        </div>
      </div>
      <div class="card-premium p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-500 dark:text-slate-400">Subscribers</p>
            <p class="text-3xl font-bold text-slate-900 dark:text-white mt-1">{{ dashboardData.subscribers }}</p>
          </div>
          <div class="w-10 h-10 bg-emerald-50 dark:bg-emerald-900/30 rounded-xl flex items-center justify-center border border-emerald-100 dark:border-emerald-900/30">
            <svg class="w-5 h-5 text-emerald-600 dark:text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
            </svg>
          </div>
        </div>
      </div>
      <div class="card-premium p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-500 dark:text-slate-400">Comments</p>
            <p class="text-3xl font-bold text-slate-900 dark:text-white mt-1">{{ dashboardData.comments }}</p>
          </div>
          <div class="w-10 h-10 bg-amber-50 dark:bg-amber-900/30 rounded-xl flex items-center justify-center border border-amber-100 dark:border-amber-900/30">
            <svg class="w-5 h-5 text-amber-600 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
          </div>
        </div>
      </div>
      <div class="card-premium p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-500 dark:text-slate-400">Visitors</p>
            <p class="text-3xl font-bold text-slate-900 dark:text-white mt-1">{{ dashboardData.total_visitors }}</p>
          </div>
          <div class="w-10 h-10 bg-violet-50 dark:bg-violet-900/30 rounded-xl flex items-center justify-center border border-violet-100 dark:border-violet-900/30">
            <svg class="w-5 h-5 text-violet-600 dark:text-violet-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
          </div>
        </div>
      </div>
    </div>

    <div class="card-premium mt-8 p-6">
      <h3 class="text-lg font-semibold text-slate-900 dark:text-white mb-4">To Do List</h3>
      <form @submit.prevent="addTask" class="flex gap-2 mb-4">
        <input v-model="newTask" type="text" placeholder="Add a new task..." class="input flex-1">
        <button type="submit" class="btn-primary shrink-0">Add</button>
      </form>
      <ul class="space-y-2">
        <li v-for="(task, index) in tasks" :key="task.id" class="flex items-center justify-between p-3 bg-slate-50 dark:bg-slate-800/50 rounded-xl">
          <span class="text-sm text-slate-700 dark:text-slate-300">{{ task.text }}</span>
          <button @click="deleteTask(index)" class="text-slate-400 hover:text-red-500 dark:hover:text-red-400 transition-colors p-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
            </svg>
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import API from '../../services/api.js'

export default {
  name: "DashboardSection",
  data() {
    return {
      dashboardData: null,
      loading: false,
      error: "",
      tasks: [],
      newTask: ""
    }
  },
  mounted() {
    this.fetchDashboardData()
    this.loadTasks()
  },
  methods: {
    async fetchDashboardData() {
      this.loading = true
      this.error = ""
      try {
        const token = localStorage.getItem('token')
        const headers = token ? { Authorization: `Bearer ${token}` } : {}
        const response = await API.get('/dashboard/stats', { headers })
        this.dashboardData = response.data
      } catch (err) {
        this.error = "Failed to load dashboard data."
        console.error('Error fetching dashboard data:', err)
      } finally {
        this.loading = false
      }
    },
    addTask() {
      if (this.newTask.trim()) {
        this.tasks.push({ id: Date.now(), text: this.newTask.trim() })
        this.saveTasks()
        this.newTask = ""
      }
    },
    deleteTask(index) {
      this.tasks.splice(index, 1)
      this.saveTasks()
    },
    saveTasks() {
      localStorage.setItem('adminTasks', JSON.stringify(this.tasks))
    },
    loadTasks() {
      const saved = localStorage.getItem('adminTasks')
      if (saved) {
        this.tasks = JSON.parse(saved)
      }
    },
  }
}
</script>
