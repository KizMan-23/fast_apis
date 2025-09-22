from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum, Integer
from enum import IntEnum
from datetime import datetime, timezone
from ..database.core import Base


class PriorityLevel(IntEnum):
    NORMAL = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)
    due_date = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    priority = Column(Enum(PriorityLevel), default=PriorityLevel.NORMAL, nullable=False)
    
    def __repr__(self):
        return f"<Todo(id={self.id}, title={self.title}, due_date= {self.due_date}, is_completed={self.is_completed})>"
