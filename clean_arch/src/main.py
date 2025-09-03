from fastapi import FastAPI
# from .database.core import engine, Base
from .entities.todo import Todo
from .entities.user import User


app = FastAPI()

# Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}