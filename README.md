# Advanced Attendance Management System

Advanced Attendance Management System built with FastAPI, MongoDB, and a responsive HTML/CSS/JavaScript frontend.

## Features

- Admin login and dashboard stats
- Student management with edit, delete, and Excel import
- Daily attendance marking
- Branch and semester attendance reports
- Student attendance status lookup
- HOD and teacher account management
- Teacher subject/class assignment workflow
- Student login portal
- Public attendance link for parent/student sharing
- WhatsApp-ready notification integration using Twilio environment variables

## Project Structure

```text
attendance_system/
├── backend/
│   ├── database.py
│   └── main.py
├── frontend/
│   ├── login.html
│   ├── dashboard.html
│   ├── admin_management.html
│   ├── settings.html
│   ├── add_student.html
│   ├── attendance.html
│   ├── student_status.html
│   ├── report.html
│   ├── hod_login.html
│   ├── hod_dashboard.html
│   ├── teacher_login.html
│   ├── teacher_dashboard.html
│   ├── student_login.html
│   ├── student_dashboard.html
│   ├── attendance_link.html
│   └── style.css
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10+
- MongoDB running locally or a MongoDB Atlas connection string

## Installation

1. Create and activate a virtual environment.
2. Install dependencies:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

3. Make sure MongoDB is running locally at `mongodb://localhost:27017/`, or set a custom URI:

```powershell
$env:MONGO_URI="mongodb://localhost:27017/"
```

## Run the Backend

From the project root:

```powershell
.\venv\Scripts\python.exe -m uvicorn backend.main:app --reload
```

API docs:

- `http://127.0.0.1:8000/docs`

## Open the Frontend

Local frontend entry points:

- `frontend/login.html`
- `frontend/student_login.html`
- `frontend/teacher_login.html`
- `frontend/hod_login.html`

When the app runs on FastAPI, the frontend is also available directly from the same server:

```text
http://127.0.0.1:8000/frontend/login.html
```

## Admin Credentials

```text
Username: admin
Password: admin123
```

## WhatsApp Notification Setup

Set these before starting the backend:

```powershell
$env:TWILIO_ACCOUNT_SID="your_sid"
$env:TWILIO_AUTH_TOKEN="your_token"
$env:TWILIO_WHATSAPP_FROM="whatsapp:+917024899669"
$env:PUBLIC_ATTENDANCE_URL="http://127.0.0.1:5500/frontend/attendance_link.html"
$env:STUDENT_PORTAL_URL="http://127.0.0.1:5500/frontend/student_login.html"
```

Then restart the backend.

## GitHub Publish Notes

This project is ready to be published, but Git must be installed on the machine first. After installing Git, use:

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Free Deployment Option

The easiest free deployment flow for this project is:

1. Push this code to GitHub.
2. Create a free MongoDB Atlas cluster and copy the connection string.
3. Create a Render web service from this repository.
4. Render will use `render.yaml` and start the app with Uvicorn.
5. Add these environment variables in Render:

```text
MONGO_URI=<your-mongodb-atlas-uri>
TWILIO_ACCOUNT_SID=<optional>
TWILIO_AUTH_TOKEN=<optional>
TWILIO_WHATSAPP_FROM=<optional>
PUBLIC_ATTENDANCE_URL=https://<your-render-service>.onrender.com/frontend/attendance_link.html
STUDENT_PORTAL_URL=https://<your-render-service>.onrender.com/frontend/student_login.html
```

Official references:

- Render free deploy docs: https://render.com/docs/free
- Render static sites docs: https://render.com/docs/static-sites
- MongoDB Atlas free cluster docs: https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/

## Notes

- Branches are limited to the configured engineering departments.
- Semesters are limited to `1` through `6`.
- Student roll number format is validated like `25014C04010`.
- WhatsApp delivery depends on valid Twilio credentials and an approved WhatsApp sender.
