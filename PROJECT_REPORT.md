# QuickBlog — Complete Project Report

## 1. Overview

QuickBlog is a **full-stack blog platform** with a Python Flask backend and a Vue.js 3 frontend. It supports blog creation with AI-generated content, user authentication, comments, newsletter subscribers, contact forms, page view tracking, and a full admin dashboard. The UI uses Tailwind CSS with dark mode support.

---

## 2. Tech Stack

### Backend
| Technology | Purpose |
|---|---|
| **Python 3** | Runtime |
| **Flask 3.1.1** | Web framework |
| **Flask-SQLAlchemy 3.1.1** | ORM / Database |
| **Flask-Migrate 4.1.0** | Database migrations |
| **Flask-JWT-Extended 4.7.1** | JWT authentication |
| **Flask-CORS 5.0.1** | Cross-origin resource sharing |
| **SQLAlchemy 2.0.40** | Core ORM |
| **PyMySQL 1.1.1** | MySQL database driver |
| **Werkzeug 3.1.3** | Password hashing, file uploads |
| **python-dotenv 1.1.0** | Environment variables |
| **requests 2.32.3** | HTTP client (for AI API) |
| **smtplib** (stdlib) | Email sending via SMTP |
| **Google Gemini API** | AI blog content generation |

### Frontend
| Technology | Purpose |
|---|---|
| **Vue.js 3.5.18** | UI framework |
| **Vue Router 4.5.1** | Client-side routing |
| **Axios 1.11.0** | HTTP client |
| **Vite 7.1.2** | Build tool / dev server |
| **Tailwind CSS 3.3.2** | Utility-first CSS |
| **PostCSS 8.4.24** | CSS processing |
| **Autoprefixer 10.4.14** | CSS vendor prefixes |
| **Font Awesome 7.0.1** | Icons |

### Database
- **MySQL** (primary, via PyMySQL)
- **SQLite** (fallback, configured as default in `config.py`)

---

## 3. Project Structure

```
QuickBlog/
├── README.md
├── backend/
│   ├── app.py                    # Flask app factory + entry point
│   ├── config.py                 # Configuration (DB, JWT, secret keys)
│   ├── models.py                 # All SQLAlchemy models
│   ├── requirements.txt          # Python dependencies
│   ├── .env                      # Environment variables
│   ├── setup.py                  # DB creation + seed script
│   ├── create_admin.py           # Creates default admin user
│   ├── create_categories.py      # Seeds default categories
│   ├── seed_blogs.py             # Seeds sample blogs with images
│   ├── check_comments.py         # Utility: list all comments
│   ├── test_db.py                # Utility: test DB connection
│   ├── test_subscribers.py       # Utility: list subscribers
│   ├── update_drafts.py          # Utility: publish all drafts
│   ├── routes/
│   │   ├── auth.py               # Login, profile, register
│   │   ├── blogs.py              # CRUD for blogs
│   │   ├── categories.py         # CRUD for categories
│   │   ├── comments.py           # CRUD for comments
│   │   ├── contacts.py           # Contact form submissions
│   │   ├── subscribers.py        # Newsletter subscribers
│   │   ├── dashboard.py          # Admin dashboard stats
│   │   ├── ai.py                 # AI content generation
│   │   ├── settings.py           # Site settings (key-value)
│   │   ├── views.py              # Page view tracking
│   │   └── search.py             # Blog search
│   ├── services/
│   │   └── email_service.py      # SMTP email sending
│   ├── static/uploads/           # Uploaded thumbnails
│   ├── instance/                 # SQLite DB file (if used)
│   ├── migrations/               # Flask-Migrate migrations
│   └── venv/                     # Python virtual environment
│
└── frontend/
    ├── index.html                # HTML entry point (Google Fonts: Inter)
    ├── package.json              # Node dependencies
    ├── package-lock.json
    ├── vite.config.js            # Vite config + API proxy
    ├── tailwind.config.js        # Tailwind config (dark mode, brand colors)
    ├── postcss.config.js         # PostCSS plugins
    ├── .env                      # VITE_API_BASE_URL=http://127.0.0.1:5000
    ├── public/                   # Static assets
    ├── node_modules/
    ├── dist/                     # Build output
    └── src/
        ├── main.js               # Vue app bootstrap
        ├── App.vue               # Root component (<router-view />)
        ├── style.css             # Global styles (Tailwind + custom)
        ├── router/
        │   └── index.js          # Route definitions
        ├── services/
        │   └── api.js            # Axios instance with JWT interceptor
        ├── assets/
        │   └── assets.js         # Asset imports + static seed data
        ├── pages/
        │   ├── Home.vue          # Landing page
        │   ├── Login.vue         # Admin login
        │   ├── BlogDetail.vue    # Single blog view
        │   ├── BlogList.vue      # All articles listing
        │   ├── AdminDashboard.vue# Admin panel
        │   ├── About.vue         # About page
        │   └── Contact.vue       # Contact page
        ├── components/
        │   ├── Navbar.vue        # Fixed header with nav, search, dark mode
        │   ├── HeroSection.vue   # Hero banner with stats
        │   ├── BlogGrid.vue      # Blog card grid + skeleton loading
        │   ├── CategoryTab.vue   # Category filter pills
        │   ├── FooterSection.vue # Footer with newsletter
        │   ├── ContactSection.vue# Inline contact form
        │   ├── AboutSection.vue  # Inline about card
        │   └── admin/
        │       ├── Sidebar.vue           # Admin sidebar navigation
        │       ├── DashboardSection.vue   # Stats cards + todo list
        │       ├── AddBlog.vue            # Blog creation form + AI
        │       ├── BlogList.vue           # Blog management table
        │       ├── CommentsSection.vue    # Comment management
        │       └── SubscriberSection.vue  # Subscriber management
```

