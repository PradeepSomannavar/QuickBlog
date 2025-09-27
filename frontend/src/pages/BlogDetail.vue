<template>
  <div class="max-w-4xl mx-auto px-6 py-12">
    <!-- Hero Section -->
    <div class="text-center mb-6 text-black">
      <h1 class="text-4xl font-bold mb-2">{{ blog.title }}</h1>
      <p class="text-gray-500 text-sm">📅 Published on {{ blog.date }}</p>
    </div>

    <!-- Blog Image -->
    <img
      :src="blog.image"
      alt="Blog Image"
      class="w-full h-80 object-cover rounded-lg shadow mb-6"
    />

    <!-- Subtitle -->
    <h2 class="text-xl font-semibold text-black mb-4">{{ blog.subtitle }}</h2>

    <!-- Blog Content -->
    <div class="prose max-w-none text-black leading-relaxed mb-12">
      <p v-for="(para, index) in blog.content" :key="index" class="mb-4">
        {{ para }}
      </p>
    </div>

    <!-- Comments Section -->
    <div class="mb-10">
      <h2 class="text-2xl font-bold mb-6 text-left text-black">Comments</h2>
      <div v-if="comments.length === 0" class="text-gray-500">No comments yet.</div>

      <div
        v-for="(comment, index) in comments"
        :key="index"
        class="border-b pb-4 mb-4 text-left text-black"
      >
        <p class="font-semibold text-black">
          {{ comment.name }}
          <span class="text-sm text-gray-500 ml-2">{{ comment.date }}</span>
          <button
            @click="deleteComment(comment.id)"
            class="ml-4 bg-red-600 hover:bg-red-700 text-white px-2 py-1 rounded text-xs"
          >
            Delete
          </button>
        </p>
        <p class="text-black">{{ comment.comment }}</p>
      </div>
    </div>

    <!-- Add Comment -->
    <div class="text-left">
      <h3 class="text-xl font-semibold mb-4 text-black">Add a Comment</h3>
      <input
        v-model="newComment.name"
        type="text"
        placeholder="Your Name"
        class="border rounded w-full p-2 mb-3 focus:outline-none focus:ring focus:ring-purple-300"
      />
      <textarea
        v-model="newComment.text"
        placeholder="Your Comment"
        class="border rounded w-full p-2 mb-3 focus:outline-none focus:ring focus:ring-purple-300"
      ></textarea>
      <button
        @click="addComment"
        class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition"
      >
        Submit
      </button>
    </div>
  </div>
</template>

<script>
import API from '../services/api.js'

export default {
  name: "BlogDetail",
  props: ["id"],
  data() {
    return {
      blog: {},
      comments: [],
      newComment: { name: "", text: "" },
      loadingComments: false,
      error: "",
    }
  },
  async created() {
    this.error = ""
    try {
      console.log("BlogDetail id prop:", this.id)
      const response = await API.get(`/blogs/${this.id}`)
      const data = response.data
      console.log("Fetched blog data:", data)
      this.blog = {
        id: data.id,
        title: data.title,
        subtitle: data.subtitle,
        image: data.thumbnail ? `http://127.0.0.1:5000/static/uploads/${data.thumbnail}` : '',
        date: new Date(data.created_at).toLocaleDateString(),
        content: data.description ? data.description.split('\n') : [],
      }
    } catch (err) {
      this.error = "Failed to load blog details."
      console.error(err)
    }

    await this.fetchComments()
  },
  methods: {
    async fetchComments() {
      this.loadingComments = true
      this.error = ""
      try {
        const response = await API.get('/comments/public')
        const data = response.data
        console.log('Fetched comments:', data)
        // Filter comments for this blog and only approved ones
        this.comments = data
          .filter(c => c.blog_id == this.blog.id && c.approved)
          .map(c => ({
            ...c,
            date: new Date(c.created_at).toLocaleDateString()
          }))
      } catch (err) {
        this.error = "Failed to load comments."
        console.error(err)
      } finally {
        this.loadingComments = false
      }
    },
    async addComment() {
      if (!this.newComment.name || !this.newComment.text) return
      try {
        const response = await API.post('/comments/', {
          blog_id: this.blog.id,
          name: this.newComment.name,
          comment: this.newComment.text,
        })
        // Optimistically add comment to list
        this.comments.push({
          blog_id: this.blog.id,
          name: this.newComment.name,
          comment: this.newComment.text,
          approved: true,
          date: new Date().toLocaleDateString(),
        })
        this.newComment = { name: "", text: "" }
      } catch (err) {
        alert('Failed to submit comment. Please try again.')
        console.error(err)
      }
    },
  },
  methods: {
    async fetchComments() {
      this.loadingComments = true
      this.error = ""
      try {
        const response = await API.get('/comments/public')
        const data = response.data
        console.log('Fetched comments:', data)
        // Filter comments for this blog and only approved ones
        this.comments = data
          .filter(c => c.blog_id == this.blog.id && c.approved)
          .map(c => ({
            ...c,
            date: new Date(c.created_at).toLocaleDateString()
          }))
      } catch (err) {
        this.error = "Failed to load comments."
        console.error(err)
      } finally {
        this.loadingComments = false
      }
    },
    async addComment() {
      if (!this.newComment.name || !this.newComment.text) return
      try {
        const response = await API.post('/comments/', {
          blog_id: this.blog.id,
          name: this.newComment.name,
          comment: this.newComment.text,
        })
        // Optimistically add comment to list
        this.comments.push({
          blog_id: this.blog.id,
          name: this.newComment.name,
          comment: this.newComment.text,
          approved: true,
          date: new Date().toLocaleDateString(),
        })
        this.newComment = { name: "", text: "" }
      } catch (err) {
        alert('Failed to submit comment. Please try again.')
        console.error(err)
      }
    },
    async deleteComment(id) {
      try {
        const token = localStorage.getItem('token')
        if (!token) {
          alert('You must be logged in to delete comments.')
          return
        }
        const headers = { Authorization: `Bearer ${token}` }
        const response = await API.delete(`/comments/${id}`, { headers })
        console.log('Delete response:', response)
        if (response.status === 200) {
          await this.fetchComments()
        } else {
          alert('Failed to delete comment. Please check console for details.')
        }
      } catch (err) {
        alert('Failed to delete comment. Please check console for details.')
        console.error('Error deleting comment:', err)
      }
    }
  }
}
</script>
