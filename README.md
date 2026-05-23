# 🎭 Pass Culture Full-Stack Application

<div align="center">

![React](https://img.shields.io/badge/Frontend-React-blue?style=for-the-badge&logo=react)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green?style=for-the-badge&logo=fastapi)
![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel)
![Render](https://img.shields.io/badge/Backend-Render-46E3B7?style=for-the-badge&logo=render)

A cloud-native full-stack application integrating external APIs, secure backend authentication, CAPTCHA solving, and managed cloud services.

</div>

---

# 📚 Table of Contents

- [📖 Project Overview](#-project-overview)
- [🎯 Problem Statement](#-problem-statement)
- [🏗 Architecture](#-architecture)
- [⚙️ Technologies Used](#️-technologies-used)
- [🔌 APIs & Services](#-apis--services)
- [📁 Repository Structure](#-repository-structure)
- [🚀 Local Setup](#-local-setup)
- [☁️ Deployment](#️-deployment)
- [🔐 Security](#-security)
- [🧪 Test Plan](#-test-plan)
- [⚠️ Known Limitations](#️-known-limitations)
- [🔮 Future Improvements](#-future-improvements)
- [🌍 Live Deployment](#-live-deployment)
- [👥 Team Roles](#-team-roles)
- [📄 Conclusion](#-conclusion)

---

# 📖 Project Overview

This project is a **full-stack cloud-native web application** allowing users to authenticate with their Pass Culture account and retrieve:

- 👤 Profile information
- 💳 Remaining credit balance
- 🎟 Booking history

The application demonstrates a modern digital ecosystem architecture built around:

- external APIs
- backend orchestration
- cloud hosting
- managed databases
- secure authentication flows

---

# 🎯 Problem Statement

Pass Culture users do not currently have a lightweight dashboard allowing simplified access to their account information through a modern web interface.

This project solves that problem by providing:

✅ A clean React frontend  
✅ Secure backend authentication  
✅ External API integration  
✅ Persistent cloud storage  
✅ Fully deployed cloud infrastructure  

---

# 🏗 Architecture

## System Architecture Diagram

```text
+---------------------------+
|       React Frontend      |
|         (Vercel)          |
+-------------+-------------+
              |
              | HTTPS Requests
              v
+---------------------------+
|      FastAPI Backend      |
|         (Render)          |
+-------------+-------------+
              |
    -------------------------
    |                       |
    v                       v

+----------------+   +----------------+
| PassCulture API|   | 2Captcha API   |
+----------------+   +----------------+

              |
              v

+---------------------------+
| Supabase PostgreSQL DB    |
|     (Cloud Database)      |
+---------------------------+
```

---

# ⚙️ Technologies Used

## 🎨 Frontend

- React
- JavaScript
- HTML/CSS
- Fetch API

## 🐍 Backend

- Python
- FastAPI
- Requests
- Uvicorn

## 🗄 Database

- Supabase
- PostgreSQL

## ☁️ Cloud Platforms

- Vercel
- Render
- Supabase

---

# 🔌 APIs & Services

## 🎭 PassCulture API

Used for:

- User authentication
- Profile retrieval
- Bookings retrieval

### Endpoints Used

```text
/native/v1/signin
/native/v1/me
/native/v2/bookings/ended
```

---

## 🤖 2Captcha API

Used for:

- Solving reCAPTCHA v2 challenges
- Automating authentication flow

Website:

```text
https://2captcha.com
```

---

## 🟢 Supabase API

Used for:

- Persistent cloud storage
- PostgreSQL database management
- Session-related storage

Website:

```text
https://supabase.com
```

---

# 📁 Repository Structure

```text
project-root/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── ...
│
├── README.md
└── .gitignore
```

---

# 🚀 Local Setup

## 📋 Prerequisites

Install:

- Node.js
- Python 3.11+
- Git

---

# 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/passculture-project.git
cd passculture-project
```

---

# 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs on:

```text
http://localhost:3000
```

---

# 3️⃣ Backend Setup

## Windows

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## macOS/Linux

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

# 4️⃣ Environment Variables

Create a `.env` file inside `/backend`:

```env
TWOCAPTCHA_KEY=your_2captcha_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

---

# 5️⃣ Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

# ☁️ Deployment

## 🌐 Frontend Deployment (Vercel)

### Configuration

| Setting | Value |
|---|---|
| Framework Preset | Create React App |
| Root Directory | frontend |
| Build Command | npm run build |
| Output Directory | build |

---

## ⚡ Backend Deployment (Render)

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

### Environment Variables

```env
TWOCAPTCHA_KEY=your_key
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

---

# 🔐 Security

This project follows secure backend practices:

✅ API keys stored in environment variables  
✅ No secrets exposed in frontend  
✅ Backend acts as secure proxy  
✅ CAPTCHA solved server-side  
✅ Tokens protected from public exposure  

---

# 🧪 Test Plan

## 🎨 Frontend Tests

| Test | Expected Result |
|---|---|
| Login form loads | UI displayed correctly |
| Submit credentials | Backend request sent |
| Invalid login | Error message shown |
| Successful login | Dashboard displayed |

---

## 🐍 Backend Tests

| Test | Expected Result |
|---|---|
| API reachable | HTTP 200 |
| CAPTCHA solved | Token returned |
| Login request | Access token received |
| Profile request | Profile data returned |
| Bookings request | Booking list returned |

---

## 🗄 Database Tests

| Test | Expected Result |
|---|---|
| Insert session | Row created |
| Retrieve data | Data available |
| Persistence | Data remains after restart |

---

# ⚠️ Known Limitations

- CAPTCHA solving introduces latency
- Dependency on external APIs
- Potential API rate limits
- No official OAuth support available

---

# 🔮 Future Improvements

- Replace CAPTCHA solving with OAuth if available
- Improve UI/UX design
- Add caching system
- Implement retry queues
- Improve mobile responsiveness
- Add analytics dashboard

---

# 🌍 Live Deployment

## 🎨 Frontend

```text
https://passculture-project.vercel.app
```

## 🐍 Backend

```text
https://passculture-project.onrender.com
```

---

# 👥 Team Roles

| Role | Responsibility |
|---|---|
| Backend Lead | API integration & authentication |
| Frontend Lead | React UI & UX |
| Cloud & DevOps Lead | Deployment & infrastructure |
| QA & Documentation Lead | Testing & documentation |
| Project Manager | Coordination & planning |

---

# 📄 Conclusion

This project demonstrates a modern digital ecosystem architecture combining:

- external APIs
- secure backend logic
- cloud-native deployment
- managed database infrastructure
- frontend/backend separation

The application reflects how modern software systems are built today through orchestration of services rather than monolithic local applications.

---

<div align="center">

## 🚀 Digital Ecosystem – Spring 2026

Built with React, FastAPI, Supabase, Render & Vercel.

</div>

