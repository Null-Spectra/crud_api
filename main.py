from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# in-memory list of task objects
tasks_db = [
    {"id": 1, "title": "Learn FastAPI", "done": True},
    {"id": 2, "title": "Build CRUD API", "done": False},
    {"id": 3, "title": "Publish to GitHub", "done": False},
]

# Stage 0
@app.get("/")
def home():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

# Stage 1
@app.get("/health")
def health():
    return {"status": "ok"}

# Stage 2
@app.get("/tasks")
def get_all_tasks():
    return tasks_db

@app.get("/tasks/{task_id}")
def get_single_task_by_id(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task

    return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"}
            )