---

## 4. Database Models

### User
| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| username | String(50) | Unique, not null |
| email | String(150) | Unique |
| password_hash | String(256) | Not null (Werkzeug) |
| role | String(20) | Default: "admin" |
| created_at | DateTime | Default: utcnow |
| blogs | Relationship | One-to-many → Blog |

### Category
| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| name | String(50) | Unique, not null |
| slug | String(50) | Unique |
| description | Text | |
| created_at | DateTime | Default: utcnow |
| blogs | Relationship | One-to-many → Blog |

### Tag
| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| name | String(50) | Unique, not null |
| slug | String(50) | Unique |

### Blog
| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| title | String(200) | Not null |
| subtitle | String(300) | |
| description | Text | Not null (full blog content) |
| thumbnail | String(200) | Filename of uploaded image |
| status | String(20) | "draft" or "published" |
| featured | Boolean | Default: False |
| views | Integer | Default: 0 (incremented on view) |
| category_id | Integer | FK → categories.id |
| user_id | Integer | FK → users.id |
| created_at | DateTime | |
| updated_at | DateTime | Auto-updated |
| comments | Relationship | One-to-many → Comment (cascade delete) |
| tags | Relationship | Many-to-many → Tag |

### blog_tags (association table)
| Column | Type | Notes |
|---|---|---|
| blog_id | Integer | FK → blogs.id, PK |
| tag_id | Integer | FK → tags.id, PK |

### Comment
| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| blog_id | Integer | FK → blogs.id, not null |
| name | String(100) | Commenter name, not null |
| email | String(150) | |
| comment | Text | Not null |
| approved | Boolean | Default: False |
| created_at | DateTime | |

### Subscriber
| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| email | String(150) | Unique, not null |
| active | Boolean | Default: True |
| created_at | DateTime | |

### PageView
| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| blog_id | Integer | FK → blogs.id, nullable |
| ip_address | String(45) | |
| user_agent | Text | |
| viewed_at | DateTime | |

### Contact
| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| name | String(100) | Not null |
| email | String(150) | Not null |
| phone | String(20) | |
| subject | String(200) | |
| message | Text | Not null |
| is_read | Boolean | Default: False |
| created_at | DateTime | |

### SiteSetting
| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| key | String(100) | Unique, not null |
| value | Text | |

---

## 5. Backend API Routes (All Endpoints)

### Authentication — `/api/auth`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/auth/login` | No | Login with username/password → returns JWT + user object |
| GET | `/api/auth/profile` | JWT | Get current user profile |
| POST | `/api/auth/register` | JWT (admin) | Create new admin user |

### Blogs — `/api/blogs`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/blogs/` | No | List published blogs (paginated, filterable by category/featured) |
| GET | `/api/blogs/all` | No | List all published blogs (no pagination) |
| GET | `/api/blogs/admin` | JWT | List ALL blogs (any status) for admin |
| GET | `/api/blogs/<id>` | No | Get single blog (increments view count) |
| POST | `/api/blogs/` | JWT | Create new blog (multipart: thumbnail file + JSON fields) → sends email to subscribers if published |
| PUT | `/api/blogs/<id>` | JWT | Update blog fields |
| DELETE | `/api/blogs/<id>` | JWT | Delete blog + its comments |

