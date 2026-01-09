# In-Memory Python Console Todo Application (Phase I)

This is a command-line todo application that stores data in memory with optional file persistence. It demonstrates clean architecture with separation of concerns between presentation, domain logic, and state management.

## Features

- Add new todo items
- View all todo items
- Update existing todo items
- Delete todo items
- Mark todo items as completed
- Persistent storage (data persists between application runs)

## Requirements

- Python 3.13+

## Usage

### Add a Todo Item
```bash
python src/main.py add "Your task description"
```

### View All Todo Items
```bash
python src/main.py view
```

### Update a Todo Item
```bash
python src/main.py update [ID] "New task description"
```

### Mark a Todo Item as Completed
```bash
python src/main.py complete [ID]
```

### Delete a Todo Item
```bash
python src/main.py delete [ID]
```

### Get Help
```bash
python src/main.py --help
```

## Examples

```bash
# Add a task
python src/main.py add "Buy groceries"

# View all tasks
python src/main.py view

# Mark task #1 as completed
python src/main.py complete 1

# Update task #2
python src/main.py update 2 "Buy groceries and cook dinner"

# Delete task #1
python src/main.py delete 1
```

## Architecture

The application follows a clean architecture pattern with four distinct layers:

- **CLI Layer**: Handles input/output and command parsing (`src/cli/`)
- **Service Layer**: Orchestrates business logic (`src/services/`)
- **Domain Layer**: Contains business rules and entities (`src/domain/`)
- **Repository Layer**: Manages data storage and retrieval (`src/repository/`)

## Persistence

The application stores data in `.todo_storage.json` in the project root. This allows data to persist between application runs while maintaining the in-memory nature of the application.

## Error Handling

The application provides clear error messages for invalid inputs:
- Non-existent task IDs
- Empty or invalid task descriptions
- Invalid command usage