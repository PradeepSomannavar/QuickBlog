<template>
  <div>
    <div v-if="loading" class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
      <div v-for="i in 6" :key="i" class="rounded-2xl bg-white dark:bg-slate-900/80 border border-slate-100 dark:border-slate-800/60 overflow-hidden animate-pulse">
        <div class="h-48 bg-slate-100 dark:bg-slate-800"></div>
        <div class="p-5 space-y-3">
          <div class="h-4 bg-slate-100 dark:bg-slate-800 rounded w-1/4"></div>
          <div class="h-5 bg-slate-100 dark:bg-slate-800 rounded w-3/4"></div>
          <div class="h-4 bg-slate-100 dark:bg-slate-800 rounded w-full"></div>
          <div class="h-4 bg-slate-100 dark:bg-slate-800 rounded w-2/3"></div>
        </div>
      </div>
    </div>
    <div v-else-if="blogs.length === 0" class="text-center py-20">
      <div class="w-16 h-16 mx-auto mb-4 rounded-2xl bg-slate-50 dark:bg-slate-800/50 flex items-center justify-center">
        <svg class="w-8 h-8 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        </svg>
      </div>
      <p class="text-slate-500 dark:text-slate-400 text-lg font-medium">No articles found</p>
      <p class="text-slate-400 dark:text-slate-500 text-sm mt-1">Check back soon for new content.</p>
    </div>
    <div v-else class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
      <article v-for="(blog, index) in blogs" :key="blog.id" class="group card-premium overflow-hidden cursor-pointer" @click="$router.push(`/blog/${blog.slug || blog.id}`)" :style="{ animationDelay: `${index * 0.05}s` }">
        <div class="relative h-48 overflow-hidden">
          <img
            :src="blog.thumbnail ? `http://127.0.0.1:5000/static/uploads/${blog.thumbnail}` : `https://ui-avatars.com/api/?name=${encodeURIComponent(blog.title)}&background=6366f1&color=fff&size=400&font-size=0.33`"
            :alt="blog.title"
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent"></div>
          <div class="absolute top-3 left-3">
            <span class="badge bg-white/90 dark:bg-slate-900/90 text-slate-700 dark:text-slate-300 backdrop-blur-sm shadow-sm">
              {{ blog.category || blog.category_name || 'Uncategorized' }}
            </span>
          </div>
          <div class="absolute bottom-3 left-3" v-if="blog.reading_time">
            <span class="text-xs text-white/80 flex items-center gap-1">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              {{ blog.reading_time }} min read
            </span>
          </div>
        </div>
        <div class="p-5">
          <h3 class="font-semibold text-lg text-slate-900 dark:text-white mb-2 line-clamp-2 group-hover:text-brand-600 dark:group-hover:text-brand-400 transition-colors">
            {{ blog.title }}
          </h3>
          <p class="text-sm text-slate-500 dark:text-slate-400 line-clamp-2 leading-relaxed mb-4">
            {{ blog.excerpt || blog.content?.substring(0, 120) + '...' }}
          </p>
          <div class="flex items-center justify-between pt-3 border-t border-slate-100 dark:border-slate-800">
            <div class="flex items-center gap-2.5">
              <div class="w-7 h-7 rounded-full bg-brand-100 dark:bg-brand-900/40 flex items-center justify-center text-xs font-bold text-brand-600 dark:text-brand-400">
                {{ (blog.author_name || blog.author || 'A')[0].toUpperCase() }}
              </div>
              <span class="text-xs text-slate-500 dark:text-slate-400">{{ blog.author_name || blog.author || 'Anonymous' }}</span>
            </div>
            <span class="text-xs text-slate-400 dark:text-slate-500">
              {{ formatDate(blog.created_at || blog.published_at) }}
            </span>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: "BlogGrid",
  props: {
    blogs: { type: Array, default: () => [] },
    loading: { type: Boolean, default: false }
  },
  methods: {
    formatDate(dateStr) {
      if (!dateStr) return '';
      const d = new Date(dateStr);
      return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    }
  }
}
</script>
