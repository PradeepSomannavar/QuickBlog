<template>
  <div>
    <Navbar/>
    <HeroSection @search="handleSearch" />
    <CategoryTab @categorySelected="filterBlogs" />
    <BlogGrid :blogs="filteredBlogs" />
    <AboutSection />
    <ContactSection />
    <SubscriberSection />
    <FooterSection />   <!-- 👈 Added footer -->
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import HeroSection from "@/components/HeroSection.vue"
import CategoryTab from "@/components/CategoryTab.vue"
import BlogGrid from "@/components/BlogGrid.vue"
import AboutSection from "@/components/AboutSection.vue"
import ContactSection from "@/components/ContactSection.vue"
import SubscriberSection from "@/components/SubscriberSection.vue"
import FooterSection from "@/components/Footer.vue"

export default {
  name: "Home",
  components: { HeroSection, CategoryTab, BlogGrid, SubscriberSection, FooterSection ,Navbar},
  data() {
    return {
      blogs: [],
      selectedCategory: "All",
      searchQuery: ""
    }
  },
  computed: {
    filteredBlogs() {
      let blogs = this.blogs
      if (this.searchQuery) {
        const lowerQuery = this.searchQuery.toLowerCase()
        blogs = blogs.filter(blog =>
          blog.title.toLowerCase().includes(lowerQuery) ||
          blog.subtitle.toLowerCase().includes(lowerQuery)
        )
      }
      if (this.selectedCategory !== "All") {
        blogs = blogs.filter(blog => blog.category === this.selectedCategory)
      }
      return blogs
    }
  },
  methods: {
    filterBlogs(category) {
      this.selectedCategory = category
    },
    handleSearch(query) {
      this.searchQuery = query
      this.selectedCategory = "All" // Reset category filter on search
    }
  },
  mounted() {
    this.fetchBlogs()
  },
  methods: {
    async fetchBlogs() {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/blogs/')
        const data = await response.json()
        this.blogs = data.map(blog => ({
          id: blog.id,
          title: blog.title,
          subtitle: blog.subtitle,
          thumbnail: blog.thumbnail,
          category: blog.category_id ? this.getCategoryName(blog.category_id) : 'Uncategorized'
        }))
      } catch (error) {
        console.error('Failed to fetch blogs:', error)
      }
    },
    getCategoryName(categoryId) {
      const categories = {
        1: 'Tech',
        2: 'AI',
        3: 'Lifestyle',
        4: 'Finance'
      }
      return categories[categoryId] || 'Uncategorized'
    },
    filterBlogs(category) {
      this.selectedCategory = category
    },
    handleSearch(query) {
      this.searchQuery = query
      this.selectedCategory = "All" // Reset category filter on search
    }
  }
}
</script>
