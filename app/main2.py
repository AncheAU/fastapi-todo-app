from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()


#list of todos
todos = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": False,
        "priority": "high"
    },
    {
        "id": 2,
        "title": "Learn Git",
        "completed": False,
        "priority": "high"
    },
    {
        "id": 3,
        "title": "Learn uv",
        "completed": False,
        "priority": "low"
    }
]


class TodoCreate(BaseModel):
    title: str
    priority: Literal["high", "medium", "low"]


@app.get("/")
def home():
    return {
        "message": "Todo API is running."
    }

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_single_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    
    return {
        "error": f"Todo with ID {todo_id} does not exist."
    }

@app.post("/todos")
def create_todo(todo: TodoCreate):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": False,
        "priority": todo.priority.lower()
    }

    todos.append(new_todo)
    return new_todo

@app.get("/search/{todo_title}")
def search_todo_title(todo_title: str):
    result = []
    for todo in todos:
        if todo_title.lower() in todo["title"].lower():
            result.append(todo)
        else:
            return {
            "error": f"No title with '{todo_title}' exist."
            } 

    return {
        "results": result    
    }

@app.get("/stats")
def todo_statistics():
    total_todos = len(todos)
    total_completed = 0
    total_not_completed = 0

    for todo in todos:
        if todo["completed"]:
            total_completed += 1
        else:
            total_not_completed += 1
    
    return {
        "total": total_todos,
        "completed": total_completed,
        "pending": total_not_completed
    }

@app.get("/todos/priority/high")
def get_priority_high():
    result = []
    for todo in todos:
        if todo["priority"] == "high":
            result.append(todo)
        
        else:
            return "No priority with 'high'."
    
    return result

    
    