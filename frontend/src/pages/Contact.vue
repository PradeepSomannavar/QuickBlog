<template>
  <div>
    <Navbar />
    <div class="pt-24 lg:pt-28">
      <section class="relative py-20 lg:py-28 bg-slate-50/50 dark:bg-[#0f172a]/30 border-b border-slate-100 dark:border-slate-800/60">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center animate-in">
          <span class="badge-brand mb-4 inline-block">Get in Touch</span>
          <h1 class="section-heading mb-4">Contact <span class="text-brand-600">Us</span></h1>
          <p class="section-subheading mx-auto text-lg">
            Have questions or feedback? We'd love to hear from you.
          </p>
        </div>
      </section>

      <section class="py-20 lg:py-28">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 grid md:grid-cols-2 gap-12 lg:gap-16">
          <div class="animate-in">
            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mb-4">Let's talk</h2>
            <p class="text-slate-500 dark:text-slate-400 leading-relaxed mb-6">
              We are available for questions, feedback, or collaboration opportunities. Let us know how we can help!
            </p>
            <div class="space-y-4">
              <div class="flex items-center gap-3 text-sm text-slate-500 dark:text-slate-400">
                <div class="w-10 h-10 rounded-xl bg-brand-50 dark:bg-brand-900/30 flex items-center justify-center shrink-0">
                  <svg class="w-5 h-5 text-brand-600 dark:text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                </div>
                <a href="mailto:contact@quickblog.com" class="hover:text-brand-600 dark:hover:text-brand-400 transition-colors">contact@quickblog.com</a>
              </div>
              <div class="flex items-center gap-3 text-sm text-slate-500 dark:text-slate-400">
                <div class="w-10 h-10 rounded-xl bg-brand-50 dark:bg-brand-900/30 flex items-center justify-center shrink-0">
                  <svg class="w-5 h-5 text-brand-600 dark:text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                </div>
                <span>QuickBlog HQ</span>
              </div>
            </div>
          </div>
          <form class="card-premium p-6 lg:p-8 space-y-5 animate-in animate-in-delay-1" @submit.prevent="submitContact">
            <div>
              <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Name</label>
              <input v-model="form.name" type="text" placeholder="Your Name" required class="input">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Email</label>
              <input v-model="form.email" type="email" placeholder="your@email.com" required class="input">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Subject</label>
              <input v-model="form.subject" type="text" placeholder="What's this about?" class="input">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">Message</label>
              <textarea v-model="form.message" rows="4" placeholder="Tell us everything..." required class="input resize-none"></textarea>
            </div>
            <div class="flex items-center gap-2">
              <input id="recaptcha" type="checkbox" v-model="form.recaptcha" required class="w-4 h-4 rounded border-slate-300 dark:border-slate-600 text-brand-600 focus:ring-brand-500">
              <label for="recaptcha" class="text-sm text-slate-500 dark:text-slate-400 select-none">I'm not a robot</label>
            </div>
            <button type="submit" class="btn-primary w-full py-3">
              Send Message
              <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/></svg>
            </button>
          </form>
        </div>
      </section>
    </div>
    <FooterSection />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import FooterSection from "@/components/FooterSection.vue"
import API from '@/services/api.js'

export default {
  name: "ContactPage",
  components: { Navbar, FooterSection },
  data() {
    return {
      form: { name: "", email: "", subject: "", message: "", recaptcha: false }
    }
  },
  methods: {
    async submitContact() {
      try {
        await API.post('/contacts/', {
          name: this.form.name,
          email: this.form.email,
          subject: this.form.subject,
          message: this.form.message,
        })
        alert(`Thank you, ${this.form.name}! Your message has been sent.`)
        this.form = { name: "", email: "", subject: "", message: "", recaptcha: false }
      } catch {
        alert('Failed to send message. Please try again.')
      }
    }
  }
}
</script>
