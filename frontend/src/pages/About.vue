<template>
  <div>
    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-[#0f2027] via-[#203a43] to-[#2c5364] text-white py-24">
      <div class="container mx-auto px-6 text-center">
        <h1 class="text-6xl font-extrabold mb-6 tracking-tight">About QuickBlog</h1>
        <p class="text-xl max-w-3xl mx-auto leading-relaxed opacity-90">
          A fast, simple, and modern way to connect writers and readers.
          Quick reads that leave lasting thoughts.
        </p>
      </div>
    </section>

    <!-- What Makes QuickBlog Different -->
    <section class="py-20 bg-gray-100">
      <div class="container mx-auto px-6">
        <h2 class="text-4xl font-bold text-center mb-14 text-gray-800">
          What Makes Us Different
        </h2>
        <div class="grid md:grid-cols-3 gap-10">
          <!-- Card -->
          <div class="bg-white/90 backdrop-blur-md p-8 rounded-2xl shadow-xl hover:scale-105 hover:shadow-2xl transition-all text-center border-t-4 border-[#2c5364]">
            <h3 class="text-2xl font-semibold mb-4 text-[#2c5364]">⚡ Fresh Everyday</h3>
            <p class="text-gray-600">Always new blogs waiting for you. No stagnation, no pause.</p>
          </div>
          <div class="bg-white/90 backdrop-blur-md p-8 rounded-2xl shadow-xl hover:scale-105 hover:shadow-2xl transition-all text-center border-t-4 border-[#0f2027]">
            <h3 class="text-2xl font-semibold mb-4 text-[#0f2027]">🌐 Diverse Worlds</h3>
            <p class="text-gray-600">Tech, finance, ideas — a mix that connects curious minds.</p>
          </div>
          <div class="bg-white/90 backdrop-blur-md p-8 rounded-2xl shadow-xl hover:scale-105 hover:shadow-2xl transition-all text-center border-t-4 border-[#203a43]">
            <h3 class="text-2xl font-semibold mb-4 text-[#203a43]">🎯 Simple & Clear</h3>
            <p class="text-gray-600">Quick reads. Straight value. No noise, no filler.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Why QuickBlog Exists -->
    <section class="py-20 bg-white">
      <div class="container mx-auto px-6 text-center max-w-3xl">
        <h2 class="text-3xl font-bold mb-6 text-[#2c5364]">Why QuickBlog Exists</h2>
        <p class="text-lg text-gray-600">
          Because not everyone has time for endless scrolling. QuickBlog is made for readers who want
          <span class="font-semibold text-[#2c5364]"> sharp insights in minutes.</span>
        </p>
      </div>
    </section>

    <!-- Meet the Creator -->
    <section class="py-24 bg-gradient-to-br from-[#0f2027] via-[#203a43] to-[#2c5364]">
      <div class="container mx-auto px-6 text-center">
        <h2 class="text-4xl font-bold mb-14 text-white">Meet the Creator</h2>

        <div class="relative max-w-lg mx-auto">
          <!-- Glow effect -->
          <div class="absolute inset-0 bg-gradient-to-r from-cyan-400 to-blue-500 blur-3xl opacity-40 rounded-3xl"></div>

          <!-- Glass Card -->
          <div class="relative bg-white/10 backdrop-blur-xl rounded-3xl p-10 shadow-2xl border border-white/20">
            <h3 class="text-2xl font-semibold text-white mb-2">Pradeep Somannavar</h3>
          </div>
        </div>
      </div>
    </section>

    <!-- Closing -->
    <section class="py-20 bg-[#0f2027] text-white text-center">
      <h2 class="text-3xl md:text-4xl font-bold tracking-tight">
        QuickBlog — Quick to read. Lasting to think.
      </h2>
    </section>
  </div>
</template>

<script>
export default {
  name: "AboutPage",
};
</script>
