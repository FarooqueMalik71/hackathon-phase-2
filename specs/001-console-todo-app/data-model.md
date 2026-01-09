# Data Model: In-Memory Python Console Todo Application (Phase I)

**Feature**: 001-console-todo-app
**Date**: 2026-01-09
**Status**: Complete

## Overview

This document defines the data model for the in-memory Python console todo application. It describes the core entities, their attributes, relationships, and validation rules based on the functional requirements in the feature specification.

## Core Entities

### TodoItem

**Description**: Represents a single todo task in the application

**Attributes**:
- `id` (int): Unique identifier for the todo item; auto-incremented
- `title` (str): Short description of the task; required field
- `completed` (bool): Status indicator showing whether the task is completed; default: False
- `created_at` (datetime): Timestamp when the item was added; auto-generated
- `updated_at` (datetime): Timestamp when the item was last modified; auto-updated

**Validation Rules**:
- `id` must be a positive integer
- `title` must be a non-empty string (1-500 characters)
- `title` cannot contain only whitespace
- `completed` must be a boolean value
- `created_at` must be a valid datetime object
- `updated_at` must be a valid datetime object

**State Transitions**:
- New item: `completed = False` (default)
- When marked complete: `completed = True`
- When marked incomplete: `completed = False`
- When updated: `updated_at` is refreshed to current time

### TodoList

**Description**: Collection of TodoItem objects managed in memory

**Attributes**:
- `items` (list[TodoItem]): Ordered collection of TodoItem objects
- `next_id` (int): Counter for generating unique IDs; auto-incremented

**Operations**:
- Add: Insert new TodoItem to the list and assign next available ID
- Retrieve: Access TodoItem by ID or index position
- Update: Modify existing TodoItem properties
- Delete: Remove TodoItem from the list
- List: Return all TodoItems in the collection
- Find: Search for TodoItems by property (e.g., completed status)

**Validation Rules**:
- `items` must be a list containing only TodoItem objects
- Each TodoItem in the list must have a unique ID
- `next_id` must be a positive integer greater than any existing ID in the collection

## Relationships

### TodoItem → TodoList
- Each TodoItem belongs to exactly one TodoList
- TodoList contains zero or more TodoItem objects
- Relationship is managed through the `items` attribute of TodoList

## Data Flow Patterns

### Creation Flow
1. User provides title for new todo item
2. System validates title meets requirements
3. System assigns next available ID from TodoList counter
4. System creates TodoItem with provided title, ID, and default values
5. System adds TodoItem to TodoList.items collection
6. System updates TodoList.next_id counter

### Update Flow
1. User provides ID/index and new title for existing todo item
2. System validates ID/index exists in TodoList
3. System updates TodoItem.title with new value
4. System updates TodoItem.updated_at timestamp
5. System returns confirmation of update

### Completion Flow
1. User provides ID/index of todo item to mark complete
2. System validates ID/index exists in TodoList
3. System updates TodoItem.completed to True
4. System updates TodoItem.updated_at timestamp
5. System returns confirmation of completion

### Deletion Flow
1. User provides ID/index of todo item to delete
2. System validates ID/index exists in TodoList
3. System removes TodoItem from TodoList.items collection
4. System adjusts indices if needed to maintain sequential order
5. System returns confirmation of deletion

## Constraints

### Integrity Constraints
- No duplicate IDs allowed within a TodoList
- No null titles allowed in TodoItems
- IDs must remain consistent even after deletions (no reuse of deleted IDs)

### Business Constraints
- Items can only be marked complete/incomplete (binary state)
- Items maintain creation order in the list
- Deleted items' positions are filled by subsequent items shifting down to maintain sequential indices

## Serialization Format

For internal memory representation, the data model uses native Python objects:
- TodoItem: Python class instance with attributes
- TodoList: Python list containing TodoItem instances

**Note**: Since this is an in-memory application with no persistence, serialization is not required for external storage.