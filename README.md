## TechHive

TechHive is a full-stack social network for developers built with Django REST Framework on the backend and React on the frontend. It supports user registration, authentication, profiles, experience and education entries, posts, comments, likes, and GitHub repository lookup.

## Project Stack

- Backend: Django 5.2, Django REST Framework, Token Authentication
- Frontend: React 16, React Router, Redux, Redux Thunk
- Database: SQLite
- Package manager: `pip` for Python, `npm` for frontend dependencies

## Repository Layout

- `backend/` - Django project and API
- `frontend/` - React client
- `start-dev.ps1` - Windows launcher for starting both servers
- `.venv/` - Local virtual environment used for running the backend here

## Features

- Register and log in users
- Token-based authentication
- Create and edit developer profiles
- Add work experience and education
- View developer profiles
- Create posts, like posts, and comment on posts
- Fetch public GitHub repositories for a profile username
- Admin panel for managing backend data

## Current Branding

The app is branded as TechHive in the visible UI and API banner.

## Backend Setup

Change into the backend folder before running Django commands.

```powershell
cd backend
```

Install backend dependencies if needed.

```powershell
..\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Apply migrations.

```powershell
..\.venv\Scripts\python.exe manage.py migrate
```

Create a superuser for the admin panel.

```powershell
..\.venv\Scripts\python.exe manage.py createsuperuser
```

Run the backend development server.

```powershell
..\.venv\Scripts\python.exe manage.py runserver
```

The backend runs at `http://127.0.0.1:8000/`.

## Frontend Setup

Change into the frontend folder before running React commands.

```powershell
cd frontend
```

Install frontend dependencies if needed.

```powershell
npm install
```

Run the frontend development server.

```powershell
npm start
```

The frontend runs at `http://localhost:3000/`.

Build the frontend for production.

```powershell
npm run build
```

## One-Command Windows Launch

From the repository root, start both servers with:

```powershell
.\start-dev.ps1
```

This opens one PowerShell window for the backend and one for the frontend.

## Database Notes

- The active local database file is `backend/db_dev.sqlite3`
- This file was chosen to avoid inconsistent migration history from the old database
- If you want a clean reset, delete `backend/db_dev.sqlite3` and run `manage.py migrate` again

## API Endpoints

Base API URL:

```text
http://127.0.0.1:8000/api/
```

Available routes:

- `GET /api/` - API root with a short TechHive banner and endpoint list
- `POST /api/users` - Register a user
- `GET, POST /api/auth` - Read authenticated user data or log in
- `GET /api/posts` - List all posts
- `GET /api/posts/<id>` - Get a single post
- `POST /api/posts` - Create a post
- `POST /api/posts/<id>/like` - Like or unlike a post
- `POST /api/posts/<id>/comments` - Add a comment to a post
- `DELETE /api/posts/comments/<id>` - Delete a comment
- `GET /api/profile` - Get your profile
- `POST /api/profile` - Create or update your profile
- `GET /api/profile/me` - Alias for your own profile
- `GET /api/profiles` - List all profiles
- `GET /api/profile/<id>` - Get a profile by user id
- `POST /api/profile/experience` - Add experience
- `DELETE /api/profile/experience/<id>` - Delete experience
- `POST /api/profile/education` - Add education
- `DELETE /api/profile/education/<id>` - Delete education
- `GET /api/github/<username>` - Fetch GitHub repos for a username

## Admin Panel

Open the Django admin at:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser credentials you created with `createsuperuser`.

## Environment Variables

The backend settings file includes placeholders for GitHub API credentials.

```python
GIT_CLIENT_ID = ''
GIT_CLIENT_SECRET = ''
```

You can fill those in if you want higher GitHub API limits for profile repo lookup.

## Troubleshooting

- If the API root shows JSON, that is expected; the React app lives on port 3000.
- If `createsuperuser` fails, run `migrate` first.
- If the frontend fails on modern Node, the `cross-env NODE_OPTIONS=--openssl-legacy-provider` script is already configured.
- If you want to reset the backend database, remove `backend/db_dev.sqlite3` and migrate again.

## Notes

- The backend package name is still `devconnector` internally, even though the public app branding is TechHive.
- The project is intended for local development and learning, not production deployment as-is.
