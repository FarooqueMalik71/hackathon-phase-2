# Quickstart Guide: In-Memory Python Console Todo Application (Phase I)

**Feature**: 001-console-todo-app
**Date**: 2026-01-09
**Status**: Complete

## Overview

This guide provides essential information to quickly understand, set up, and run the in-memory Python console todo application. This application implements a simple CLI-based todo manager with core CRUD functionality using only Python standard library.

## Prerequisites

- Python 3.13 or higher
- UV package manager (optional, for environment management)
- Operating system: Windows, macOS, or Linux

## Installation

### Direct Execution (No Installation Required)
```bash
# Clone or download the repository
git clone [repository-url]
cd [repository-directory]

# Run the application directly
python src/main.py --help
```

### Using UV Environment (Recommended)
```bash
# Create and activate a UV-managed environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# The application uses only standard library, so no pip install needed
python src/main.py --help
```

## Basic Usage

### Adding a Todo Item
```bash
python src/main.py add "Buy groceries"
```

### Viewing All Todo Items
```bash
python src/main.py view
```

### Updating a Todo Item
```bash
python src/main.py update 1 "Buy groceries and cook dinner"
```

### Marking a Todo Item as Complete
```bash
python src/main.py complete 1
```

### Deleting a Todo Item
```bash
python src/main.py delete 1
```

### Interactive Mode
```bash
python src/main.py
# This enters interactive mode where you can enter commands without the prefix
```

## Example Session

```
$ python src/main.py add "Learn Python"
Added task: [1] "Learn Python" (Pending)

$ python src/main.py add "Build CLI app"
Added task: [2] "Build CLI app" (Pending)

$ python src/main.py view
Todo List:
[1] [ ] "Learn Python" (Added: 2026-01-09 16:30:45)
[2] [ ] "Build CLI app" (Added: 2026-01-09 16:30:46)

Total: 2 tasks (0 completed, 2 pending)

$ python src/main.py complete 1
Completed task [1]: "Learn Python"

$ python src/main.py view
Todo List:
[1] [X] "Learn Python" (Added: 2026-01-09 16:30:45)
[2] [ ] "Build CLI app" (Added: 2026-01-09 16:30:46)

Total: 2 tasks (1 completed, 1 pending)
```

## Project Structure

```
src/
├── main.py              # Entry point and CLI loop
├── cli/
│   ├── handlers.py      # Input/output handling
│   └── parser.py        # Command parsing
├── services/
│   ├── todo_service.py  # Business logic orchestration
│   └── validators.py    # Input validation
├── domain/
│   ├── entities.py      # TodoItem class and domain logic
│   └── exceptions.py    # Custom domain exceptions
├── repository/
│   └── in_memory_repo.py # In-memory storage implementation
└── utils/
    └── formatting.py    # Helper functions
```

## Configuration

This application has no external configuration files. All behavior is controlled by command-line arguments.

## Troubleshooting

### Common Issues

1. **Python Version Error**
   - Problem: "SyntaxError" or "ModuleNotFoundError"
   - Solution: Ensure Python 3.13+ is installed and being used

2. **Command Not Found**
   - Problem: "python: command not found"
   - Solution: Check that Python is installed and in your PATH

3. **Permission Error**
   - Problem: Permission denied when running
   - Solution: Ensure you have read/write permissions for the project directory

## Development

### Running Tests
```bash
python -m unittest discover tests/
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for public functions and classes

### Architecture Notes
- CLI Layer: Handles input/output and command parsing
- Service Layer: Orchestrates business logic
- Domain Layer: Contains business rules and entities
- Repository Layer: Manages data storage and retrieval

## Limitations

- Data is stored only in memory and is lost when the application exits
- Single-user, single-session application
- No persistent storage
- No network connectivity required or supported