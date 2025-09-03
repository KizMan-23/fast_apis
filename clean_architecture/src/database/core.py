from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import Depends
import os
from dotenv import load_dotenv

load_dotenv()

#add Database url to env file
DATABASE_URL = os.getenv("DATABASE_URL")

# """Hard Code of PostgreSQL"""
# DATABASE_URL = "postgresql://postgres:postgres@db:5432/cleanfastapi"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]