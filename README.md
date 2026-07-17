# Task API

This is a simple Task Management API developed using FastAPI as part of my FlyRank Backend Internship assignment.

## Features

- View all tasks
- View a task by ID
- Add a new task
- Update an existing task
- Delete a task
- Automatic API documentation using Swagger

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

## How to Run

Install the required packages:

```bash
pip install fastapi uvicorn
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

| Method | Endpoint |
|--------|----------|
| GET | `/` |
| GET | `/health` |
| GET | `/tasks` |
| GET | `/tasks/{task_id}` |
| POST | `/tasks` |
| PUT | `/tasks/{task_id}` |
| DELETE | `/tasks/{task_id}` |

## Status Codes

- 200 - OK
- 201 - Created
- 204 - No Content
- 400 - Bad Request
- 404 - Not Found

## Author

Urvi Porwal