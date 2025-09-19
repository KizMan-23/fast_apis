from fastapi import HTTPException, status

class TodoError(HTTPException):
    """Base Exception for todo-related errors"""
    pass

class TodoNotFoundError(TodoError):
    def __init__(self, todo_id=None):
        message = "Todo not found" if todo_id is None else f"Todo with id {todo_id} not found"
        super().__init__(status_code=404, detail=message)


class TodoCreationError(TodoError):
    def __init__(self, errror: str):
        super().__init__(status_code=500, detail=f"Failed to create todo: {errror}")


class UserError(HTTPException):
    """Base Exception for user-related errors"""
    pass


class UserNotFoundError(UserError):
    def __init__(self, user_id=None):
        message = "User not found" if user_id is None else f"User with id {user_id} not Found"
        super().__init__(status_code=404, detail=message)


class PasswordMismatchError(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="New Passwords do not match")


class InvalidPasswordError(UserError):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Current Password is incorrect")


class AuthenticationError(HTTPException):
    def __init__(self, message: str = "Could not Validate user"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=message)