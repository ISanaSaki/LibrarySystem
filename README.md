# 📚 Library Management System API

A modern **Library Management System** built with **FastAPI**,
**PostgreSQL**, and **SQLAlchemy**, featuring JWT authentication,
role-based access control, and full Docker support.

This project allows users to browse and borrow books, authors to manage
their own books, and admins to oversee the system.

------------------------------------------------------------------------

## 🚀 Features

-   ✨ User authentication with JWT\
-   ✨ Role-based access (user, author, admin)\
-   ✨ Author profiles & book management\
-   ✨ Borrow & return books\
-   ✨ Availability tracking\
-   ✨ Reports & statistics\
-   ✨ PostgreSQL + Alembic migrations\
-   ✨ Dockerized setup

------------------------------------------------------------------------

## 🛠 Tech Stack

-   **Backend:** FastAPI
-   **Database:** PostgreSQL
-   **ORM:** SQLAlchemy
-   **Auth:** JWT (OAuth2 Password Flow)
-   **Migrations:** Alembic
-   **Security:** Argon2 password hashing
-   **Containerization:** Docker & Docker Compose

------------------------------------------------------------------------

## 📂 Project Structure

    app/
    ├── api/            # API routes (Auth, Books, Authors, Borrow, Reports)
    ├── core/           # Config, security, dependencies
    ├── crud/           # Database operations
    ├── db/             # DB session & initialization
    ├── models/         # SQLAlchemy models
    ├── schemas/        # Pydantic schemas
    ├── utils/          # Permissions & helpers
    ├── main.py         # Application entry point
    alembic/            # Database migrations
    Dockerfile
    docker-compose.yml
    requirements.txt
    .env

------------------------------------------------------------------------

## 🔐 Authentication & Roles

Authentication is handled using **JWT tokens**.

### Roles

**User** - Borrow and return books\
- View available books

**Author** - Create author profile\
- Create, update, delete own books

**Admin** - Full access to all resources

------------------------------------------------------------------------

## 🔑 API Endpoints Overview

### Auth

-   `POST /api/auth/register` -- Register new user\
-   `POST /api/auth/login` -- Login & receive JWT

### Authors

-   `POST /api/authors/` -- Create author profile (Author only)

### Books

-   `POST /api/books/` -- Create book (Author/Admin)\
-   `GET /api/books/` -- List books\
-   `GET /api/books/{id}` -- Book details\
-   `PUT /api/books/{id}` -- Update book (Owner/Admin)\
-   `DELETE /api/books/{id}` -- Delete book (Owner/Admin)

### Borrow

-   `POST /api/borrow/borrow/{book_id}` -- Borrow a book\
-   `POST /api/borrow/return/{book_id}` -- Return a book

### Reports

-   `GET /api/reports/my-borrows` -- My borrowed books\
-   `GET /api/reports/my-books` -- My written books (Author)\
-   `GET /api/reports/borrowed-books` -- All borrowed books\
-   `GET /api/reports/stats` -- Library statistics

------------------------------------------------------------------------

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

``` env
DATABASE_URL=postgresql://postgres:postgres@db:5432/library
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

------------------------------------------------------------------------

## 🐳 Run with Docker (Recommended)

``` bash
docker-compose up --build
```

API will be available at:

-   http://localhost:8000\
-   Swagger docs: http://localhost:8000/docs

------------------------------------------------------------------------

## 🧪 Run Locally (Without Docker)

``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

------------------------------------------------------------------------

## 🧬 Database Migrations

Run migrations inside the container or locally:

``` bash
alembic upgrade head
```

------------------------------------------------------------------------

## 📊 Reports & Statistics

-   Total books\
-   Available vs borrowed books\
-   User borrowing history\
-   Author book listings

------------------------------------------------------------------------

## 🔒 Security Notes

-   Passwords are hashed using **Argon2**\
-   JWT tokens are signed and time-limited\
-   Ownership and role checks are enforced at API level

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome!\
Feel free to open issues or submit pull requests.
