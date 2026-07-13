<template>
  <header class="fixed top-0 left-0 right-0 z-50">
    <div class="absolute inset-0 bg-white/70 dark:bg-[#020617]/70 backdrop-blur-xl border-b border-slate-200/60 dark:border-slate-800/60"></div>
    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 lg:h-20">
        <div class="flex items-center gap-10">
          <button @click="$router.push('/')" class="flex items-center gap-2.5 group">
            <div class="w-9 h-9 bg-brand-600 rounded-xl flex items-center justify-center shadow-sm shadow-brand-600/20 group-hover:shadow-md group-hover:shadow-brand-600/30 transition-all duration-300">
              <span class="text-white font-bold text-base">Q</span>
            </div>
            <span class="text-lg font-bold text-slate-900 dark:text-white tracking-tight">QuickBlog</span>
          </button>
          <nav class="hidden md:flex items-center gap-1">
            <router-link to="/" :class="navLinkClass('/')" class="nav-link">Home</router-link>
            <router-link to="/about" :class="navLinkClass('/about')" class="nav-link">About</router-link>
            <router-link to="/contact" :class="navLinkClass('/contact')" class="nav-link">Contact</router-link>
            <router-link to="/blog-list" :class="navLinkClass('/blog-list')" class="nav-link">Blog</router-link>
          </nav>
        </div>
        <div class="flex items-center gap-2 sm:gap-3">
          <button @click="searchOpen = !searchOpen" class="btn-ghost p-2 rounded-xl relative" aria-label="Search">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
            </svg>
          </button>
          <button @click="toggleTheme" class="btn-ghost p-2 rounded-xl" :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'">
            <svg v-if="!isDark" class="w-5 h-5 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/>
            </svg>
            <svg v-else class="w-5 h-5 transition-transform duration-300 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>
            </svg>
          </button>
          <button class="hidden sm:inline-flex btn-primary" @click="$router.push('/login')">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/>
            </svg>
            Sign In
          </button>
          <button @click="mobileOpen = !mobileOpen" class="md:hidden btn-ghost p-2 rounded-xl" aria-label="Menu">
            <svg v-if="!mobileOpen" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <transition enter-active-class="transition-all duration-300 ease-out" leave-active-class="transition-all duration-200 ease-in">
      <div v-if="searchOpen" class="border-t border-slate-100 dark:border-slate-800 bg-white/90 dark:bg-[#020617]/90 backdrop-blur-xl">
        <div class="max-w-2xl mx-auto px-4 py-4">
          <div class="relative">
            <svg class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
            </svg>
            <input v-model="searchQuery" @keyup.enter="doSearch" type="text" placeholder="Search articles..." class="w-full pl-12 pr-4 py-3 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-brand-500/40 transition-all" ref="searchInput" />
          </div>
        </div>
      </div>
    </transition>

    <transition enter-active-class="transition-all duration-300 ease-out" leave-active-class="transition-all duration-200 ease-in">
      <div v-if="mobileOpen" class="md:hidden border-t border-slate-100 dark:border-slate-800 bg-white/95 dark:bg-[#020617]/95 backdrop-blur-xl">
        <div class="px-4 py-4 space-y-1">
          <router-link to="/" @click="mobileOpen = false" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium" :class="$route.path === '/' ? 'bg-brand-50 text-brand-700 dark:bg-brand-900/30 dark:text-brand-300' : 'text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800/50'">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
            Home
          </router-link>
          <router-link to="/about" @click="mobileOpen = false" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium" :class="$route.path === '/about' ? 'bg-brand-50 text-brand-700 dark:bg-brand-900/30 dark:text-brand-300' : 'text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800/50'">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
            About
          </router-link>
          <router-link to="/contact" @click="mobileOpen = false" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium" :class="$route.path === '/contact' ? 'bg-brand-50 text-brand-700 dark:bg-brand-900/30 dark:text-brand-300' : 'text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800/50'">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
            Contact
          </router-link>
          <router-link to="/blog-list" @click="mobileOpen = false" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium" :class="$route.path === '/blog-list' ? 'bg-brand-50 text-brand-700 dark:bg-brand-900/30 dark:text-brand-300' : 'text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800/50'">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/></svg>
            Blog
          </router-link>
          <hr class="border-slate-100 dark:border-slate-800 my-2" />
          <button @click="$router.push('/login')" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800/50">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/></svg>
            Sign In
          </button>
        </div>
      </div>
    </transition>
  </header>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      isDark: false,
      mobileOpen: false,
      searchOpen: false,
      searchQuery: ""
    }
  },
  mounted() {
    this.isDark = localStorage.getItem('theme') === 'dark';
    this.applyTheme();
  },
  watch: {
    searchOpen(val) {
      if (val) this.$nextTick(() => this.$refs.searchInput?.focus());
    }
  },
  methods: {
    navLinkClass(path) {
      const active = this.$route.path === path;
      return `px-3 py-2 text-sm font-medium rounded-xl transition-all duration-200 ${
        active
          ? 'bg-brand-50 text-brand-700 dark:bg-brand-900/30 dark:text-brand-300'
          : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-50 dark:hover:bg-slate-800/50'
      }`;
    },
    doSearch() {
      if (this.searchQuery.trim()) {
        this.$router.push(`/blog-list?q=${encodeURIComponent(this.searchQuery)}`);
        this.searchOpen = false;
        this.searchQuery = "";
      }
    },
    toggleTheme() {
      this.isDark = !this.isDark;
      this.applyTheme();
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light');
    },
    applyTheme() {
      document.documentElement.classList.toggle('dark', this.isDark);
    }
  }
}
</script>
