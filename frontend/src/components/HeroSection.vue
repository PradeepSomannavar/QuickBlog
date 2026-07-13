<template>
  <section class="relative min-h-[90vh] flex items-center overflow-hidden">
    <div class="absolute inset-0 bg-grid opacity-40"></div>
    <div class="absolute -top-40 -right-40 w-96 h-96 bg-brand-500/5 dark:bg-brand-500/5 rounded-full blur-3xl"></div>
    <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-indigo-500/5 rounded-full blur-3xl"></div>
    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 lg:py-32">
      <div class="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
        <div class="animate-in">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full text-xs font-medium bg-brand-50 text-brand-700 dark:bg-brand-900/30 dark:text-brand-300 border border-brand-200 dark:border-brand-800 mb-6">
            <span class="w-1.5 h-1.5 rounded-full bg-brand-500 animate-pulse"></span>
            Latest from our team
          </div>
          <h1 class="section-heading text-balance mb-4 leading-[1.1]">
            {{ title }}
          </h1>
          <p class="section-subheading mb-8 text-lg">
            {{ subtitle }}
          </p>
          <div class="flex flex-wrap gap-3">
            <button @click="$router.push('/blog-list')" class="btn-primary px-6 py-3">
              Explore Articles
              <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
              </svg>
            </button>
            <button @click="$router.push('/about')" class="btn-outline px-6 py-3">
              Learn More
            </button>
          </div>
          <div class="flex items-center gap-8 mt-10 pt-8 border-t border-slate-100 dark:border-slate-800">
            <div class="text-center">
              <div class="text-2xl font-bold text-slate-900 dark:text-white">12+</div>
              <div class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">Articles</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold text-slate-900 dark:text-white">6</div>
              <div class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">Categories</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold text-slate-900 dark:text-white">100%</div>
              <div class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">Free</div>
            </div>
          </div>
        </div>
        <div class="hidden lg:block animate-in animate-in-delay-2">
          <div class="relative">
            <div class="relative z-10 bg-white dark:bg-slate-900/80 border border-slate-100 dark:border-slate-800/60 rounded-2xl p-6 shadow-xl">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-2 h-2 rounded-full bg-red-400"></div>
                <div class="w-2 h-2 rounded-full bg-yellow-400"></div>
                <div class="w-2 h-2 rounded-full bg-green-400"></div>
                <span class="text-xs text-slate-400 ml-2 font-mono">preview.md</span>
              </div>
              <div class="space-y-3">
                <div class="h-3 bg-slate-100 dark:bg-slate-800 rounded w-3/4"></div>
                <div class="h-3 bg-slate-100 dark:bg-slate-800 rounded w-1/2"></div>
                <div class="h-3 bg-slate-100 dark:bg-slate-800 rounded w-5/6"></div>
                <div class="h-3 bg-slate-100 dark:bg-slate-800 rounded w-2/3"></div>
                <div class="flex gap-2 pt-2">
                  <span class="h-6 bg-brand-100 dark:bg-brand-900/40 text-brand-700 dark:text-brand-300 rounded-md px-2 text-xs flex items-center font-medium">#writing</span>
                  <span class="h-6 bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400 rounded-md px-2 text-xs flex items-center">#tech</span>
                  <span class="h-6 bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400 rounded-md px-2 text-xs flex items-center">#blog</span>
                </div>
              </div>
            </div>
            <div class="absolute -bottom-4 -right-4 w-full h-full border border-slate-200 dark:border-slate-700 rounded-2xl -z-10"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "HeroSection",
  props: {
    title: { type: String, default: "Where Ideas Take Shape and Stories Come to Life" },
    subtitle: { type: String, default: "Discover insightful articles, tutorials, and stories crafted by passionate writers. Join our growing community of curious minds." }
  }
}
</script>
