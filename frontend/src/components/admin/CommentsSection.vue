<template>
  <div class="p-6">
    <h2 class="text-3xl font-bold mb-6 text-gray-800">Comments Management</h2>
    <div v-if="loading" class="text-gray-500 text-center py-8">Loading comments...</div>
    <div v-if="error" class="text-red-600 bg-red-50 p-4 rounded-lg">{{ error }}</div>
    <div v-if="comments.length" class="bg-white rounded-xl shadow-xl overflow-hidden border border-gray-200">
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gradient-to-r from-blue-600 to-blue-700 text-white">
            <tr>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">ID</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Blog ID</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Name</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Comment</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Approved</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="(comment, index) in comments" :key="comment.id" class="hover:bg-gradient-to-r hover:from-gray-50 hover:to-blue-50 transition-colors duration-200">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 text-center">{{ index + 1 }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-center">{{ comment.blog_id }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ comment.name }}</td>
              <td class="px-6 py-4 text-sm text-gray-500 max-w-xs truncate" :title="comment.comment">{{ comment.comment }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-center">
                <span :class="['px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full', comment.approved ? 'bg-green-100 text-green-800 border border-green-200' : 'bg-yellow-100 text-yellow-800 border border-yellow-200']">
                  {{ comment.approved ? 'Approved' : 'Pending' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-center">
                <button @click="deleteComment(comment.id)" class="text-red-600 hover:text-red-800 p-2 rounded-full hover:bg-red-100 transition-all duration-200" title="Delete">
                  <i class="fas fa-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else class="text-gray-600 text-center py-8">No comments found.</div>
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
        console.log('Token for fetching comments:', token)
        if (!token) {
          this.error = "No authorization token found. Please login."
          this.loading = false
          return
        }
        const headers = { Authorization: `Bearer ${token}` }
        const response = await API.get('/comments/', { headers })
        console.log('Fetched comments:', response.data)
        this.comments = response.data
      } catch (err) {
        this.error = "Failed to load comments."
        console.error('Error fetching comments:', err)
        alert('Failed to load comments. Please check console for details.')
      } finally {
        this.loading = false
      }
    },
    async deleteComment(id) {
      if (!confirm('Are you sure you want to delete this comment?')) return
      console.log('deleteComment method triggered for id:', id)
      try {
        const token = localStorage.getItem('token')
        if (!token) {
          this.error = "No authorization token found. Please login."
          return
        }
        const headers = { Authorization: `Bearer ${token}` }
        const response = await API.delete(`/comments/${id}`, { headers })
        console.log('Delete response:', response)
        if (response.status === 200) {
          this.fetchComments()
        } else {
          this.error = "Failed to delete comment."
          alert('Failed to delete comment. Please check console for details.')
        }
      } catch (err) {
        this.error = "Failed to delete comment."
        console.error('Error deleting comment:', err)
        alert('Failed to delete comment. Please check console for details.')
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
  font-size: 14px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid #ddd;
  color: #000000; /* Set text color to black for visibility */
}
th, td {
  text-align: left;
  padding: 12px 16px;
  border-bottom: 1px solid #e2e8f0;
  border-right: 1px solid #e2e8f0;
  color: #000000; /* Set text color to black for visibility */
}
th {
  background-color: #2d3748;
  color: #edf2f7;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
tbody tr:hover {
  background-color: #f7fafc;
  cursor: pointer;
}
button {
  cursor: pointer;
}
</style>
