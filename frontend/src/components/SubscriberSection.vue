s issue
<template>
  <section>
    <div class="max-w-2xl mx-auto text-center">
      <h2 class="text-2xl font-bold text-gray-800 mb-4">
        Subscribe to QuickBlog
      </h2>
      <p class="text-gray-600 mb-6">
        Get the latest articles straight to your inbox.
      </p>

      <form @submit.prevent="subscribe" class="flex flex-col sm:flex-row gap-3">
        <input
          type="email"
          v-model="email"
          placeholder="Enter your email"
          class="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-white bg-gray-800 placeholder-gray-400"
          required
        />
        <button
          type="submit"
          class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
        >
          Subscribe
        </button>
      </form>

      <p v-if="success" class="text-green-600 mt-4">{{ success }}</p>
      <p v-if="error" class="text-red-600 mt-4">{{ error }}</p>
    </div>
  </section>
</template>

<script>
import API from '../services/api.js'

export default {
  name: "SubscriberSection",
  data() {
    return {
      email: "",
      success: "",
      error: ""
    }
  },
  methods: {
    async subscribe() {
      if (!this.email.includes("@")) {
        this.error = "Please enter a valid email address."
        this.success = ""
        return
      }

      try {
        const response = await API.post('/subscribers/', { email: this.email })
        if (response.status === 200 || response.status === 201) {
          this.success = "Thanks for subscribing! 🎉"
          this.error = ""
          this.email = ""
        } else {
          this.error = response.data?.error || "Subscription failed. Please try again."
          this.success = ""
        }
      } catch (error) {
        console.error("Subscription error:", error)
        this.error = error.response?.data?.error || "Subscription failed. Please try again."
        if (!this.error) {
          this.error = "Subscription failed. Please try again."
        }
        this.success = ""
      }
    }
  }
}
</script>
