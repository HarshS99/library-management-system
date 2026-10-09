```
# Library Management System 📚

[![Build Status](https://github.com/HarshS99/library-management-system/actions/workflows/ci.yml/badge.svg)](https://github.com/HarshS99/library-management-system/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Node.js Version](https://img.shields.io/badge/node-16+-green.svg)](https://nodejs.org/)
[![GitHub Stars](https://img.shields.io/github/stars/HarshS99/library-management-system?style=social)](https://github.com/HarshS99/library-management-system/stargazers)

A full-stack **Library Management System** built with **FastAPI**, **React**, and **PostgreSQL**, featuring user authentication, book management, issue/return tracking, and a responsive dashboard.

---

## ✨ Features

- 🔐 **User Authentication** (JWT-based)
- 📖 **Book Management** (CRUD operations)
- 📂 **Book Categories & Search**
- 📅 **Issue & Return Records**
- 📊 **Responsive Dashboard** (React)
- 🛡️ **Role-based Access Control** (Admin/Librarian/User)
- 📦 **Dockerized Deployment**

---

## 🛠️ Tech Stack

| **Backend**       | **Frontend** | **Database** | **DevOps**       |
|-------------------|-------------|-------------|------------------|
| FastAPI (Python)  | React       | PostgreSQL  | Docker           |
| SQLAlchemy        | TypeScript  |             | Docker Compose   |
| JWT Auth          | TailwindCSS |             | GitHub Actions   |

---

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Node.js (v16+)
- Python (3.9+)

### Installation

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/HarshS99/library-management-system.git
cd library-management-system
```

#### 2️⃣ Environment Setup
```bash
cp .env.example .env
# Update .env with your PostgreSQL credentials
```

#### 3️⃣ Start Services
```bash
docker-compose up --build
```

#### 4️⃣ Access the Application
- **Backend (FastAPI)**: `http://localhost:8000`
- **Frontend (React)**: `http://localhost:3000`
- **PostgreSQL**: `postgresql://user:password@db:5432/library_db`

---

## 💡 Usage Examples

### API Endpoints (FastAPI)
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Login & get JWT token |
| `GET` | `/books` | List all books |
| `POST` | `/books/issue` | Issue a book |
| `POST` | `/books/return` | Return a book |

### React Dashboard
- **Admin Panel**: Manage users & books
- **Librarian Panel**: Track issues/returns
- **User Panel**: View borrowed books

---

## 📂 Folder Structure
```
library-management-system/
├── backend/                # FastAPI application
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── core/           # JWT & config
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic models
│   │   └── main.py         # FastAPI entry
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/               # React application
│   ├── public/
│   ├── src/
│   │   ├── components/     # Reusable UI
│   │   ├── pages/          # Dashboard pages
│   │   ├── services/       # API calls
│   │   └── App.tsx
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 🏗️ Architecture Diagram

```
┌─────────────┐    ┌─────────────┐    ┌─────────────────┐
│   React     │    │   FastAPI   │    │   PostgreSQL    │
│  Frontend   │◄──►│  Backend    │◄──►│   Database      │
└─────────────┘    └─────────────┘    └─────────────────┘
       ▲                  ▲                  ▲
       │                  │                  │
┌──────┴──────┐    ┌──────┴──────┐    ┌──────┴──────┐
│   Docker    │    │   Docker    │    │   Docker    │
│  Container  │    │  Container  │    │  Container  │
└─────────────┘    └─────────────┘    └─────────────┘
```

---

## 🤝 Contributing
Contributions are welcome! Please follow:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/foo`)
3. Commit changes (`git commit -m 'Add foo'`)
4. Push to branch (`git push origin feature/foo`)
5. Open a Pull Request

---

## 📜 License
This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.
```