import json
import os
from typing import List, Optional
from src.domain.entities import TodoItem
from src.domain.exceptions import TodoNotFoundError


class TodoList:
    """
    Collection of TodoItem objects managed in memory with optional persistence
    """
    def __init__(self, storage_file: str = None):
        self.storage_file = storage_file or ".todo_storage.json"
        self.items: List[TodoItem] = []
        self.next_id: int = 1
        self.load_from_storage()

    def load_from_storage(self):
        """Load todos from storage file if it exists"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.items = []
                    for item_data in data['items']:
                        # Create TodoItem from stored data
                        item = TodoItem(
                            id=item_data['id'],
                            title=item_data['title'],
                            completed=item_data['completed'],
                        )
                        # Set datetime values if they exist
                        if 'created_at' in item_data and item_data['created_at']:
                            from datetime import datetime
                            item.created_at = datetime.fromisoformat(item_data['created_at'])
                        if 'updated_at' in item_data and item_data['updated_at']:
                            from datetime import datetime
                            item.updated_at = datetime.fromisoformat(item_data['updated_at'])
                        self.items.append(item)
                    self.next_id = data.get('next_id', 1)
            except (json.JSONDecodeError, KeyError):
                # If there's an error loading, start fresh
                self.items = []
                self.next_id = 1
        else:
            self.items = []
            self.next_id = 1

    def save_to_storage(self):
        """Save todos to storage file"""
        data = {
            'items': [
                {
                    'id': item.id,
                    'title': item.title,
                    'completed': item.completed,
                    'created_at': item.created_at.isoformat() if item.created_at else None,
                    'updated_at': item.updated_at.isoformat() if item.updated_at else None
                }
                for item in self.items
            ],
            'next_id': max([item.id for item in self.items] + [0]) + 1
        }
        with open(self.storage_file, 'w') as f:
            json.dump(data, f)

    def add(self, title: str) -> TodoItem:
        """Add a new todo item to the list"""
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")

        if len(title) > 500:
            raise ValueError("Title must be between 1 and 500 characters")

        todo = TodoItem(
            id=self.next_id,
            title=title.strip()
        )
        self.items.append(todo)
        self.next_id = max([item.id for item in self.items] + [0]) + 1
        self.save_to_storage()
        return todo

    def get_all(self) -> List[TodoItem]:
        """Return all todo items in the collection"""
        return self.items.copy()

    def get_by_id(self, todo_id: int) -> TodoItem:
        """Get a todo item by its ID"""
        for item in self.items:
            if item.id == todo_id:
                return item
        raise TodoNotFoundError(f"Todo with ID {todo_id} does not exist")

    def update(self, todo_id: int, new_title: str) -> TodoItem:
        """Update the title of an existing todo item"""
        if not new_title or not new_title.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")

        if len(new_title) > 500:
            raise ValueError("Title must be between 1 and 500 characters")

        for item in self.items:
            if item.id == todo_id:
                item.update_title(new_title.strip())
                self.save_to_storage()
                return item
        raise TodoNotFoundError(f"Todo with ID {todo_id} does not exist")

    def mark_completed(self, todo_id: int) -> TodoItem:
        """Mark a todo item as completed"""
        for item in self.items:
            if item.id == todo_id:
                item.mark_completed()
                self.save_to_storage()
                return item
        raise TodoNotFoundError(f"Todo with ID {todo_id} does not exist")

    def delete(self, todo_id: int) -> TodoItem:
        """Remove a todo item from the list"""
        for i, item in enumerate(self.items):
            if item.id == todo_id:
                deleted_item = self.items.pop(i)
                # Adjust IDs of subsequent items to maintain sequential order
                for j, subsequent_item in enumerate(self.items[i:], i):
                    subsequent_item.id = j + 1
                self.save_to_storage()
                return deleted_item
        raise TodoNotFoundError(f"Todo with ID {todo_id} does not exist")