<template>
  <div>
    <Navbar />
    <div class="pt-24 lg:pt-28">
      <div v-if="error" class="max-w-3xl mx-auto px-4 py-20 text-center">
        <div class="w-16 h-16 mx-auto mb-4 rounded-2xl bg-red-50 dark:bg-red-900/10 flex items-center justify-center border border-red-100 dark:border-red-900/30">
          <svg class="w-8 h-8 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4.5c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z"/>
          </svg>
        </div>
        <p class="text-lg font-medium text-red-500 dark:text-red-400">{{ error }}</p>
      </div>

      <article v-if="blog.title" class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
        <div class="animate-in">
          <div class="flex items-center gap-2 text-xs text-slate-400 dark:text-slate-500 mb-4">
            <button @click="$router.push('/blog-list')" class="hover:text-brand-600 dark:hover:text-brand-400 transition-colors flex items-center gap-1">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
              Back to articles
            </button>
            <span class="text-slate-300 dark:text-slate-600">|</span>
            <span class="badge-slate">{{ blog.category || 'Uncategorized' }}</span>
          </div>

          <header class="mb-10">
            <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900 dark:text-white mb-4 leading-[1.1] text-balance">
              {{ blog.title }}
            </h1>
            <p class="text-lg text-slate-500 dark:text-slate-400 mb-6 leading-relaxed">{{ blog.subtitle }}</p>
            <div class="flex flex-wrap items-center gap-4 text-sm text-slate-400 dark:text-slate-500">
              <div class="flex items-center gap-2">
                <div class="w-8 h-8 rounded-full bg-brand-100 dark:bg-brand-900/40 flex items-center justify-center text-xs font-bold text-brand-600 dark:text-brand-400">
                  {{ (blog.author || 'A')[0].toUpperCase() }}
                </div>
                <span>{{ blog.author }}</span>
              </div>
              <span class="hidden sm:inline text-slate-300 dark:text-slate-600">|</span>
              <span class="flex items-center gap-1">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                {{ blog.date }}
              </span>
              <span v-if="blog.reading_time" class="flex items-center gap-1">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                {{ blog.reading_time }} min read
              </span>
            </div>
          </header>

          <div v-if="blog.image" class="mb-12 rounded-2xl overflow-hidden border border-slate-100 dark:border-slate-800 shadow-sm">
            <img :src="blog.image" alt="Blog Image" class="w-full h-auto object-cover" />
          </div>

          <div class="prose prose-slate dark:prose-invert max-w-none mb-16">
            <p v-for="(para, index) in blog.content" :key="index" class="mb-5 text-slate-600 dark:text-slate-300 leading-relaxed text-base md:text-lg">{{ para }}</p>
          </div>

          <section class="border-t border-slate-100 dark:border-slate-800 pt-10 animate-in animate-in-delay-2">
            <div class="flex items-center justify-between mb-8">
              <h2 class="text-2xl font-bold text-slate-900 dark:text-white">Comments <span class="text-sm font-normal text-slate-400 dark:text-slate-500">({{ comments.length }})</span></h2>
            </div>

            <div v-if="comments.length === 0" class="text-center py-12 bg-slate-50/50 dark:bg-slate-900/30 rounded-2xl border border-slate-100 dark:border-slate-800/60 mb-8">
              <div class="w-12 h-12 mx-auto mb-3 rounded-xl bg-slate-100 dark:bg-slate-800 flex items-center justify-center">
                <svg class="w-6 h-6 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
              </div>
              <p class="text-slate-500 dark:text-slate-400 font-medium">No comments yet</p>
              <p class="text-slate-400 dark:text-slate-500 text-sm mt-1">Be the first to share your thoughts!</p>
            </div>

            <div v-for="(comment, index) in comments" :key="index" class="flex items-start gap-4 pb-6 mb-6 border-b border-slate-100 dark:border-slate-800 last:border-b-0">
              <div class="w-10 h-10 rounded-full bg-brand-100 dark:bg-brand-900/30 flex items-center justify-center shrink-0">
                <span class="text-sm font-bold text-brand-600 dark:text-brand-400">{{ (comment.name || 'A')[0].toUpperCase() }}</span>
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="font-semibold text-sm text-slate-900 dark:text-white">{{ comment.name }}</span>
                  <span class="text-xs text-slate-400 dark:text-slate-500">{{ comment.date || formatDate(comment.created_at) }}</span>
                </div>
                <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">{{ comment.comment || comment.content }}</p>
              </div>
            </div>

            <div class="mt-10 p-6 bg-slate-50/50 dark:bg-slate-900/30 rounded-2xl border border-slate-100 dark:border-slate-800/60">
              <h3 class="text-lg font-semibold text-slate-900 dark:text-white mb-5">Leave a Comment</h3>
              <div class="space-y-4">
                <input v-model="newComment.name" type="text" placeholder="Your Name" class="input" />
                <textarea v-model="newComment.email" placeholder="Your Email (optional)" rows="1" class="input resize-none"></textarea>
                <textarea v-model="newComment.text" placeholder="Share your thoughts..." rows="4" class="input resize-none"></textarea>
                <button @click="addComment" class="btn-primary">
                  Post Comment
                  <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/></svg>
                </button>
              </div>
            </div>
          </section>
        </div>
      </article>
    </div>
    <FooterSection />
  </div>
</template>

<script>
import API from '@/services/api.js'
import Navbar from "@/components/Navbar.vue"
import FooterSection from "@/components/FooterSection.vue"

export default {
  name: "BlogDetail",
  components: { Navbar, FooterSection },
  props: ["id"],
  data() {
    return {
      blog: {},
      comments: [],
      newComment: { name: "", email: "", text: "" },
      error: "",
    }
  },
  async created() {
    this.error = ""
    try {
      const response = await API.get(`/blogs/${this.id}`)
      const data = response.data
      const thumb = data.thumbnail || data.image
      this.blog = {
        id: data.id,
        title: data.title,
        subtitle: data.subtitle || data.excerpt || '',
        image: thumb ? `http://127.0.0.1:5000/static/uploads/${thumb}` : '',
        category: data.category || data.category_name || 'Uncategorized',
        author: data.author_name || data.author || 'Anonymous',
        reading_time: data.reading_time,
        date: new Date(data.created_at || data.published_at).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        content: data.description ? data.description.split('\n').filter(p => p.trim()) : (data.content || []),
      }
    } catch (err) {
      this.error = "Failed to load blog details."
      console.error(err)
    }

    try {
      const res = await API.get('/comments/public')
      const data = res.data
      this.comments = (Array.isArray(data) ? data : (data.comments || []))
        .filter(c => c.blog_id == this.id && c.approved !== false)
        .map(c => ({ ...c, date: new Date(c.created_at).toLocaleDateString() }))
    } catch (err) {
      console.error(err)
    }
  },
  methods: {
    formatDate(d) {
      if (!d) return ''
      return new Date(d).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
    },
    async addComment() {
      if (!this.newComment.name || !this.newComment.text) return
      try {
        await API.post('/comments/', {
          blog_id: this.id,
          name: this.newComment.name,
          email: this.newComment.email || undefined,
          comment: this.newComment.text,
        })
        this.comments.push({
          blog_id: this.id,
          name: this.newComment.name,
          comment: this.newComment.text,
          approved: true,
          date: new Date().toLocaleDateString(),
        })
        this.newComment = { name: "", email: "", text: "" }
      } catch (err) {
        alert('Failed to submit comment.')
        console.error(err)
      }
    },
  }
}
</script>
