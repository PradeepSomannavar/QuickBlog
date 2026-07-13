<template>
  <div class="grid md:grid-cols-2 gap-12 items-start">
    <div class="space-y-6 animate-in">
      <div class="flex items-start gap-4" v-for="item in contactInfo" :key="item.title">
        <div class="w-11 h-11 bg-brand-50 dark:bg-brand-900/30 rounded-xl flex items-center justify-center shrink-0 border border-brand-100 dark:border-brand-900/30">
          <svg class="w-5 h-5 text-brand-600 dark:text-brand-400" fill="none" stroke="currentColor" :viewBox="item.icon">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.path"/>
          </svg>
        </div>
        <div>
          <h3 class="font-semibold text-slate-900 dark:text-white text-sm">{{ item.title }}</h3>
          <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">{{ item.value }}</p>
        </div>
      </div>
    </div>
    <form class="card-premium p-6 animate-in animate-in-delay-1" @submit.prevent="submitContact">
      <div class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Name</label>
          <input type="text" placeholder="Your name" v-model="form.name" class="input" required>
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Email</label>
          <input type="email" placeholder="your@email.com" v-model="form.email" class="input" required>
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Message</label>
          <textarea rows="4" placeholder="Your message..." v-model="form.message" class="input resize-none" required></textarea>
        </div>
        <p v-if="success" class="text-green-600 dark:text-green-400 text-sm">{{ success }}</p>
        <p v-if="error" class="text-red-500 dark:text-red-400 text-sm">{{ error }}</p>
        <button type="submit" class="btn-primary w-full" :disabled="sending">
          {{ sending ? 'Sending...' : 'Send Message' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import API from '@/services/api.js'

export default {
  name: "ContactSection",
  data() {
    return {
      form: { name: "", email: "", message: "" },
      sending: false,
      success: "",
      error: "",
      contactInfo: [
        { title: "Email Us", value: "contact@quickblog.com", icon: "0 0 24 24", path: "M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" },
        { title: "Call Us", value: "+1 (555) 123-4567", icon: "0 0 24 24", path: "M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" },
        { title: "Visit Us", value: "123 Blog Street, Content City", icon: "0 0 24 24", path: "M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0zM15 11a3 3 0 11-6 0 3 3 0 016 0z" },
      ]
    }
  },
  methods: {
    async submitContact() {
      this.sending = true
      this.success = ""
      this.error = ""
      try {
        await API.post('/contacts/', {
          name: this.form.name,
          email: this.form.email,
          message: this.form.message,
        })
        this.success = "Message sent! We'll get back to you soon."
        this.form = { name: "", email: "", message: "" }
      } catch {
        this.error = "Failed to send. Please try again."
      } finally {
        this.sending = false
      }
    }
  }
}
</script>
