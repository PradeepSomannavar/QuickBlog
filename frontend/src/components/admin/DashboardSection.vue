<template>
  <div class="p-6">
    <h2 class="text-3xl font-bold mb-6 text-gray-800">Dashboard Overview</h2>
    <div v-if="loading" class="text-gray-500 text-center py-8">Loading dashboard data...</div>
    <div v-if="error" class="text-red-600 bg-red-50 p-4 rounded-lg">{{ error }}</div>
    <div v-if="dashboardData" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 border border-blue-200">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-lg font-semibold mb-2 text-blue-800">Total Blogs</h3>
            <p class="text-4xl font-bold text-blue-600">{{ dashboardData.blogs }}</p>
          </div>
          <div class="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center">
            <i class="fas fa-blog text-white text-xl"></i>
          </div>
        </div>
      </div>
      <div class="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 border border-green-200">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-lg font-semibold mb-2 text-green-800">Total Subscribers</h3>
            <p class="text-4xl font-bold text-green-600">{{ dashboardData.subscribers }}</p>
          </div>
          <div class="w-12 h-12 bg-green-500 rounded-full flex items-center justify-center">
            <i class="fas fa-users text-white text-xl"></i>
          </div>
        </div>
      </div>
      <div class="bg-gradient-to-br from-red-50 to-red-100 p-6 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 border border-red-200">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-lg font-semibold mb-2 text-red-800">Total Comments</h3>
            <p class="text-4xl font-bold text-red-600">{{ dashboardData.comments }}</p>
          </div>
          <div class="w-12 h-12 bg-red-500 rounded-full flex items-center justify-center">
            <i class="fas fa-comments text-white text-xl"></i>
          </div>
        </div>
      </div>
      <div class="bg-gradient-to-br from-purple-50 to-purple-100 p-6 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 border border-purple-200">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-lg font-semibold mb-2 text-purple-800">Total Visitors</h3>
            <p class="text-4xl font-bold text-purple-600">{{ dashboardData.total_visitors }}</p>
          </div>
          <div class="w-12 h-12 bg-purple-500 rounded-full flex items-center justify-center">
            <i class="fas fa-eye text-white text-xl"></i>
          </div>
        </div>
      </div>
    </div>
    <div class="mt-6 bg-white p-6 rounded shadow">
      <h3 class="text-lg font-semibold mb-4 text-gray-700">To Do List</h3>
      <form @submit.prevent="addTask" class="mb-4">
        <div class="flex gap-2">
          <input v-model="newTask" type="text" placeholder="Add a new task..." class="flex-1 p-2 border border-gray-300 rounded bg-black text-white" required>
          <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">Add</button>
        </div>
      </form>
      <ul class="space-y-2">
        <li v-for="(task, index) in tasks" :key="task.id" class="flex justify-between items-center p-2 border border-gray-200 rounded">
          <span class="text-black">{{ task.text }}</span>
          <button @click="deleteTask(index)" class="text-red-600 hover:text-red-800 p-1 rounded hover:bg-red-100 transition-all duration-200" title="Delete">
            <i class="fas fa-trash"></i>
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

<style scoped>
.bg-white {
  background-color: white;
}
.shadow {
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
.rounded {
  border-radius: 6px;
}
.p-4 {
  padding: 1rem;
}
.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}
.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}
.font-semibold {
  font-weight: 600;
}
.mb-2 {
  margin-bottom: 0.5rem;
}
.mb-4 {
  margin-bottom: 1rem;
}
.grid {
  display: grid;
}
.grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr));
}
.md\:grid-cols-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}
.gap-6 {
  gap: 1.5rem;
}
.text-gray-500 {
  color: #6b7280;
}
.text-red-600 {
  color: #dc2626;
}
</style>
