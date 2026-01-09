from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class TodoItem:
    """
    Represents a single todo task in the application
    """
    id: int
    title: str
    completed: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = self.created_at

    def mark_completed(self):
        """Mark the todo item as completed"""
        self.completed = True
        self.updated_at = datetime.now()

    def update_title(self, new_title: str):
        """Update the title of the todo item"""
        self.title = new_title
        self.updated_at = datetime.now()