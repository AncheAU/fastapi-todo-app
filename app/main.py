from fastapi import FastAPI

app = FastAPI()

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