### Categories — `/api/categories`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/categories/` | No | List all categories |
| POST | `/api/categories/` | JWT | Create category (auto-generates slug) |
| PUT | `/api/categories/<id>` | JWT | Update category |
| DELETE | `/api/categories/<id>` | JWT | Delete category |

### Comments — `/api/comments`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/comments/` | No | Add comment (auto-approved=True) |
| GET | `/api/comments/` | JWT | Get all comments (admin, filterable by blog_id) |
| GET | `/api/comments/public` | No | Get approved comments only |
| PUT | `/api/comments/<id>/approve` | JWT | Approve comment |
| PUT | `/api/comments/<id>` | JWT | Update comment text |
| DELETE | `/api/comments/<id>` | JWT | Delete comment |

### Subscribers — `/api/subscribers`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/subscribers/` | No | Subscribe (reactivates if previously unsubscribed) |
| GET | `/api/subscribers/` | JWT | List all subscribers |
| DELETE | `/api/subscribers/<id>` | JWT | Delete subscriber |

### Dashboard — `/api/dashboard`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/dashboard/stats` | JWT | Returns counts: blogs, drafts, published, comments, pending comments, subscribers, messages, unread messages, page views, total visitors |

### AI — `/api/ai`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/ai/generate` | No | Generates blog content using Google Gemini 1.5 Flash based on title + subtitle |

### Contacts — `/api/contacts`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/contacts/` | No | Submit contact form |
| GET | `/api/contacts/` | JWT | List all contact submissions |
| PUT | `/api/contacts/<id>/read` | JWT | Mark as read |
| DELETE | `/api/contacts/<id>` | JWT | Delete contact |

### Settings — `/api/settings`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/settings/` | No | Get all site settings (with defaults) |
| PUT | `/api/settings/` | JWT | Update/create settings (key-value pairs) |

### Views — `/api/views`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/views/track` | No | Track a page view (logs IP + user agent) |
| GET | `/api/views/stats` | No | Get total views + unique visitors |

