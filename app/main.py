from fastapi import FastAPI

app = FastAPI()

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