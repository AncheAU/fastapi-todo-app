from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TodoCreate(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    completed: bool

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
        "id": max(todo["id"] for todo in todos) + 1,
        "title": todo.title,
        "completed": False
    }

    todos.append(new_todo)
    return new_todo

@app.get("/todos/{todo_id}")
def get_single_todo(todo_id : int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    
    return {
        "error": f"Todo with ID {todo_id} does not exist."
    }

@app.delete("/todos/{todo_id}")
def delete_todos(todo_id: int):
    for index, todo in enumerate(todos):
        if todo_id == todo["id"]:
            deleted_todo = todos.pop(index)

            return {
                "message": "Todo deleted successfully",
                "deleted": deleted_todo
            }
        
    return {
        "error": f"Todo with ID {todo_id} does not exist."
    }

@app.put("/todos/{todo_id}")
def update_todo(todo_id : int, todo_update: TodoUpdate):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = todo_update.completed

            return todo
        
    return {
        "error": f"Todo with ID {todo_id} does not exist."
        }

            