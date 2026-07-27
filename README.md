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
- SQLite
- DB Browser for SQLite
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

## Database Verification

To verify that the API reads directly from the SQLite database, I manually updated the database using DB Browser for SQLite while the FastAPI server was still running. Refreshing the API immediately reflected the changes without restarting the server.

### SQL Query Used

```sql
UPDATE tasks
SET title = 'Updated from DB Browser'
WHERE id = 1;
```

Result: After refreshing the GET /tasks/1 endpoint, the API returned the updated task title "Updated from DB Browser" without requiring a server restart.

## Status Codes

- 200 - OK
- 201 - Created
- 204 - No Content
- 400 - Bad Request
- 404 - Not Found

## Author

Urvi Porwal