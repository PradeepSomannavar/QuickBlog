import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import BlogDetail from '../pages/BlogDetail.vue'
import Login from '../pages/Login.vue'
import AdminDashboard from '../pages/AdminDashboard.vue'
import BlogList from '../pages/BlogList.vue'
import About from '../pages/About.vue'
import Contact from '../pages/Contact.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/blog/:id', component: BlogDetail, props: true },
  { path: '/login', component: Login },
  { path: '/admin', component: AdminDashboard },
  { path: '/blog-list', component: BlogList },
  { path: '/about', component: About },
  { path: '/contact', component: Contact }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
