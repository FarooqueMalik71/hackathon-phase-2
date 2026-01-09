class TodoError(Exception):
    """Base exception for todo-related errors"""
    pass


class TodoNotFoundError(TodoError):
    """Raised when a todo item is not found"""
    pass


class InvalidTodoError(TodoError):
    """Raised when a todo item is invalid"""
    pass