### Search — `/api/search`
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/search/?q=...&category=...` | No | Search blogs by title/subtitle/description (paginated, filterable by category) |

---

## 6. Frontend

### Routes (Vue Router)
| Path | Component | Description |
|---|---|---|
| `/` | Home.vue | Landing page with hero, categories, blog grid, about, contact, footer |
| `/blog/:id` | BlogDetail.vue | Single blog view with comments section |
| `/login` | Login.vue | Admin login form |
| `/admin` | AdminDashboard.vue | Admin panel (protected) |
| `/blog-list` | BlogList.vue | Public article listing with search |
| `/about` | About.vue | About page |
| `/contact` | Contact.vue | Contact form page |

### Pages

#### Home.vue
- **HeroSection**: Full-height hero banner with animated gradient background, stats counters (blogs, views, subscribers), and a code preview card
- **CategoryTab**: Horizontal pill buttons to filter blogs by category
- **BlogGrid**: Responsive grid of blog cards with skeleton loading placeholders
- **AboutSection**: Inline about card with creator info
- **ContactSection**: Inline contact form
- **FooterSection**: Footer with newsletter subscription input

#### Login.vue
- Username + password form
- Show/hide password toggle
- Sends POST to `/api/auth/login`
- Stores JWT token in localStorage
- Redirects to `/admin` on success

#### BlogDetail.vue
- Fetches single blog by ID
- Displays title, subtitle, thumbnail, author, date, views, category
- Blog content rendered as plain text (newlines → paragraphs)
- **Comments Section**: Shows approved comments, form to add new comment
- Related blogs sidebar

#### BlogList.vue
- Fetches all published blogs via `/api/blogs/all`
- Search bar to filter by title
- Grid of blog cards linking to detail pages

#### AdminDashboard.vue
- Sidebar navigation (Dashboard, Add Blog, Blog List, Comments, Subscribers, Settings, Logout)
- **DashboardSection**: Stats cards (total blogs, published, drafts, comments, pending, subscribers, messages, views), To-do list stored in localStorage
- **AddBlog**: Form with title, subtitle, category dropdown, publish/draft toggle, featured toggle, thumbnail file upload, AI generate button (calls `/api/ai/generate` to fill description)
- **BlogList**: Table of all blogs with edit/delete actions, pagination
- **CommentsSection**: Table of all comments with approve/delete actions
- **SubscriberSection**: Table of subscribers with delete action

#### About.vue
- Static about page with creator info, mission, values

#### Contact.vue
- Full-page contact form (name, email, phone, subject, message)
- Submits to `/api/contacts/`

### Components

#### Navbar.vue
- Fixed header with logo "QuickBlog"
- Navigation links: Home, Blog, About, Contact
- Dark mode toggle (adds/removes `dark` class on `<html>`)
- Search bar (triggers search overlay)
- Mobile hamburger menu
- Admin link (visible when JWT token exists)

#### HeroSection.vue
- Full-viewport-height hero
- Gradient background with animated shapes
- Headline + subtext
- Stats row: total blogs, views, subscribers (fetched from API)
- Code preview card with syntax-highlighted snippet

#### BlogGrid.vue
- Receives blogs as prop
- Responsive CSS grid (1-col mobile, 2-col tablet, 3-col desktop)
- Each card shows: thumbnail, category badge, title, subtitle, author, date, views
- Skeleton loading placeholders while loading
- Cards link to `/blog/:id`

#### CategoryTab.vue
- Fetches categories from `/api/categories/`
- Horizontal scrollable pill buttons
- "All" button + one per category
- Emits `select` event with category ID

#### FooterSection.vue
- Site links, social icons
- Newsletter subscription form (POST to `/api/subscribers/`)
- Copyright text

#### ContactSection.vue
- Compact contact form for use inline on Home page
- Name, email, message fields
- Submits to `/api/contacts/`

#### AboutSection.vue
- Brief about card for use inline on Home page

### Admin Components

#### Sidebar.vue
- Dark-themed sidebar
- Navigation items: Dashboard, Add Blog, Blog List, Comments, Subscribers, Settings
- Active state highlighting
- Logout button (clears JWT + redirects to login)

#### DashboardSection.vue
- Fetches stats from `/api/dashboard/stats`
- Displays stat cards with icons for each metric
- To-do list feature (CRUD, stored in localStorage)

#### AddBlog.vue
- Title, subtitle inputs
- Category dropdown (fetched from API)
- Status toggle: Draft / Published
- Featured checkbox
- Thumbnail file upload with preview
- "AI Generate" button: sends title + subtitle to `/api/ai/generate`, fills description with AI response
- Submit creates blog via POST to `/api/blogs/` (multipart form data)

#### BlogList.vue (admin)
- Table view of all blogs (fetched from `/api/blogs/admin`)
- Columns: Title, Category, Status, Featured, Views, Date, Actions
- Edit: opens inline edit mode
- Delete: calls DELETE endpoint
- Pagination controls

#### CommentsSection.vue
- Table view of all comments (fetched from `/api/comments/`)
- Columns: Blog ID, Name, Email, Comment, Approved, Date, Actions
- Approve: calls PUT `/api/comments/<id>/approve`
- Delete: calls DELETE `/api/comments/<id>`

#### SubscriberSection.vue
- Table view of all subscribers (fetched from `/api/subscribers/`)
- Columns: Email, Active, Date, Actions
- Delete: calls DELETE `/api/subscribers/<id>`

---

## 7. Features & Functionality Summary

### Public Features
1. **Blog browsing**: Paginated grid with category filtering
2. **Blog detail view**: Full article with view counter, comments
3. **Search**: Search blogs by title/subtitle/description
4. **Comments**: Anyone can leave comments (auto-approved)
5. **Newsletter subscription**: Email subscription with duplicate/reactivation handling
6. **Contact form**: Submit inquiries (name, email, phone, subject, message)
7. **About page**: Static creator info
8. **Dark mode toggle**: Persistent via class-based dark mode

### Admin Features
1. **JWT authentication**: Secure login with token-based auth
2. **Admin dashboard**: Real-time stats (blogs, comments, subscribers, views)
3. **Blog CRUD**: Create, read, update, delete blogs with thumbnail upload
4. **AI blog generation**: Generate blog content via Google Gemini API from title/subtitle
5. **Category management**: CRUD for blog categories
6. **Comment moderation**: View, approve, delete comments
7. **Subscriber management**: View, delete subscribers
8. **Contact management**: View, mark as read, delete contact submissions
9. **Site settings**: Key-value configuration (site name, social links, contact info)
10. **To-do list**: Admin task tracker (localStorage-based)

### Technical Features
1. **Page view tracking**: Logs IP, user agent, blog ID for analytics
2. **Email notifications**: Sends email to all active subscribers when a new blog is published (via SMTP)
3. **Image uploads**: Thumbnail upload to `static/uploads/` with secure filename
4. **CORS support**: Cross-origin requests enabled
5. **Database migrations**: Flask-Migrate for schema versioning
6. **Responsive design**: Mobile-first with Tailwind CSS breakpoints
7. **Skeleton loading**: Placeholder animations while data loads
8. **Password hashing**: Werkzeug generate_password_hash / check_password_hash

---

## 8. Configuration

### Backend `.env`
```
GOOGLE_AI_API_KEY=<key>
DATABASE_URL=mysql+pymysql://root:password@localhost/quickblog
SECRET_KEY=quickblog_secret_key_2025
JWT_SECRET_KEY=quickblog_jwt_secret_2025
SMTP_SERVER=<smtp server>
SMTP_PORT=587
SMTP_USERNAME=<email>
SMTP_PASSWORD=<password>
```

### Frontend `.env`
```
VITE_API_BASE_URL=http://127.0.0.1:5000
```

### Vite Config
- `@` alias → `src/`
- Proxy: `/subscribers` → `localhost:5000`

### Tailwind Config
- Dark mode: `class` strategy
- Custom `brand` color palette (indigo-based)
- Custom font family: Inter

---

## 9. Setup & Run Instructions

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python setup.py              # Creates DB, tables, admin user, categories
python seed_blogs.py         # (Optional) Seeds sample blogs with images
python app.py                # Starts Flask on http://127.0.0.1:5000
```

