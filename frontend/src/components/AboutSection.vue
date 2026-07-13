<template>
  <div class="grid md:grid-cols-2 gap-12 items-center max-w-4xl mx-auto">
    <div class="space-y-5 animate-in">
      <p class="text-slate-500 dark:text-slate-400 leading-relaxed">
        Welcome to QuickBlog, your go-to platform for insightful articles and stories. We are passionate about sharing knowledge and connecting with our readers.
      </p>
      <p class="text-slate-500 dark:text-slate-400 leading-relaxed">
        Our mission is to create a vibrant community where ideas flourish, perspectives broaden, and meaningful conversations happen.
      </p>
      <div class="flex flex-wrap gap-6 pt-2">
        <div class="flex items-center gap-2" v-for="item in ['Quality Content', 'Community Driven', 'Expert Writers']" :key="item">
          <svg class="w-5 h-5 text-brand-600 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
          </svg>
          <span class="text-sm text-slate-700 dark:text-slate-300">{{ item }}</span>
        </div>
      </div>
    </div>
    <div class="flex justify-center animate-in animate-in-delay-1">
      <div class="w-64 h-64 bg-brand-50 dark:bg-brand-900/20 rounded-2xl flex items-center justify-center border border-brand-100 dark:border-brand-900/30">
        <svg class="w-32 h-32 text-brand-600 dark:text-brand-400" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12 2C6.48 2 2 6.48 2 12s6.48 10 10 10 10-6.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutSection"
}
</script>
