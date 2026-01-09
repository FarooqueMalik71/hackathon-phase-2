---
description: "Task list for In-Memory Python Console Todo Application (Phase I)"
---

# Tasks: In-Memory Python Console Todo Application (Phase I)

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in src/
- [ ] T002 Create src/__init__.py file
- [ ] T003 [P] Create directory structure: src/cli/, src/services/, src/domain/, src/repository/, src/utils/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 [P] Create src/domain/entities.py with TodoItem class
- [ ] T005 [P] Create src/domain/exceptions.py with domain-specific exceptions
- [ ] T006 [P] Create src/repository/in_memory_repo.py with TodoList class
- [ ] T007 Create src/domain/__init__.py
- [ ] T008 Create src/repository/__init__.py
- [ ] T009 Create src/services/__init__.py
- [ ] T010 Create src/cli/__init__.py
- [ ] T011 Create src/utils/__init__.py
- [ ] T012 [P] Create src/utils/formatting.py with helper functions
- [ ] T013 Create src/services/validators.py with input validation functions

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to the list with proper validation

**Independent Test**: User can run the application, enter an "add" command with a task description, and see the task appear in their todo list without any other features implemented

### Implementation for User Story 1

- [ ] T014 [P] [US1] Implement TodoItem class with attributes (id, title, completed, created_at, updated_at) in src/domain/entities.py
- [ ] T015 [P] [US1] Implement TodoList repository with add operation in src/repository/in_memory_repo.py
- [ ] T016 [US1] Implement TodoService.add_todo method in src/services/todo_service.py
- [ ] T017 [US1] Create src/services/todo_service.py file
- [ ] T018 [US1] Implement CLI handler for add command in src/cli/handlers.py
- [ ] T019 [US1] Create src/cli/handlers.py file
- [ ] T020 [US1] Update command parser to handle add command in src/cli/parser.py
- [ ] T021 [US1] Create src/cli/parser.py file
- [ ] T022 [US1] Add validation for title length and non-empty requirement in src/services/validators.py
- [ ] T023 [US1] Create main entry point with basic CLI loop in src/main.py
- [ ] T024 [US1] Test adding a todo item with valid input and verify success output

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Todo Items (Priority: P1)

**Goal**: Enable users to view all their todo items with status and index

**Independent Test**: User can run the application, add some tasks, then view all tasks to see their complete list without needing other features

### Implementation for User Story 2

- [ ] T025 [P] [US2] Implement TodoList.list_all operation in src/repository/in_memory_repo.py
- [ ] T026 [US2] Implement TodoService.get_all_todos method in src/services/todo_service.py
- [ ] T027 [US2] Implement CLI handler for view command in src/cli/handlers.py
- [ ] T028 [US2] Update command parser to handle view command in src/cli/parser.py
- [ ] T029 [US2] Implement formatting function to display todos in src/utils/formatting.py
- [ ] T030 [US2] Test viewing all todo items with multiple items and verify proper display format

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo Item as Completed (Priority: P2)

**Goal**: Enable users to mark todo items as completed to track progress

**Independent Test**: User can run the application, add tasks, mark specific tasks as completed, and see the status change reflected when viewing the list

### Implementation for User Story 3

- [ ] T031 [P] [US3] Implement TodoList.update operation in src/repository/in_memory_repo.py
- [ ] T032 [US3] Implement TodoService.mark_completed method in src/services/todo_service.py
- [ ] T033 [US3] Implement CLI handler for complete command in src/cli/handlers.py
- [ ] T034 [US3] Update command parser to handle complete command in src/cli/parser.py
- [ ] T035 [US3] Add validation for valid ID/index in src/services/validators.py
- [ ] T036 [US3] Test marking a todo item as completed and verify status update

**Checkpoint**: User Stories 1, 2, and 3 should now be independently functional

---

## Phase 6: User Story 4 - Update Existing Todo Item (Priority: P2)

**Goal**: Enable users to update existing todo item descriptions

**Independent Test**: User can run the application, add tasks, update specific tasks with new descriptions, and verify the changes are reflected

### Implementation for User Story 4

- [ ] T037 [US4] Implement TodoService.update_todo method in src/services/todo_service.py
- [ ] T038 [US4] Implement CLI handler for update command in src/cli/handlers.py
- [ ] T039 [US4] Update command parser to handle update command in src/cli/parser.py
- [ ] T040 [US4] Add validation for valid ID/index and non-empty description in src/services/validators.py
- [ ] T041 [US4] Test updating a todo item with valid input and verify description change

**Checkpoint**: User Stories 1, 2, 3, and 4 should now be independently functional

---

## Phase 7: User Story 5 - Delete Todo Item (Priority: P3)

**Goal**: Enable users to delete todo items from the list

**Independent Test**: User can run the application, add tasks, delete specific tasks, and verify the deletion is reflected when viewing the list

### Implementation for User Story 5

- [ ] T042 [US5] Implement TodoList.delete operation in src/repository/in_memory_repo.py
- [ ] T043 [US5] Implement TodoService.delete_todo method in src/services/todo_service.py
- [ ] T044 [US5] Implement CLI handler for delete command in src/cli/handlers.py
- [ ] T045 [US5] Update command parser to handle delete command in src/cli/parser.py
- [ ] T046 [US5] Handle index adjustment after deletion to maintain sequential order in src/repository/in_memory_repo.py
- [ ] T047 [US5] Test deleting a todo item and verify it's removed from the list

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T048 [P] Add comprehensive error handling for invalid commands in src/cli/parser.py
- [ ] T049 [P] Implement proper error messages for all user stories in src/cli/handlers.py
- [ ] T050 [P] Add input validation for all commands in src/services/validators.py
- [ ] T051 [P] Implement interactive mode in src/main.py
- [ ] T052 [P] Add help functionality to display available commands in src/cli/parser.py
- [ ] T053 [P] Add proper exit codes to main application in src/main.py
- [ ] T054 [P] Update documentation in README.md with usage instructions
- [ ] T055 Run complete end-to-end tests to validate all functionality

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Core implementation before CLI integration
- Validation before command handling
- Repository operations before service methods
- Service methods before CLI handlers

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Models and utilities within foundational phase can run in parallel
- Different user stories should be implemented sequentially by priority

---

## Parallel Example: Foundational Phase

```bash
# Launch all foundational components together:
Task: "Create src/domain/entities.py with TodoItem class"
Task: "Create src/domain/exceptions.py with domain-specific exceptions"
Task: "Create src/repository/in_memory_repo.py with TodoList class"
Task: "Create src/utils/formatting.py with helper functions"
```

---

## Implementation Strategy

### MVP First (User Stories 1-2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Todo)
4. Complete Phase 4: User Story 2 (View Todos)
5. **STOP and VALIDATE**: Test User Stories 1-2 independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (Basic Add!)
3. Add User Story 2 → Test independently → Deploy/Demo (Add + View!)
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Sequential Team Strategy

With single developer:

1. Complete Setup + Foundational together
2. Complete User Story 1: Add functionality
3. Complete User Story 2: View functionality
4. Complete User Story 3: Complete functionality
5. Complete User Story 4: Update functionality
6. Complete User Story 5: Delete functionality
7. Complete Polish phase

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Tasks must follow the strict format: `- [ ] Txxx [P] [USx] Description with file path`