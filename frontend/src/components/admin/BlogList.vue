<template>
  <div class="p-6 lg:p-8">
    <div class="max-w-7xl mx-auto">
      <div class="flex items-center justify-between mb-8">
        <h1 class="text-2xl font-bold text-slate-900 dark:text-white">All Blogs</h1>
      </div>
      <div class="card-premium overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-sm">
            <thead>
              <tr class="bg-slate-50 dark:bg-slate-800/50 border-b border-slate-100 dark:border-slate-800">
                <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">#</th>
                <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Title</th>
                <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Date</th>
                <th class="px-6 py-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Status</th>
                <th class="px-6 py-3 text-right text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Actions</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
              <tr v-for="(blog, index) in paginatedBlogs" :key="blog.id" class="hover:bg-slate-50 dark:hover:bg-slate-800/30 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-slate-500 dark:text-slate-400">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
                <td class="px-6 py-4">
                  <div v-if="editingBlogId !== blog.id" class="font-medium text-slate-900 dark:text-white">{{ blog.title }}</div>
                  <input v-else v-model="editTitle" class="input py-1.5 text-sm" />
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-slate-500 dark:text-slate-400">{{ blog.created_at }}</td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span v-if="editingBlogId !== blog.id" :class="['inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium', blog.status === 'published' ? 'bg-emerald-50 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-900/30' : 'bg-amber-50 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400 border border-amber-200 dark:border-amber-900/30']">
                    {{ blog.status }}
                  </span>
                  <select v-else v-model="editStatus" class="input py-1.5 text-sm">
                    <option value="published">Published</option>
                    <option value="draft">Draft</option>
                  </select>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right">
                  <div v-if="editingBlogId !== blog.id" class="flex items-center justify-end gap-1">
                    <button @click="startEdit(blog)" class="p-2 text-slate-400 hover:text-brand-600 dark:hover:text-brand-400 transition-colors rounded-lg hover:bg-brand-50 dark:hover:bg-brand-900/20" title="Edit">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
                      </svg>
                    </button>
                    <button @click="unpublish(blog.id)" class="p-2 text-slate-400 hover:text-amber-600 dark:hover:text-amber-400 transition-colors rounded-lg hover:bg-amber-50 dark:hover:bg-amber-900/20" title="Unpublish">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/>
                      </svg>
                    </button>
                    <button @click="deleteBlog(blog.id)" class="p-2 text-slate-400 hover:text-red-600 dark:hover:text-red-400 transition-colors rounded-lg hover:bg-red-50 dark:hover:bg-red-900/20" title="Delete">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                      </svg>
                    </button>
                  </div>
                  <div v-else class="flex items-center justify-end gap-1">
                    <button @click="saveEdit" class="p-2 text-emerald-600 hover:text-emerald-700 dark:hover:text-emerald-400 transition-colors rounded-lg hover:bg-emerald-50 dark:hover:bg-emerald-900/20" title="Save">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                      </svg>
                    </button>
                    <button @click="cancelEdit" class="p-2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-300 transition-colors rounded-lg hover:bg-slate-50 dark:hover:bg-slate-900/50" title="Cancel">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                      </svg>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="px-6 py-4 bg-slate-50 dark:bg-slate-800/50 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
          <div class="text-sm text-slate-500 dark:text-slate-400">
            Showing {{ (currentPage - 1) * itemsPerPage + 1 }} to {{ Math.min(currentPage * itemsPerPage, totalBlogs) }} of {{ totalBlogs }} results
          </div>
          <div class="flex gap-2">
            <button @click="prevPage" :disabled="currentPage === 1" class="btn-outline text-xs px-3 py-1.5 disabled:opacity-50">Previous</button>
            <button @click="nextPage" :disabled="currentPage === totalPages" class="btn-outline text-xs px-3 py-1.5 disabled:opacity-50">Next</button>
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
const itemsPerPage = 10
const totalBlogs = computed(() => blogs.value.length)
const totalPages = computed(() => Math.ceil(totalBlogs.value / itemsPerPage))
const paginatedBlogs = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return blogs.value.slice(start, start + itemsPerPage)
})

async function fetchBlogs() {
  try {
    const token = localStorage.getItem('token')
    const headers = token ? { Authorization: `Bearer ${token}` } : {}
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
  if (currentPage.value > 1) currentPage.value--
}

function nextPage() {
  if (currentPage.value < totalPages.value) currentPage.value++
}

onMounted(() => {
  fetchBlogs()
})
</script>
