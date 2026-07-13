<template>
  <div class="p-6 lg:p-8">
    <div class="flex items-center justify-between mb-8">
      <h1 class="text-2xl font-bold text-slate-900 dark:text-white">Subscribers</h1>
      <button @click="fetchSubscribers" class="btn-outline text-sm" :disabled="loading">
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
        </svg>
        Refresh
      </button>
    </div>

    <div v-if="loading" class="text-center py-12">
      <div class="inline-flex items-center gap-2 text-slate-400">
        <svg class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
        </svg>
        Loading subscribers...
      </div>
    </div>

    <div v-if="error" class="text-red-500 dark:text-red-400 bg-red-50 dark:bg-red-900/20 p-4 rounded-xl text-sm mb-6 border border-red-100 dark:border-red-900/30">{{ error }}</div>

    <div v-if="subscribers.length" class="card-premium overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="bg-slate-50 dark:bg-slate-800/50 border-b border-slate-100 dark:border-slate-800">
              <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">#</th>
              <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Email</th>
              <th class="px-6 py-3 text-right text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
            <tr v-for="(sub, index) in subscribers" :key="sub.id" class="hover:bg-slate-50 dark:hover:bg-slate-800/30 transition-colors">
              <td class="px-6 py-4 whitespace-nowrap text-slate-500 dark:text-slate-400">{{ index + 1 }}</td>
              <td class="px-6 py-4 whitespace-nowrap font-medium text-slate-900 dark:text-white">{{ sub.email }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-right">
                <button @click="deleteSubscriber(sub.id)" class="p-2 text-slate-400 hover:text-red-600 dark:hover:text-red-400 transition-colors rounded-lg hover:bg-red-50 dark:hover:bg-red-900/20" title="Delete">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else-if="!loading" class="text-center py-12">
      <div class="w-12 h-12 mx-auto mb-3 rounded-xl bg-slate-100 dark:bg-slate-800 flex items-center justify-center">
        <svg class="w-6 h-6 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
        </svg>
      </div>
      <p class="text-slate-500 dark:text-slate-400">No subscribers found.</p>
    </div>
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
        const token = localStorage.getItem('token')
        const headers = token ? { Authorization: `Bearer ${token}` } : {}
        const response = await API.get('/subscribers/', { headers })
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
