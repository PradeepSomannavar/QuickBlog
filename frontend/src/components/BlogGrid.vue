<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 p-6">
    <div
      v-for="blog in blogs"
      :key="blog.id"
      class="bg-white shadow-md rounded-lg overflow-hidden hover:shadow-xl transition-shadow duration-300"
    >
      <!-- Make the card clickable with router-link -->
      <router-link :to="`/blog/${blog.id}`">
        <img
          :src="blog.thumbnail ? `http://127.0.0.1:5000/static/uploads/${blog.thumbnail}` : 'http://127.0.0.1:5000/static/uploads/default-thumbnail.png'"
          :alt="blog.title"
          class="w-full h-40 object-cover"
        />
        <div class="p-4">
          <h2 class="text-xl font-semibold mb-2">{{ blog.title }}</h2>
          <p class="text-gray-600">{{ blog.subtitle }}</p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "BlogGrid",
  props: {
    blogs: {
      type: Array,
      required: true,
    },
  },
}
</script>

<style scoped>
/* optional hover effect */
</style>
