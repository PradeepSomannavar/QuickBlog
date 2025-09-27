import axios from 'axios'

// Base API URL (Flask backend)
const API = axios.create({
  baseURL: 'http://127.0.0.1:5000/api'
})

// Add token if available
API.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default API
