<template>
  <div>
    <Navbar />
    <div class="pt-24 lg:pt-28">
      <section class="relative py-20 lg:py-28 bg-slate-50/50 dark:bg-[#0f172a]/30 border-b border-slate-100 dark:border-slate-800/60">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center animate-in">
          <span class="badge-brand mb-4 inline-block">About Us</span>
          <h1 class="section-heading mb-4">About <span class="text-brand-600">QuickBlog</span></h1>
          <p class="section-subheading mx-auto text-lg">
            A fast, simple, and modern way to connect writers and readers. Quick reads that leave lasting thoughts.
          </p>
        </div>
      </section>

      <section class="py-20 lg:py-28">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-16 animate-in">
            <h2 class="section-heading mb-4">What Makes Us Different</h2>
            <p class="section-subheading mx-auto">Three pillars that define everything we do.</p>
          </div>
          <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
            <div class="card-premium p-8 text-center animate-in animate-in-delay-1">
              <div class="w-12 h-12 bg-brand-50 dark:bg-brand-900/30 rounded-xl flex items-center justify-center mx-auto mb-5">
                <svg class="w-6 h-6 text-brand-600 dark:text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-slate-900 dark:text-white mb-3">Fresh Everyday</h3>
              <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">Always new blogs waiting for you. No stagnation, no pause.</p>
            </div>
            <div class="card-premium p-8 text-center animate-in animate-in-delay-2">
              <div class="w-12 h-12 bg-brand-50 dark:bg-brand-900/30 rounded-xl flex items-center justify-center mx-auto mb-5">
                <svg class="w-6 h-6 text-brand-600 dark:text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-slate-900 dark:text-white mb-3">Diverse Worlds</h3>
              <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">Tech, finance, ideas — a mix that connects curious minds.</p>
            </div>
            <div class="card-premium p-8 text-center animate-in animate-in-delay-3">
              <div class="w-12 h-12 bg-brand-50 dark:bg-brand-900/30 rounded-xl flex items-center justify-center mx-auto mb-5">
                <svg class="w-6 h-6 text-brand-600 dark:text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-slate-900 dark:text-white mb-3">Simple & Clear</h3>
              <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">Quick reads. Straight value. No noise, no filler.</p>
            </div>
          </div>
        </div>
      </section>

      <section class="py-20 lg:py-28 bg-slate-50/50 dark:bg-[#0f172a]/30 border-y border-slate-100 dark:border-slate-800/60">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center max-w-3xl animate-in">
          <span class="badge-brand mb-4 inline-block">Our Mission</span>
          <h2 class="section-heading mb-6">Why QuickBlog Exists</h2>
          <p class="text-lg text-slate-500 dark:text-slate-400 leading-relaxed">
            Because not everyone has time for endless scrolling. QuickBlog is made for readers who want
            <span class="font-semibold text-brand-600 dark:text-brand-400"> sharp insights in minutes.</span>
          </p>
        </div>
      </section>

      <section class="py-20 lg:py-28">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center animate-in">
          <span class="badge-brand mb-4 inline-block">Creator</span>
          <h2 class="section-heading mb-12">Meet the Creator</h2>
          <div class="card-premium max-w-sm mx-auto p-8">
            <div class="w-20 h-20 bg-brand-100 dark:bg-brand-900/30 rounded-full flex items-center justify-center mx-auto mb-5">
              <span class="text-3xl font-bold text-brand-600 dark:text-brand-400">P</span>
            </div>
            <h3 class="text-xl font-semibold text-slate-900 dark:text-white mb-1">Pradeep Somannavar</h3>
            <p class="text-sm text-slate-500 dark:text-slate-400">Creator & Developer</p>
          </div>
        </div>
      </section>

      <section class="py-16 bg-slate-900 dark:bg-slate-950 text-white text-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <p class="text-2xl md:text-3xl font-bold tracking-tight">QuickBlog — Quick to read. Lasting to think.</p>
        </div>
      </section>
    </div>
    <FooterSection />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import FooterSection from "@/components/FooterSection.vue"

export default {
  name: "AboutPage",
  components: { Navbar, FooterSection }
}
</script>
