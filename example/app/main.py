from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    env_message = os.getenv("APP_MESSAGE", "Hello from FastAPI!")
    return {"message": env_message}
