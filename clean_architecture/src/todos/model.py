from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from src.entities.todo import PriorityLevel

class TodoBase(BaseModel):
    title: str |  None
    description: str
    due_date: Optional[datetime] = None
    priority: PriorityLevel = PriorityLevel.MEDIUM

class TodoCreate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: int
    is_completed: bool
    completed_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class TodoUpdate(BaseModel): 
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[PriorityLevel] = None