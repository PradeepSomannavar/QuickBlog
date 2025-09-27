<template>
  <div class="flex min-h-screen bg-gray-100 h-screen">
    <Sidebar @update-section="currentSection = $event" />
    <div class="flex-1 overflow-auto">
      <DashboardSection v-if="currentSection==='dashboard'" />
      <AddBlog v-if="currentSection==='addBlog'" />
      <BlogList v-if="currentSection==='blogList'" />
      <CommentsSection v-if="currentSection==='comments'" />
      <SubscriberSection v-if="currentSection==='subscribers'" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Sidebar from '../components/admin/Sidebar.vue'
import DashboardSection from '../components/admin/DashboardSection.vue'
import AddBlog from '../components/admin/AddBlog.vue'
import BlogList from '../components/admin/BlogList.vue'
import CommentsSection from '../components/admin/CommentsSection.vue'
import SubscriberSection from '../components/admin/SubscriberSection.vue'

const currentSection = ref('dashboard')
</script>


