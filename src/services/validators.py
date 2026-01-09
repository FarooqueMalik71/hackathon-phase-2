def validate_title(title: str) -> str:
    """Validate and clean a todo title"""
    if not title:
        raise ValueError("Task description is required")

    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("Task description cannot be empty")

    if len(cleaned_title) > 500:
        raise ValueError("Task description is too long (max 500 characters)")

    return cleaned_title


def validate_todo_id(todo_id: int, max_id: int = None) -> int:
    """Validate a todo ID"""
    if not isinstance(todo_id, int) or todo_id <= 0:
        raise ValueError("Task ID must be a positive integer")

    if max_id and todo_id > max_id:
        raise ValueError(f"Task with ID {todo_id} does not exist")

    return todo_id