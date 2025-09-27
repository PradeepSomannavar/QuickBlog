<template>
  <footer class="bg-gray-900 text-gray-300 py-8 mt-12">
    <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Brand / About -->
      <div>
        <h2 class="text-xl font-bold text-white mb-3">QuickBlog</h2>
        <p class="text-gray-400">
          Share your thoughts, learn new things, and explore amazing blogs on tech, AI, lifestyle, and more.
        </p>
      </div>

      <!-- Links -->
      <div>
        <h2 class="text-lg font-semibold text-white mb-3">Quick Links</h2>
        <ul class="space-y-2">
          <li><a href="/" class="hover:text-white transition">Home</a></li>
          <li><router-link to="/about" class="hover:text-white transition">About</router-link></li>
          <li><router-link to="/contact" class="hover:text-white transition">Contact</router-link></li>
        </ul>
      </div>

      <!-- Social -->
      <div>
        <h2 class="text-lg font-semibold text-white mb-3">Follow Us</h2>
        <div class="flex flex-col space-y-4">
          <a href="#" class="hover:text-white transition">
            <i class="fab fa-facebook-f"></i>
          </a>
          <a href="#" class="hover:text-white transition">
            <i class="fab fa-twitter"></i>
          </a>
          <a href="#" class="hover:text-white transition">
            <i class="fab fa-instagram"></i>
          </a>
          <a href="#" class="hover:text-white transition">
            <i class="fab fa-linkedin-in"></i>
          </a>
        </div>
      </div>

    </div>

    <!-- Bottom -->
    <div class="mt-8 border-t border-gray-800 pt-4 text-center text-gray-500 text-sm">
      &copy; 2025 QuickBlog. All rights reserved.
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterSection",
};
</script>


<style scoped>
/* Optional: add hover effects for icons */
.fab {
  font-size: 1.2rem;
}
</style>
