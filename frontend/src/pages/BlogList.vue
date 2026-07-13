<template>
  <div>
    <Navbar />
    <div class="pt-24 lg:pt-28">
      <section class="relative py-16 lg:py-20 bg-slate-50/50 dark:bg-[#0f172a]/30 border-b border-slate-100 dark:border-slate-800/60">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center animate-in">
            <span class="badge-brand mb-4 inline-block">Our Blog</span>
            <h1 class="section-heading mb-4">All Articles</h1>
            <p class="section-subheading mx-auto">Browse our complete collection of articles, tutorials, and stories.</p>
            <div class="max-w-md mx-auto mt-8 relative">
              <svg class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
              </svg>
              <input v-model="searchQuery" @input="fetchBlogs" type="text" placeholder="Search articles..." class="w-full pl-12 pr-4 py-3 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-brand-500/40 transition-all" />
            </div>
          </div>
        </div>
      </section>
      <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-20">
        <BlogGrid :blogs="blogs" :loading="loading" />
        <div v-if="error" class="text-red-500 dark:text-red-400 text-center py-8 bg-red-50/50 dark:bg-red-900/10 rounded-2xl border border-red-100 dark:border-red-900/30">
          <p class="font-medium">{{ error }}</p>
        </div>
      </section>
    </div>
    <FooterSection />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import BlogGrid from '@/components/BlogGrid.vue'
import FooterSection from '@/components/FooterSection.vue'
import API from '@/services/api.js'

export default {
  name: "BlogList",
  components: { Navbar, BlogGrid, FooterSection },
  setup() {
    const route = useRoute()
    const blogs = ref([])
    const loading = ref(false)
    const error = ref('')
    const searchQuery = ref(route.query.q || '')

    async function fetchBlogs() {
      loading.value = true
      error.value = ''
      try {
        const params = {}
        if (searchQuery.value) params.q = searchQuery.value
        const res = await API.get('/blogs/all', { params })
        blogs.value = Array.isArray(res.data) ? res.data : (res.data.blogs || [])
      } catch (err) {
        error.value = 'Failed to load blogs.'
        console.error(err)
      } finally {
        loading.value = false
      }
    }

    onMounted(() => { fetchBlogs() })

    return { blogs, loading, error, searchQuery, fetchBlogs }
  }
}
</script>
