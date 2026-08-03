# Task API - Authentication & JWT

A secure Task API built using FastAPI and Supabase Auth. This project implements user signup, login, logout, JWT verification, and protected routes as part of the FlyRank Backend Internship assignment.

## Features

- User signup using Supabase Auth
- User login with JWT access tokens
- JWT token verification
- Protected routes
- User logout
- Swagger UI with Bearer authentication
- Secure environment variable handling

## Technologies

- Python
- FastAPI
- Supabase Auth
- JWT
- PostgreSQL
- Uvicorn
- Docker

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
uvicorn main:app --reload
```

Open Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Authentication |
|--------|----------|----------------|
| POST | `/auth/signup` | ❌ |
| POST | `/auth/login` | ❌ |
| POST | `/auth/logout` | ✅ |
| GET | `/protected/profile` | ✅ |
| GET | `/public/info` | ❌ |

## Status Codes

- 200 - OK
- 201 - Created
- 204 - No Content
- 400 - Bad Request
- 404 - Not Found
- 401 - Unauthorized (Missing or invalid JWT token)
- 403 - Forbidden (Authenticated user does not have permission)

## Environment Variables

Create a `.env` file:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```
A .env.example file is included for reference. Never commit real secrets.

## Swagger UI Overview

![Swagger UI Overview](assests/Swagger-UI-Overview.png)

## Bearer Authentication

![Bearer Authentication](assests/Bearer-Authentication.png)

## Author

Urvi Porwal
