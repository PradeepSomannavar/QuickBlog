<template>
  <section class="hero">
    <!-- Main Welcome Text -->
    <div class="hero-content">
      <h1 class="hero-title">Welcome to QuickBlog</h1>
      <p class="hero-subtitle">Explore stories that inspire, inform, and innovate.</p>

      <!-- Search Bar -->
      <div class="search-bar">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search blogs..."
          class="search-input"
          @keyup.enter="onSearch"
        />
        <button class="search-btn" @click="onSearch">
          <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
          Search
        </button>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "HeroSection",
  data() {
    return {
      searchQuery: ""
    }
  },
  methods: {
    onSearch() {
      if (this.searchQuery.trim()) {
        this.$emit("search", this.searchQuery) // Emit search to parent (Homepage)
      }
    }
  }
}
</script>

<style scoped>
.hero {
  position: relative;
  text-align: center;
  padding: 80px 20px;
  background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
  color: white;
  border-radius: 0 0 30px 30px;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('@/assets/gradientBackground.png') no-repeat center center;
  background-size: cover;
  opacity: 0.1;
  z-index: -1;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
  animation: fadeInUp 1s ease-out;
}

.hero-title {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 20px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  animation: fadeInUp 1s ease-out 0.2s both;
}

.hero-subtitle {
  font-size: 20px;
  margin-bottom: 40px;
  opacity: 0.9;
  animation: fadeInUp 1s ease-out 0.4s both;
}

.search-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0;
  max-width: 500px;
  margin: 0 auto;
  animation: fadeInUp 1s ease-out 0.6s both;
}

.search-input {
  flex: 1;
  padding: 16px 20px;
  border: none;
  border-radius: 25px 0 0 25px;
  font-size: 16px;
  background: rgba(255, 255, 255, 0.95);
  color: var(--text-light);
  outline: none;
  transition: box-shadow 0.3s ease;
}

.search-input:focus {
  box-shadow: 0 0 0 3px rgba(255, 102, 0, 0.3);
}

.search-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 16px 24px;
  background: var(--accent-orange);
  border: none;
  border-radius: 0 25px 25px 0;
  color: white;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.search-btn:hover {
  background: #ff8533;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 102, 0, 0.4);
}

.search-icon {
  width: 18px;
  height: 18px;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 60px 20px;
  }
  .hero-title {
    font-size: 36px;
  }
  .hero-subtitle {
    font-size: 18px;
  }
  .search-bar {
    flex-direction: column;
    gap: 10px;
  }
  .search-input {
    border-radius: 25px;
    width: 100%;
  }
  .search-btn {
    border-radius: 25px;
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 28px;
  }
  .hero-subtitle {
    font-size: 16px;
  }
}
</style>
