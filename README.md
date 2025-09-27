# 🚀 QuickBlog - AI Powered Blog Website

A **modern, fast, and simple blogging platform** that connects writers and readers. Built with **Vue.js** for the frontend and **Flask** for the backend, QuickBlog integrates **AI-powered content features** for automatic blog descriptions.

---

## 🎯 Project Purpose

The purpose of developing **QuickBlog** is to **learn full-stack web development** and explore modern tech stacks like **Vue.js + Flask + PostgreSQL**.
This project gave hands-on experience with:

- **Frontend** ✅
- **Backend** ✅
- **Databases** ✅
- **Authentication** ✅
- **AI integration** ✅

This is a **new step towards becoming a full-stack web developer**! 💻✨

---

## ✨ Features

- **🔑 User Authentication:** Secure login and registration system
- **📝 Blog Management:** Create, edit, and publish blog posts with **images, titles, and AI-generated descriptions**
- **💬 Comment System:** Engage with readers through comments
- **📊 Admin Dashboard:** Manage blogs, comments, and subscribers
- **📱 Responsive Design:** Optimized for desktop and mobile devices
- **🌙 Dark Mode:** Toggle between light and dark themes
- **🤖 AI Integration:** Automatically generate blog descriptions and enhance content creation

---

## 🛠 Tech Stack

### Frontend
- **Vue.js 3**
- **Vue Router**
- **Tailwind CSS**
- **Vite**

### Backend
- **Flask**
- **SQLAlchemy**
- **JWT Authentication**
- **Email Service** (for notifications)

### Database
- **SQLite** (development) / **PostgreSQL** (production)

---

## ⚡ Installation

### Prerequisites
- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **Git**

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quickblog.git
   cd quickblog
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python create_admin.py
   python create_categories.py
   ```

4. Run the backend:
   ```bash
   python app.py
   ```

### Frontend Setup

1. In a new terminal, set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

2. Run the frontend:
   ```bash
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:5173`

---

## 📌 Usage

1. Register a new account or login with existing credentials
2. Create and publish blog posts
3. Browse and read blogs from other writers
4. Comment on posts to engage with the community
5. Use the admin dashboard to manage content (admin only)
6. Use the AI-powered description feature to automatically generate blog content

---

## 🔗 API Documentation

The backend provides RESTful APIs for:

- User authentication
- Blog CRUD operations
- Comment management
- Subscriber management
- AI-powered description generation 🤖
