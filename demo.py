#!/usr/bin/env python3
"""
Demo script to showcase the todo application functionality in a single session
"""

from src.services.todo_service import TodoService
from src.cli.handlers import CLIHandlers

def demo():
    print("=== Todo Application Demo ===\n")

    # Initialize the application components
    todo_service = TodoService()
    handlers = CLIHandlers(todo_service)

    print("1. Adding a todo item:")
    result = handlers.handle_add("Buy groceries")
    print(result)
    print()

    print("2. Adding another todo item:")
    result = handlers.handle_add("Complete project")
    print(result)
    print()

    print("3. Viewing all todo items:")
    result = handlers.handle_view()
    print(result)
    print()

    print("4. Updating a todo item:")
    result = handlers.handle_update(1, "Buy groceries and cook dinner")
    print(result)
    print()

    print("5. Marking a todo item as completed:")
    result = handlers.handle_complete(2)
    print(result)
    print()

    print("6. Viewing all todo items after updates:")
    result = handlers.handle_view()
    print(result)
    print()

    print("7. Deleting a todo item:")
    result = handlers.handle_delete(1)
    print(result)
    print()

    print("8. Final view after deletion:")
    result = handlers.handle_view()
    print(result)

if __name__ == "__main__":
    demo()