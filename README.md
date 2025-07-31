# 🧠 AI-Powered Website Builder (Django + MongoDB + OpenAI)

This is a backend system for dynamically generating and managing AI-powered websites using OpenAI GPT models. It includes user authentication, role-based access control, MongoDB integration, and live HTML previews.

---

## 🚀 Features

- 🔐 **JWT Authentication** via Email (Sign Up / Login)
- 👥 **Role-Based Access Control (ACL)** – Admin, Editor, Viewer
- 🤖 **AI Website Content Generator** using OpenAI
- 🗂️ **MongoDB** for scalable content storage
- 🛠️ **Website Management APIs** – Create, Read, Update, Delete
- 🌐 **Live Preview** using HTML templates
- ✅ **Multi-user support** and scalable architecture

---

## 🛠️ Tech Stack

| Tool         | Usage                         |
|--------------|-------------------------------|
| Django       | Backend Framework              |
| MongoEngine  | MongoDB ODM for Django         |
| JWT          | Stateless Authentication       |
| OpenAI API   | Content Generation             |
| Bootstrap    | Frontend HTML Template         |
| Django REST Framework | API Development      |

---

## 📦 Installation & Setup

### 1. Clone the project

``bash
git clone https://github.com/poonamsweet/Website_Builder.git
cd Website_Builder

### 2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate         # For Windows

### 3. Install Python dependencies by using command

pip install -r requirements.txt

### 4. Set up environment variables

OPENAI_API_KEY=your-openai-key
### 5 run the commands
python manage.py makemigrations
python manage.py migrate



### 6. Start the development server
python manage.py runserver


📚 API Endpoints

🔐 Authentication

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| POST   | `/api/register/` | Register a new user      |
| POST   | `/api/login/`    | Log in and get JWT token |


👤 Admin: User & Role Management

| Method | Endpoint         | Description                           |
| ------ | ---------------- | ------------------------------------- |
| POST   | `/api/generate/` | Generate website content using OpenAI |



🤖 AI-Powered Website Generation

Method	Endpoint	Description
POST	/api/generate/	Generate website content using OpenAI

| Method | Endpoint              | Description                  |
| ------ | --------------------- | ---------------------------- |
| GET    | `/api/websites/`      | List all websites for a user |
| POST   | `/api/websites/`      | Create a new website         |
| GET    | `/api/websites/<id>/` | Get website details by ID    |
| PUT    | `/api/websites/<id>/` | Update website content       |
| DELETE | `/api/websites/<id>/` | Delete website               |
