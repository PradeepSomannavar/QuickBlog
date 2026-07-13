<template>
  <div>
    <Navbar />
    <main class="min-h-screen">
      <HeroSection @search="handleSearch" />

      <section class="relative py-20 lg:py-28">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-14 animate-in">
            <span class="badge-brand mb-4 inline-block">Browse Articles</span>
            <h2 class="section-heading mb-4">Latest from our blog</h2>
            <p class="section-subheading mx-auto">Hand-picked articles covering technology, design, and everything in between.</p>
          </div>
          <div class="flex flex-wrap items-center justify-center gap-3 mb-12 animate-in animate-in-delay-1">
            <CategoryTab :categories="categoryList" :activeCategory="selectedCategory" @select="selectedCategory = $event" />
          </div>
          <BlogGrid :blogs="filteredBlogs" :loading="loading" />
        </div>
      </section>

      <section class="relative py-20 lg:py-28 bg-slate-50/50 dark:bg-[#0f172a]/30 border-y border-slate-100 dark:border-slate-800/60">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-14 animate-in">
            <span class="badge-brand mb-4 inline-block">About Us</span>
            <h2 class="section-heading mb-4">Our story</h2>
            <p class="section-subheading mx-auto">Learn more about what drives us and the team behind the content.</p>
          </div>
          <AboutSection />
        </div>
      </section>

      <section class="relative py-20 lg:py-28">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-14 animate-in">
            <span class="badge-brand mb-4 inline-block">Get in Touch</span>
            <h2 class="section-heading mb-4">Let's work together</h2>
            <p class="section-subheading mx-auto">Have a question, suggestion, or just want to say hi? We'd love to hear from you.</p>
          </div>
          <div class="max-w-2xl mx-auto animate-in animate-in-delay-1">
            <ContactSection />
          </div>
        </div>
      </section>
    </main>

    <FooterSection />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import HeroSection from "@/components/HeroSection.vue"
import CategoryTab from "@/components/CategoryTab.vue"
import BlogGrid from "@/components/BlogGrid.vue"
import AboutSection from "@/components/AboutSection.vue"
import ContactSection from "@/components/ContactSection.vue"
import FooterSection from "@/components/FooterSection.vue"

export default {
  name: "Home",
  components: {
    Navbar,
    HeroSection,
    CategoryTab,
    BlogGrid,
    AboutSection,
    ContactSection,
    FooterSection
  },
  data() {
    return {
      blogs: [],
      loading: true,
      selectedCategory: "",
      categoryList: [
        { id: 0, name: "All" },
        { id: 1, name: "Technology" },
        { id: 2, name: "Design" },
        { id: 3, name: "Business" },
        { id: 4, name: "Lifestyle" },
        { id: 5, name: "Travel" },
        { id: 6, name: "Food" }
      ]
    }
  },
  computed: {
    filteredBlogs() {
      if (!this.selectedCategory) return this.blogs
      return this.blogs.filter(b =>
        (b.category || b.category_name || '').toLowerCase() === this.selectedCategory.toLowerCase()
      )
    }
  },
  methods: {
    async fetchBlogs() {
      this.loading = true
      try {
        const res = await fetch('http://127.0.0.1:5000/api/blogs/all')
        const data = await res.json()
        this.blogs = Array.isArray(data) ? data : (data.blogs || [])
      } catch (err) {
        console.error('Failed to fetch blogs:', err)
      } finally {
        this.loading = false
      }
    },
    handleSearch(query) {
      this.$router.push(`/blog-list?q=${encodeURIComponent(query)}`)
    }
  },
  mounted() {
    this.fetchBlogs()
  }
}
</script>
