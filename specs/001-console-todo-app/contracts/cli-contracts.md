# CLI Contracts: In-Memory Python Console Todo Application (Phase I)

**Feature**: 001-console-todo-app
**Date**: 2026-01-09
**Status**: Complete

## Overview

This document defines the command-line interface contracts for the in-memory Python console todo application. It specifies the command syntax, parameters, expected inputs, outputs, and error conditions based on the functional requirements in the feature specification.

## Command Contracts

### ADD Command

**Purpose**: Add a new todo item to the list

**Syntax**:
```
python main.py add "task description"
```

**Parameters**:
- Positional argument 1: `description` (string, required) - The task description to add

**Input Validation**:
- Description must be provided
- Description must be non-empty after trimming whitespace
- Description must be between 1 and 500 characters

**Success Output**:
```
Added task: [ID] "task description" (Pending)
```

**Error Conditions**:
- Missing description → Output: `"Error: Task description is required"`
- Empty description → Output: `"Error: Task description cannot be empty"`

### VIEW Command

**Purpose**: Display all todo items in the list

**Syntax**:
```
python main.py view
```

**Parameters**: None

**Success Output**:
```
Todo List:
[1] [ ] "Buy groceries" (Added: YYYY-MM-DD HH:MM:SS)
[2] [X] "Complete project" (Added: YYYY-MM-DD HH:MM:SS)
[3] [ ] "Call doctor" (Added: YYYY-MM-DD HH:MM:SS)

Total: 3 tasks (1 completed, 2 pending)
```

If no tasks exist:
```
Todo List is empty.
```

**Error Conditions**: None

### UPDATE Command

**Purpose**: Update the description of an existing todo item

**Syntax**:
```
python main.py update [ID] "new description"
```

**Parameters**:
- Positional argument 1: `id` (integer, required) - The ID of the task to update
- Positional argument 2: `description` (string, required) - The new task description

**Input Validation**:
- ID must be a positive integer
- ID must correspond to an existing task
- Description must be provided
- Description must be non-empty after trimming whitespace

**Success Output**:
```
Updated task [ID]: "new description"
```

**Error Conditions**:
- Invalid ID → Output: `"Error: Task with ID [ID] does not exist"`
- Missing ID → Output: `"Error: Task ID is required"`
- Missing description → Output: `"Error: New task description is required"`
- Empty description → Output: `"Error: Task description cannot be empty"`

### DELETE Command

**Purpose**: Remove a todo item from the list

**Syntax**:
```
python main.py delete [ID]
```

**Parameters**:
- Positional argument 1: `id` (integer, required) - The ID of the task to delete

**Input Validation**:
- ID must be a positive integer
- ID must correspond to an existing task

**Success Output**:
```
Deleted task [ID]: "task description"
```

**Error Conditions**:
- Invalid ID → Output: `"Error: Task with ID [ID] does not exist"`
- Missing ID → Output: `"Error: Task ID is required"`

### COMPLETE Command

**Purpose**: Mark a todo item as completed

**Syntax**:
```
python main.py complete [ID]
```

**Parameters**:
- Positional argument 1: `id` (integer, required) - The ID of the task to mark as completed

**Input Validation**:
- ID must be a positive integer
- ID must correspond to an existing task

**Success Output**:
```
Completed task [ID]: "task description"
```

**Error Conditions**:
- Invalid ID → Output: `"Error: Task with ID [ID] does not exist"`
- Missing ID → Output: `"Error: Task ID is required"`

## Global Error Handling

### General Error Format
```
Error: [descriptive error message]
```

### Common Error Conditions
- Invalid command → Output: `"Error: Unknown command '[command]'"`
- Missing command → Output: `"Error: Please specify a command (add, view, update, delete, complete)"`
- Invalid argument count → Output: `"Error: Incorrect number of arguments for '[command]' command"`

## Interactive Mode

If no command is provided, the application enters interactive mode:

**Syntax**:
```
python main.py
```

**Behavior**:
- Displays welcome message and command prompt
- Accepts commands interactively
- Shows help message for available commands
- Exits when user enters 'quit' or 'exit'

**Interactive Prompt Format**:
```
TodoApp> [awaiting command]
```

## Exit Codes

- `0`: Successful execution
- `1`: General error
- `2`: Command-line parsing error
- `3`: Invalid input/data error