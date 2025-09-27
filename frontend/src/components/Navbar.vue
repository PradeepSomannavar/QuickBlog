<template>
  <nav class="navbar">
    <!-- Left: Logo -->
    <div class="logo" @click="$router.push('/')">
      <span class="logo-text">QuickBlog</span>
    </div>

    <!-- Right: Login and Theme Toggle -->
    <div class="nav-actions">
      <button class="theme-toggle-btn" @click="toggleTheme" :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'">
        {{ isDark ? '☀️' : '🌙' }}
      </button>
      <button class="login-btn" @click="$router.push('/login')">
        Login
      </button>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      isDark: false
    }
  },
  mounted() {
    this.isDark = localStorage.getItem('theme') === 'dark';
    this.applyTheme();
  },
  methods: {
    toggleTheme() {
      this.isDark = !this.isDark;
      this.applyTheme();
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light');
    },
    applyTheme() {
      if (this.isDark) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    }
  }
}
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 40px;
  background: var(--primary-blue);
  color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  transition: background-color 0.3s ease;
}

.dark .navbar {
  background: var(--dark-bg);
  color: var(--text-dark);
}

.logo {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.logo-img {
  width: 35px;
  height: 35px;
  margin-right: 10px;
  transition: transform 0.3s ease;
}
.logo:hover .logo-img {
  transform: scale(1.1);
}

.logo-text {
  font-size: 22px;
  font-weight: bold;
  letter-spacing: 1px;
  user-select: none;
}

.nav-actions {
  display: flex;
  align-items: center;
}

.nav-actions .login-btn {
  background: var(--accent-orange);
  border: none;
  padding: 8px 20px;
  border-radius: 6px;
  color: white;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}
.nav-actions .login-btn:hover {
  background: #ff8533;
  transform: translateY(-2px);
}

.nav-actions .theme-toggle-btn {
  background: none;
  border: none;
  padding: 8px;
  border-radius: 6px;
  color: white;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-right: 10px;
}
.nav-actions .theme-toggle-btn:hover {
  background: rgba(255, 255, 255, 0.15);
}

@media (max-width: 600px) {
  .navbar {
    padding: 10px 20px;
  }
  .logo-text {
    font-size: 18px;
  }
  .nav-actions .login-btn {
    padding: 6px 14px;
    font-size: 12px;
  }
  .nav-actions .theme-toggle-btn {
    font-size: 16px;
    padding: 6px;
  }
}
</style>
