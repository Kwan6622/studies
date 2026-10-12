from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    is_done: bool = False
    description: str = None

tasks = []

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/tasks", response_model=list[Task])
def list_tasks(limit: int = 10):
    return tasks[0:limit]

@app.get("/tasks/{task_id}", response_model=Task)
def get_item(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return {"Task": tasks[task_id]}

@app.post("/tasks")
def create_item(task: Task):
    tasks.append(task)
    return {"task": task}



