from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TodoCreate(BaseModel):
    title: str


#Todos
todos = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": False
    },
    {
        "id": 2,
        "title": "Learn Git",
        "completed": False
    },
    {
        "id": 3,
        "title": "Learn uv",
        "completed": True
    }
    
]


@app.get("/")
def home():
    return {
        "message": "Welcome to Abdullahi todo list."
    }


@app.get("/about")
def about():
    return {
        "app": "Todo API",
        "version": "1.0"
    }

@app.get("/todos")
def get_todos():
    return todos


@app.get("/health")
def get_health():
    return {
        "status": "healthy"
    }


@app.post("/todos")
def create_todo(todo : TodoCreate):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": False
    }

    todos.append(new_todo)
    return new_todo

@app.get("/todo/{todo_id}")
def get_single_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    
    return {
        "error": "Todo Not found."
    }