### Frontend
```bash
cd frontend
npm install
npm run dev                  # Starts Vite on http://localhost:5173
```

### Default Admin Credentials
- **Username:** `pradeep`
- **Password:** `pradeep123`

---

## 10. Environment Variables Reference

### Backend
| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | `supersecret` | Flask secret key |
| `DATABASE_URL` | `sqlite:///quickblog.db` | Database connection string |
| `JWT_SECRET_KEY` | `jwtsecret` | JWT signing key |
| `GOOGLE_AI_API_KEY` | — | Google Gemini API key for AI blog generation |
| `SMTP_SERVER` | — | SMTP server hostname |
| `SMTP_PORT` | `587` | SMTP port |
| `SMTP_USERNAME` | — | SMTP login email |
| `SMTP_PASSWORD` | — | SMTP login password |

### Frontend
| Variable | Default | Description |
|---|---|---|
| `VITE_API_BASE_URL` | `http://127.0.0.1:5000` | Backend API base URL |

---

## 11. Default Site Settings (seeded in DB)

| Key | Value |
|---|---|
| site_name | QuickBlog |
| site_description | A modern blog platform for insightful stories. |
| footer_text | QuickBlog. All rights reserved. |
| contact_email | contact@quickblog.com |
| contact_phone | +1 (555) 123-4567 |
| social_facebook | # |
| social_twitter | # |
| social_instagram | # |
| social_linkedin | # |
| blogs_per_page | 12 |

---

## 12. Default Categories (seeded)

| Name | Slug | Description |
|---|---|---|
| Tech | tech | Technology news, reviews, and tutorials |
| AI | ai | Artificial Intelligence, machine learning, and data science |
| Lifestyle | lifestyle | Health, wellness, travel, and personal development |
| Finance | finance | Personal finance, investing, and economic insights |
| Design | design | UI/UX, graphic design, and creative inspiration |
| Science | science | Scientific discoveries and research |

---

## 13. Utility Scripts

| Script | Purpose |
|---|---|
| `setup.py` | Creates MySQL DB, tables, admin user, categories, default settings |
| `create_admin.py` | Creates admin user only |
| `create_categories.py` | Seeds 6 default categories |
| `seed_blogs.py` | Seeds 12 sample blogs (2 per category) with generated placeholder images |
| `check_comments.py` | Prints all comments to console |
| `test_db.py` | Tests database connection |
| `test_subscribers.py` | Lists all subscribers |
| `update_drafts.py` | Publishes all draft blogs |
