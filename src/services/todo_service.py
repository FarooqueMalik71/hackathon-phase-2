from typing import List
from src.repository.in_memory_repo import TodoList
from src.domain.entities import TodoItem
from src.services.validators import validate_title, validate_todo_id


class TodoService:
    """
    Service class to orchestrate todo operations
    """
    def __init__(self, storage_file=None):
        self.todo_list = TodoList(storage_file=storage_file)

    def add_todo(self, title: str) -> TodoItem:
        """Add a new todo item"""
        validated_title = validate_title(title)
        return self.todo_list.add(validated_title)

    def get_all_todos(self) -> List[TodoItem]:
        """Get all todo items"""
        return self.todo_list.get_all()

    def update_todo(self, todo_id: int, new_title: str) -> TodoItem:
        """Update an existing todo item"""
        validated_title = validate_title(new_title)
        validated_id = validate_todo_id(todo_id)
        return self.todo_list.update(validated_id, validated_title)

    def mark_completed(self, todo_id: int) -> TodoItem:
        """Mark a todo item as completed"""
        validated_id = validate_todo_id(todo_id)
        return self.todo_list.mark_completed(validated_id)

    def delete_todo(self, todo_id: int) -> TodoItem:
        """Delete a todo item"""
        validated_id = validate_todo_id(todo_id)
        return self.todo_list.delete(validated_id)