import pytest
from src.todos import service as todo_service
from src.todos.model import TodoCreate
from src.exceptions import TodoNotFoundError, TodoCreationError
from src.entities.todo import Todo


class TestTodosService:
    def test_create_todo(self, db_session, test_token_data):
        todo_create = TodoCreate(
            title = "A Test Todo",
            description="Creating New Todo"
        )
        new_todo = todo_service.create_todo(test_token_data, db_session, todo_create)
        assert new_todo.description == "Creating New Todo"
        assert new_todo.user_id == test_token_data.get_uuid()
        assert not new_todo.is_completed

    
    # def test_create_todo_error(self, db_session, test_token_data):
    #     with pytest.raises(TodoCreationError):
    #         todo_create = TodoCreate(
    #             description="Creating Todo without Title"
    #         )
    #         todo_service.create_todo(test_token_data, db_session, todo_create)

    def test_get_todos(self, db_session, test_token_data, test_todo):
        test_todo.user_id = test_token_data.get_uuid()
        db_session.add(test_todo)
        db_session.commit()
        db_session.refresh(test_todo)

        todo = todo_service.get_todos(test_token_data, db_session)
        assert len(todo) == 1
        assert todo[0].id == test_todo.id

    
    def test_get_todo_by_id(self, db_session, test_token_data, test_todo):
        test_todo.user_id = test_token_data.get_uuid()
        db_session.add(test_todo)
        db_session.commit()
        db_session.refresh(test_todo)

        todo = todo_service.get_todo_by_id(test_token_data, db_session, test_todo.id)
        assert todo.id == test_todo.id
        assert todo.user_id == test_todo.user_id
        assert todo.description == "Test Description"

        with pytest.raises(TodoNotFoundError):
            todo_service.get_todo_by_id(test_token_data, db_session, 100)

    
    def test_complete_todo(self, db_session, test_token_data, test_todo):
        test_todo.user_id = test_token_data.get_uuid()
        db_session.add(test_todo)
        db_session.commit()
        db_session.refresh(test_todo)

        completed_todo = todo_service.complete_todo(test_token_data, db_session, test_todo.id)
        assert  completed_todo.is_completed
        assert completed_todo.completed_at is not None


    def test_delete_todo(self, db_session, test_token_data, test_todo):
        test_todo.user_id = test_token_data.get_uuid()
        db_session.add(test_todo)
        db_session.commit()
        db_session.refresh(test_todo)

        todo_service.delete_todo(test_token_data, db_session, test_todo.id)
        assert db_session.query(Todo).filter_by(id=test_todo.id).first() is None