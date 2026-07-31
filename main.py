from database import get_all_tasks, get_task_by_id
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL
)
""")

cursor.execute("SELECT COUNT(*) FROM tasks")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany("""
    INSERT INTO tasks (title, done)
    VALUES (?, ?)
    """, [
        ("Learn FastAPI", False),
        ("Build CRUD API", False),
        ("Submit Assignment", False)
    ])

conn.commit()

tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build CRUD API", "done": False},
    {"id": 3, "title": "Submit Assignment", "done": False},
]

@app.get("/")
def home():
    return {"name": "Task API",
    "version": "1.0",
    "endpoints": ["/tasks"]}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return get_all_tasks()

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

class Task(BaseModel):
    title: str
    done: bool

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    if task.title.strip() == "":
        raise HTTPException(
        status_code=400,
        detail="Title cannot be empty"
        )
    cursor.execute(
    "INSERT INTO tasks (title, done) VALUES (?, ?)",
    (task.title, False)
)

    conn.commit()

    new_id = cursor.lastrowid

    return {
        "id": new_id,
        "title": task.title,
        "done": False
    }

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    cursor.execute(
        """
        UPDATE tasks
        SET title = ?, done = ?
        WHERE id = ?
        """,
        (updated_task.title, updated_task.done, task_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    conn.commit()

    return {
        "id": task_id,
        "title": updated_task.title,
        "done": updated_task.done
    }

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    conn.commit()
    return