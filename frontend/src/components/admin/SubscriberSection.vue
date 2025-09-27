<template>
  <div class="p-6">
    <h2 class="text-3xl font-bold mb-6 text-gray-800 flex items-center justify-between">
      Subscribers
      <button
        @click="fetchSubscribers"
        class="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105"
        :disabled="loading"
      >
        <i class="fas fa-refresh mr-2"></i> Refresh
      </button>
    </h2>
    <div v-if="loading" class="text-gray-500 text-center py-8">Loading subscribers...</div>
    <div v-if="error" class="text-red-600 bg-red-50 p-4 rounded-lg">{{ error }}</div>
    <div v-if="subscribers.length" class="bg-white rounded-xl shadow-xl overflow-hidden border border-gray-200">
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gradient-to-r from-blue-600 to-blue-700 text-white">
            <tr>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">ID</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Email</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="(sub, index) in subscribers" :key="sub.id" class="hover:bg-gradient-to-r hover:from-gray-50 hover:to-blue-50 transition-colors duration-200">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 text-center">{{ index + 1 }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ sub.email }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-center">
                <button @click="deleteSubscriber(sub.id)" class="text-red-600 hover:text-red-800 p-2 rounded-full hover:bg-red-100 transition-all duration-200" title="Delete">
                  <i class="fas fa-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else class="text-gray-600 text-center py-8">No subscribers found.</div>
  </div>
</template>

<script>
import API from '../../services/api.js'

export default {
  name: "SubscriberSection",
  data() {
    return {
      subscribers: [],
      loading: false,
      error: ""
    }
  },
  mounted() {
    this.fetchSubscribers()
  },
  methods: {
    async fetchSubscribers() {
      this.loading = true
      this.error = ""
      try {
        // Add Authorization header with token if available
        const token = localStorage.getItem('token')
        const headers = token ? { Authorization: `Bearer ${token}` } : {}

        const response = await API.get('/subscribers/', { headers })
        console.log('Subscribers API response:', response)
        this.subscribers = response.data
      } catch (err) {
        this.error = "Failed to load subscribers."
        console.error('Error fetching subscribers:', err)
      } finally {
        this.loading = false
      }
    },
    async deleteSubscriber(id) {
      if (!confirm('Are you sure you want to delete this subscriber?')) return
      try {
        const token = localStorage.getItem('token')
        const headers = token ? { Authorization: `Bearer ${token}` } : {}
        await API.delete(`/subscribers/${id}`, { headers })
        this.fetchSubscribers()
      } catch (err) {
        this.error = "Failed to delete subscriber."
        console.error('Error deleting subscriber:', err)
      }
    }
  }
}
</script>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 15px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid #ddd;
  color: #2d3748; /* Dark text for table body */
}
th, td {
  text-align: left;
  padding: 12px 16px;
  border-bottom: 1px solid #e2e8f0;
  border-right: 1px solid #e2e8f0;
  color: #2d3748; /* Dark text for cells */
}
th {
  background-color: #2d3748; /* Darker gray */
  color: #edf2f7; /* Light gray */
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
tbody tr:hover {
  background-color: #f7fafc; /* Light hover */
  cursor: pointer;
}
</style>
