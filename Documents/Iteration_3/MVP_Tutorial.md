# Tutorial: Building, Installing, and Running the Course Planner App

This tutorial will guide you through setting up and running the Course Planner application, which consists of a Django backend and a Next.js frontend.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 18+** and **npm** - [Download Node.js](https://nodejs.org/)
- **Git** - For version control

**Note:** This tutorial uses macOS/Linux commands. If you're on Windows, use PowerShell or Git Bash, and replace `source env/bin/activate` with `env\Scripts\activate`.

## Project Structure

```
course-planner/
├── Code/
│   ├── backend/     # Django REST API
│   └── frontend/    # Next.js React app
```

---

## Part 1: Backend Setup (Django)

### Step 1: Navigate to Backend Directory

```bash
# Replace <project-directory> with your actual project path
cd <project-directory>/Code/backend
```

**Example:**

```bash
cd ~/Documents/course-planner/Code/backend
# or
cd /path/to/your/project/Code/backend
```

### Step 2: Create and Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
source env/bin/activate
```

You should see `(env)` prefix in your terminal prompt.

### Step 3: Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If `requirements.txt` is incomplete, install these essential packages:

```bash
pip install django djangorestframework django-cors-headers python-dotenv requests beautifulsoup4
```

### Step 4: Configure Environment Variables

Create a `.env` file in the backend directory:

```bash
touch .env
```

Add the following content to `.env`:

```env
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
DATABASE_URL=sqlite:///db.sqlite3
```

### Step 5: Verify Django Settings

Make sure all apps are registered in `backend/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'authsvc',
    'coursessvc',
    'catalogsrv',
    'plannersvc',
    'api',
]
```

### Step 6: Run Database Migrations

```bash
# Create migrations for all apps
python3 manage.py makemigrations

# Apply migrations to database
python3 manage.py migrate
```


### Step 7: Load Sample Data

```bash
# Insert course data
python3 manage.py insert_data
python3 manage.py sacrape_programs
```

If you encounter module errors, install missing packages:

```bash
pip install requests beautifulsoup4
```

### Step 9: Run the Django Development Server

```bash
python3 manage.py runserver
```

The backend should now be running at **http://127.0.0.1:8000/**

**Test the backend:**

- Admin panel: http://127.0.0.1:8000/admin/
- API endpoints: http://127.0.0.1:8000/api/

Keep this terminal window open!

---

## Part 2: Frontend Setup (Next.js)

### Step 1: Open New Terminal Window

Open a new terminal window/tab (keep the backend running in the first one).

### Step 2: Navigate to Frontend Directory

```bash
# Replace <project-directory> with your actual project path
cd <project-directory>/Code/frontend
```

**Example:**

```bash
cd ~/Documents/course-planner/Code/frontend
# or
cd /path/to/your/project/Code/frontend
```

### Step 3: Install Node.js Dependencies

```bash
npm install
```

This will install all packages listed in `package.json`.

### Step 4: Configure Environment Variables

Create a `.env.local` file in the frontend directory:

```bash
touch .env.local
```

Add the following content:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api
```

### Step 5: Run the Development Server

```bash
npm run dev
```

The frontend should now be running at **http://localhost:3000/**

---

### Stopping the Application

Press `Ctrl+C` in each terminal window.

### Deactivating Virtual Environment

```bash
deactivate
```

---

## Part 6: Building for Production

### Backend Production Setup

```bash
cd backend

# Update settings.py
# Set DEBUG=False
# Configure ALLOWED_HOSTS
# Use environment variables for sensitive data

# Collect static files
python3 manage.py collectstatic

# Use production server (e.g., Gunicorn)
pip install gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
```

### Frontend Production Build

```bash
cd frontend

# Create production build
npm run build

# Start production server
npm start
```


Once everything is set up, use these commands to start the app:

```bash
# Terminal 1 - Backend
cd <project-directory>/Code/backend
source env/bin/activate
python3 manage.py runserver

# Terminal 2 - Frontend
cd <project-directory>/Code/frontend
npm run dev
```

Then open http://localhost:3000 in your browser.


