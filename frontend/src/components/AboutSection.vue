<template>
  <section id="about" class="py-20 bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-800 dark:to-gray-900">
    <div class="container mx-auto px-4 max-w-4xl">
      <div class="text-center mb-12">
        <h2 class="text-4xl font-bold mb-4 text-gray-800 dark:text-white">About Us</h2>
        <div class="w-24 h-1 bg-gradient-to-r from-blue-500 to-orange-500 mx-auto mb-6"></div>
      </div>
      <div class="grid md:grid-cols-2 gap-12 items-center">
        <div class="space-y-6">
          <p class="text-lg text-gray-600 dark:text-gray-300 leading-relaxed">
            Welcome to QuickBlog, your go-to platform for insightful articles and stories. We are passionate about sharing knowledge and connecting with our readers.
          </p>
          <p class="text-lg text-gray-600 dark:text-gray-300 leading-relaxed">
            Our mission is to create a vibrant community where ideas flourish, perspectives broaden, and meaningful conversations happen.
          </p>
          <div class="flex flex-wrap gap-4 mt-8">
            <div class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
              </svg>
              <span class="text-gray-700 dark:text-gray-300">Quality Content</span>
            </div>
            <div class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-orange-500" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
              </svg>
              <span class="text-gray-700 dark:text-gray-300">Community Driven</span>
            </div>
          </div>
        </div>
        <div class="text-center">
          <div class="w-64 h-64 mx-auto bg-gradient-to-br from-blue-400 to-orange-400 rounded-full flex items-center justify-center shadow-2xl">
            <svg class="w-32 h-32 text-white" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "AboutSection"
}
</script>
