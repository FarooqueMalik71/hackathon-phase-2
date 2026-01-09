#!/usr/bin/env python3
"""
Entry point for the In-Memory Python Console Todo Application (Phase I)
"""

import sys
import os
# Add the project root to the Python path so imports work correctly
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.cli.parser import CLICommandParser
from src.services.todo_service import TodoService
from src.cli.handlers import CLIHandlers


def main():
    """Main entry point for the todo application"""
    # Initialize the application components with persistent storage
    todo_service = TodoService(storage_file=".todo_storage.json")
    handlers = CLIHandlers(todo_service)
    parser = CLICommandParser()

    # Parse command-line arguments
    args = parser.parse_args()

    if args is None:
        # If no command was provided, exit gracefully
        sys.exit(1)

    try:
        # Execute the appropriate command
        if args.command == "add":
            if not hasattr(args, 'description') or not args.description:
                print("Error: Task description is required")
                sys.exit(3)
            result = handlers.handle_add(args.description)
            print(result)

        elif args.command == "view":
            result = handlers.handle_view()
            print(result)

        elif args.command == "update":
            if not hasattr(args, 'description') or not args.description:
                print("Error: New task description is required")
                sys.exit(3)
            result = handlers.handle_update(args.id, args.description)
            print(result)

        elif args.command == "delete":
            result = handlers.handle_delete(args.id)
            print(result)

        elif args.command == "complete":
            result = handlers.handle_complete(args.id)
            print(result)

        else:
            # This should not happen due to argparse validation
            print(f"Error: Unknown command '{args.command}'")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()