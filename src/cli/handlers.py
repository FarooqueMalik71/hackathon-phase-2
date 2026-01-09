from src.services.todo_service import TodoService
from datetime import datetime


class CLIHandlers:
    """
    Handles CLI commands and user interactions
    """
    def __init__(self, todo_service: TodoService):
        self.todo_service = todo_service

    def handle_add(self, title: str) -> str:
        """Handle the add command"""
        try:
            todo = self.todo_service.add_todo(title)
            return f'Added task: [{todo.id}] "{todo.title}" (Pending)'
        except ValueError as e:
            return f"Error: {str(e)}"

    def handle_view(self) -> str:
        """Handle the view command"""
        todos = self.todo_service.get_all_todos()

        if not todos:
            return "Todo List is empty."

        output_lines = ["Todo List:"]
        completed_count = 0
        pending_count = 0

        for todo in todos:
            status = "X" if todo.completed else " "
            formatted_date = todo.created_at.strftime("%Y-%m-%d %H:%M:%S")
            output_lines.append(f"[{todo.id}] [{status}] \"{todo.title}\" (Added: {formatted_date})")
            if todo.completed:
                completed_count += 1
            else:
                pending_count += 1

        output_lines.append("")
        output_lines.append(f"Total: {len(todos)} tasks ({completed_count} completed, {pending_count} pending)")

        return "\n".join(output_lines)

    def handle_update(self, todo_id: int, new_title: str) -> str:
        """Handle the update command"""
        try:
            todo = self.todo_service.update_todo(todo_id, new_title)
            return f'Updated task [{todo.id}]: "{todo.title}"'
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"

    def handle_delete(self, todo_id: int) -> str:
        """Handle the delete command"""
        try:
            todo = self.todo_service.delete_todo(todo_id)
            return f'Deleted task [{todo.id}]: "{todo.title}"'
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"

    def handle_complete(self, todo_id: int) -> str:
        """Handle the complete command"""
        try:
            todo = self.todo_service.mark_completed(todo_id)
            return f'Completed task [{todo.id}]: "{todo.title}"'
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"