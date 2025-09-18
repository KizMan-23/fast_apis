from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from src.entities.todo import PriorityLevel

class TodoBase(BaseModel):
    title: str
    description: str
    due_date: Optional[datetime] = None
    priority: PriorityLevel = PriorityLevel.MEDIUM

class TodoCreate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: UUID
    is_completed: bool
    completed_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class TodoUpdate(TodoBase):
    title: Optional[str] = Field(None,max_length=500)
    description: Optional[str] = Field(None)
    due_date: Optional[datetime] = Field(None)
    priority: Optional[PriorityLevel] = Field(None)