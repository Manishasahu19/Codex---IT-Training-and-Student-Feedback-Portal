# CodeX – IT Training & Student Feedback Portal

A full-stack Course Evaluation and Student Feedback Tracking System designed for IT training bootcamps.

##  Key Features
- **Full CRUD Pipeline:** Live record insertion via student forms and real-time database deletion from the dashboard.
- **Premium Dark UI:** Modern, high-contrast dark mode dashboard built using Bootstrap 5.
- **Automated Avatars:** Dynamic string-slicing logic to automatically generate user profile avatars from student initials.

---

##  Tech Stack
- **Backend:** Python, Django (MVT Architecture)
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, Bootstrap 5

---

##  Project Structure
```text
Feedback_Form/                  # Outer Container Folder
├── feedbackapp/               # Core Application (Views, Models, Routing)
├── Feedback_Form/             # Inner Management Folder (Settings, WSGI)
│   ├── settings.py
│   └── wsgi.py
├── manage.py                  # Django CLI Utility
└── requirements.txt           # Production Dependencies

Live link: [https://codex-it-training-and-student-feedback.onrender.com]
