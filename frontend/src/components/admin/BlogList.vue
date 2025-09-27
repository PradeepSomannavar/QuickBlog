++<template>
  <div class="p-6">
    <div class="max-w-7xl mx-auto">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-3xl font-bold text-gray-800">All Blogs</h1>
      </div>
      <div class="bg-white rounded-xl shadow-xl overflow-hidden border border-gray-200">
        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gradient-to-r from-blue-600 to-blue-700 text-white">
              <tr>
                <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">S.No</th>
                <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Title</th>
                <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Date</th>
                <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Status</th>
                <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="(blog, index) in paginatedBlogs" :key="blog.id" class="hover:bg-gradient-to-r hover:from-gray-50 hover:to-blue-50 transition-colors duration-200">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 text-center">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900" v-if="editingBlogId !== blog.id">{{ blog.title }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900" v-else>
                  <input v-model="editTitle" class="border border-gray-300 rounded px-3 py-2 w-full focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-center" v-if="editingBlogId !== blog.id">{{ blog.created_at }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-center" v-else>
                  <!-- Date is not editable -->
                  {{ blog.created_at }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-center" v-if="editingBlogId !== blog.id">
                  <span :class="['px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full', blog.status === 'published' ? 'bg-green-100 text-green-800 border border-green-200' : 'bg-yellow-100 text-yellow-800 border border-yellow-200']">
                    {{ blog.status }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-center" v-else>
                  <select v-model="editStatus" class="border border-gray-300 rounded px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                    <option value="published">Published</option>
                    <option value="draft">Draft</option>
                  </select>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-center" v-if="editingBlogId !== blog.id">
                  <div class="flex justify-center space-x-3">
                    <button @click="startEdit(blog)" class="text-blue-600 hover:text-blue-800 p-2 rounded-full hover:bg-blue-100 transition-all duration-200" title="Edit">
                      <i class="fas fa-edit"></i>
                    </button>
                    <button @click="unpublish(blog.id)" class="text-yellow-600 hover:text-yellow-800 p-2 rounded-full hover:bg-yellow-100 transition-all duration-200" title="Unpublish">
                      <i class="fas fa-eye-slash"></i>
                    </button>
                    <button @click="deleteBlog(blog.id)" class="text-red-600 hover:text-red-800 p-2 rounded-full hover:bg-red-100 transition-all duration-200" title="Delete">
                      <i class="fas fa-trash"></i>
                    </button>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-center" v-else>
                  <div class="flex justify-center space-x-3">
                    <button @click="saveEdit" class="text-green-600 hover:text-green-800 p-2 rounded-full hover:bg-green-100 transition-all duration-200" title="Save">
                      <i class="fas fa-check"></i>
                    </button>
                    <button @click="cancelEdit" class="text-gray-600 hover:text-gray-800 p-2 rounded-full hover:bg-gray-100 transition-all duration-200" title="Cancel">
                      <i class="fas fa-times"></i>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="px-6 py-4 bg-gray-50 border-t border-gray-200">
          <div class="flex items-center justify-between">
            <div class="text-sm text-gray-700">
              Showing {{ (currentPage - 1) * itemsPerPage + 1 }} to {{ Math.min(currentPage * itemsPerPage, totalBlogs) }} of {{ totalBlogs }} results
            </div>
        <div class="flex space-x-2">
          <button @click="prevPage" :disabled="currentPage === 1" class="px-3 py-1 text-sm bg-blue-600 text-white border border-blue-700 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed">
            Previous
          </button>
          <button @click="nextPage" :disabled="currentPage === totalPages" class="px-3 py-1 text-sm bg-blue-600 text-white border border-blue-700 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed">
            Next
          </button>
        </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import API from '../../services/api.js'

const blogs = ref([])
const currentPage = ref(1)
const itemsPerPage = ref(10)
const totalBlogs = computed(() => blogs.value.length)
const totalPages = computed(() => Math.ceil(totalBlogs.value / itemsPerPage.value))
const paginatedBlogs = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return blogs.value.slice(start, end)
})

async function fetchBlogs() {
  try {
    const token = localStorage.getItem('token')
    const headers = token ? { Authorization: `Bearer ${token}` } : {}
    // Change API endpoint to fetch all blogs including drafts
    const response = await API.get('/blogs/admin', { headers })
    blogs.value = response.data
  } catch (error) {
    console.error('Failed to fetch blogs:', error)
  }
}

const editingBlogId = ref(null)
const editTitle = ref('')
const editSubtitle = ref('')
const editDescription = ref('')
const editCategory = ref('')
const editStatus = ref('')

function startEdit(blog) {
  editingBlogId.value = blog.id
  editTitle.value = blog.title
  editSubtitle.value = blog.subtitle
  editDescription.value = blog.description || ''
  editCategory.value = blog.category_id
  editStatus.value = blog.status
}

async function saveEdit() {
  try {
    const token = localStorage.getItem('token')
    const headers = token ? { Authorization: `Bearer ${token}` } : {}

    await API.put(`/blogs/${editingBlogId.value}`, {
      title: editTitle.value,
      subtitle: editSubtitle.value,
      description: editDescription.value,
      category_id: editCategory.value,
      status: editStatus.value
    }, { headers })

    editingBlogId.value = null
    await fetchBlogs()
  } catch (error) {
    console.error('Failed to update blog:', error)
    alert('Failed to update blog. Please try again.')
  }
}

function cancelEdit() {
  editingBlogId.value = null
}

async function unpublish(id) {
  try {
    const token = localStorage.getItem('token')
    const headers = token ? { Authorization: `Bearer ${token}` } : {}
    await API.put(`/blogs/${id}`, { status: 'draft' }, { headers })
    await fetchBlogs()
  } catch (error) {
    console.error('Failed to unpublish blog:', error)
  }
}

async function deleteBlog(id) {
  if (!confirm('Are you sure you want to delete this blog?')) return
  try {
    const token = localStorage.getItem('token')
    const headers = token ? { Authorization: `Bearer ${token}` } : {}
    await API.delete(`/blogs/${id}`, { headers })
    await fetchBlogs()
  } catch (error) {
    console.error('Failed to delete blog:', error)
  }
}

function prevPage() {
  if (currentPage.value > 1) {
    currentPage.value--
    fetchBlogs()
  }
}

function nextPage() {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
    fetchBlogs()
  }
}

onMounted(() => {
  fetchBlogs()
})
</script>


