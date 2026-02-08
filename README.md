# portfolio-resume2.0
# Personal Portfolio & Blog Website

A modern, fully responsive personal portfolio and blog website built with Django, featuring dark/light mode toggle and beautiful animations.

## Features

### Pages
- **Home**: Hero section with call-to-action buttons
- **About**: Personal information and skills showcase
- **Experience**: Timeline of work experience
- **Projects**: Grid layout of portfolio projects
- **Blog**: Daily blog updates with pagination
- **Contact**: Contact form and social media links

### Core Features
- ✅ Fully responsive design (desktop, tablet, mobile)
- ✅ Global background particle animation
- ✅ Dark/Light mode toggle (persists via localStorage)
- ✅ Clean, modern, professional UI with Tailwind CSS
- ✅ Django Admin panel for content management
- ✅ SEO-friendly slug URLs for blog posts
- ✅ Contact form with database storage
- ✅ Custom 404 page

## Tech Stack

**Backend:**
- Django 6.0.2
- Python 3.13
- SQLite (development)

**Frontend:**
- Tailwind CSS (via CDN)
- Particles.js for background animation
- Font Awesome icons
- Vanilla JavaScript

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Navigate to Project
```bash
cd /home/kkathish/Desktop/portfolio-kathish
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations (Already Done)
The database is already set up, but if you need to reset:
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Already Done)
A superuser has been created with:
- Username: `admin`
- Password: `admin123`
- Email: `admin@example.com`

To create a new superuser:
```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Or using the virtual environment:
```bash
./venv/bin/python manage.py runserver
```

The site will be available at: `http://127.0.0.1:8000/`

## Usage

### Admin Panel
Access the admin panel at: `http://127.0.0.1:8000/admin/`

Use the credentials:
- Username: `admin`
- Password: `admin123`

From the admin panel, you can:
1. Add/edit/delete Projects
2. Add/edit/delete Work Experience
3. Add/edit/delete Blog Posts
4. View Contact Messages

### Adding Content

**To add a Project:**
1. Go to Admin → Projects → Add Project
2. Fill in title, description, tech stack (comma-separated)
3. Add GitHub/Live links (optional)
4. Upload project image (optional)

**To add Experience:**
1. Go to Admin → Experiences → Add Experience
2. Fill in role, company, dates, and description
3. Check "Is current" if it's your current position

**To add a Blog Post:**
1. Go to Admin → Blogs → Add Blog
2. Fill in title and content
3. Slug will auto-generate from title
4. Upload featured image (optional)

### Theme Toggle
- Click the moon/sun icon in the navbar to switch between dark and light modes
- The theme preference is saved in localStorage and persists across sessions

## Project Structure

```
portfolio-kathish/
├── config/                 # Main project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py
├── core/                   # Core app (main pages)
│   ├── models.py          # Project, Experience, ContactMessage models
│   ├── views.py           # Class-based views
│   ├── forms.py           # Contact form
│   ├── admin.py           # Admin configuration
│   └── urls.py            # URL patterns
├── blog/                   # Blog app
│   ├── models.py          # Blog model
│   ├── views.py           # List and Detail views
│   ├── admin.py           # Admin configuration
│   └── urls.py            # URL patterns
├── templates/              # Django templates
│   ├── base.html          # Base template with navbar/footer
│   ├── 404.html           # Custom 404 page
│   ├── core/              # Core app templates
│   └── blog/              # Blog app templates
├── static/                 # Static files
│   ├── css/
│   │   └── style.css      # Custom CSS
│   └── js/
│       └── main.js        # Theme toggle, particles, mobile menu
├── media/                  # User-uploaded files
├── venv/                   # Virtual environment
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── README.md              # This file
```

## Models

### Project
- `title`: CharField
- `description`: TextField
- `tech_stack`: CharField (comma-separated)
- `github_link`: URLField (optional)
- `live_link`: URLField (optional)
- `image`: ImageField (optional)
- `created_at`: DateTimeField

### Experience
- `role`: CharField
- `company`: CharField
- `start_date`: DateField
- `end_date`: DateField (optional)
- `description`: TextField
- `is_current`: BooleanField

### Blog
- `title`: CharField
- `slug`: SlugField (auto-generated)
- `content`: TextField
- `featured_image`: ImageField (optional)
- `created_at`: DateTimeField

### ContactMessage
- `name`: CharField
- `email`: EmailField
- `message`: TextField
- `created_at`: DateTimeField

## Customization

### Colors
Edit `templates/base.html` to modify Tailwind config:
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: '#3b82f6',      // Change primary color
                secondary: '#10b981',    // Change secondary color
                dark: '#0f172a',         // Change dark mode bg
            }
        }
    }
}
```

### Background Animation
Modify `static/js/main.js` to adjust particle settings:
- `particles.number.value`: Number of particles
- `particles.size.value`: Particle size
- `particles.line_linked.distance`: Connection distance

## Deployment

### Production Settings
Before deploying to production, update `config/settings.py`:

1. Set `DEBUG = False`
2. Update `ALLOWED_HOSTS = ['yourdomain.com']`
3. Generate a new `SECRET_KEY`
4. Use a production database (PostgreSQL recommended)
5. Configure static file serving
6. Set up media file storage

### Collect Static Files
```bash
python manage.py collectstatic
```

## Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License
Free to use for personal projects.

## Author
Kathish

## Support
For issues or questions, use the contact form on the website.

---

**Enjoy building your portfolio! 🚀**
