from fastapi import APIRouter, status
from . import model, service
from src.database.core import DbSession
from src.auth.service import CurrentUser

#Bundle db: DbSession and Current user into router to avoid repetition?

router = APIRouter(
    prefix="/todos",
    tags=['Todos']
)

@router.post("/", response_model= model.TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(db: DbSession, todo: model.TodoCreate, current_user: CurrentUser):
    return service.create_todo(current_user, db, todo)


@router.get("/", response_model= list[model.TodoResponse])
def get_todos(db: DbSession, current_user: CurrentUser):
    return service.get_todos(current_user, db)


@router.get("/{todo_id}", response_model= model.TodoResponse)
def get_todo(db: DbSession, todo_id: int, current_user: CurrentUser):
    return service.get_todo_by_id(current_user, db, todo_id)


@router.put("/{todo_id}", response_model = model.TodoResponse)
def update_todo(db: DbSession, todo_id: int, todo_update: model.TodoUpdate, current_user: CurrentUser):
    return service.update_todo(current_user, db, todo_id, todo_update)


@router.put("/{todo_id}/complete", response_model = model.TodoResponse)
def complete_todo(db: DbSession, todo_id: int, current_user: CurrentUser):
    return service.complete_todo(current_user, db, todo_id)


@router.delete("/{todo_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_todo(db: DbSession, todo_id: int, current_user: CurrentUser):
    service.delete_todo(current_user, db, todo_id)