from fastapi import FastAPI
from .auth.controller import router as auth_router
from .users.controller import router as users_router
from .todos.controller import router as todos_router
from .logs import configure_logging, LogLevels
from .database.core import Base, engine


configure_logging(LogLevels.INFO)

app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(todos_router)


#Create DataBase
Base.metadata.create_all(bind=engine)
