from fastapi.responses import JSONResponse
from supabase_client import supabase
from database import(
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task
)
from fastapi import FastAPI, HTTPException, Header, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

app = FastAPI()
security = HTTPBearer(auto_error=False)

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
def create_new_task(task: Task):
    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    return create_task(task.title, task.done)

@app.put("/tasks/{task_id}")
def update_existing_task(task_id: int, updated_task: Task):

    task = update_task(
        task_id,
        updated_task.title,
        updated_task.done
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_existing_task(task_id: int):

    deleted = delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return

class AuthRequest(BaseModel):
    email: str
    password: str

@app.post("/auth/signup")
def signup(user: AuthRequest):

    if not user.email or not user.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password required"
        )

    response = supabase.auth.sign_up(
        {
            "email": user.email,
            "password": user.password
        }
    )

    return response

@app.post("/auth/login")
def login(user: AuthRequest):

    if not user.email or not user.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password required"
        )

    response = supabase.auth.sign_in_with_password(
        {
            "email": user.email,
            "password": user.password
        }
    )

    return response

@app.get("/public/info")
def public_info():
    return {
        "message": "Welcome stranger! This info is public."
    }

@app.get("/protected/profile")
def protected_profile(
    credentials: HTTPAuthorizationCredentials | None = Security(security)
):
    if credentials is None:
        return JSONResponse(
            status_code=401,
            content={"error": "Access token required"}
        )

    token = credentials.credentials

    user = supabase.auth.get_user(token)

    return {
        "id": user.user.id,
        "email": user.user.email,
        "created_at": user.user.created_at
    }