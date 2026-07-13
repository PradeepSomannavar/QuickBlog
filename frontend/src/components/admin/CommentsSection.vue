<template>
  <div class="p-6 lg:p-8">
    <h1 class="text-2xl font-bold text-slate-900 dark:text-white mb-8">Comments Management</h1>

    <div v-if="loading" class="text-center py-12">
      <div class="inline-flex items-center gap-2 text-slate-400">
        <svg class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
        </svg>
        Loading comments...
      </div>
    </div>

    <div v-if="error" class="text-red-500 dark:text-red-400 bg-red-50 dark:bg-red-900/20 p-4 rounded-xl text-sm mb-6 border border-red-100 dark:border-red-900/30">{{ error }}</div>

    <div v-if="comments.length" class="card-premium overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="bg-slate-50 dark:bg-slate-800/50 border-b border-slate-100 dark:border-slate-800">
              <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">#</th>
              <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Blog ID</th>
              <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Name</th>
              <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Comment</th>
              <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Status</th>
              <th class="px-6 py-3 text-right text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
            <tr v-for="(comment, index) in comments" :key="comment.id" class="hover:bg-slate-50 dark:hover:bg-slate-800/30 transition-colors">
              <td class="px-6 py-4 whitespace-nowrap text-slate-500 dark:text-slate-400">{{ index + 1 }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-slate-700 dark:text-slate-300">{{ comment.blog_id }}</td>
              <td class="px-6 py-4 whitespace-nowrap font-medium text-slate-900 dark:text-white">{{ comment.name }}</td>
              <td class="px-6 py-4 text-slate-600 dark:text-slate-400 max-w-xs truncate" :title="comment.comment">{{ comment.comment }}</td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span :class="['inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium', comment.approved ? 'bg-emerald-50 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-900/30' : 'bg-amber-50 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400 border border-amber-200 dark:border-amber-900/30']">
                  {{ comment.approved ? 'Approved' : 'Pending' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right">
                <button @click="deleteComment(comment.id)" class="p-2 text-slate-400 hover:text-red-600 dark:hover:text-red-400 transition-colors rounded-lg hover:bg-red-50 dark:hover:bg-red-900/20" title="Delete">
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
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
        </svg>
      </div>
      <p class="text-slate-500 dark:text-slate-400">No comments found.</p>
    </div>
  </div>
</template>

<script>
import API from '../../services/api.js'

export default {
  name: "CommentsSection",
  data() {
    return {
      comments: [],
      loading: false,
      error: ""
    }
  },
  mounted() {
    this.fetchComments()
  },
  methods: {
    async fetchComments() {
      this.loading = true
      this.error = ""
      try {
        const token = localStorage.getItem('token')
        if (!token) {
          this.error = "No authorization token found. Please login."
          this.loading = false
          return
        }
        const headers = { Authorization: `Bearer ${token}` }
        const response = await API.get('/comments/', { headers })
        this.comments = response.data
      } catch (err) {
        this.error = "Failed to load comments."
        console.error('Error fetching comments:', err)
      } finally {
        this.loading = false
      }
    },
    async deleteComment(id) {
      if (!confirm('Are you sure you want to delete this comment?')) return
      try {
        const token = localStorage.getItem('token')
        if (!token) {
          this.error = "No authorization token found. Please login."
          return
        }
        const headers = { Authorization: `Bearer ${token}` }
        const response = await API.delete(`/comments/${id}`, { headers })
        if (response.status === 200) {
          this.fetchComments()
        } else {
          this.error = "Failed to delete comment."
          alert('Failed to delete comment.')
        }
      } catch (err) {
        this.error = "Failed to delete comment."
        console.error('Error deleting comment:', err)
        alert('Failed to delete comment.')
      }
    }
  }
}
</script>
