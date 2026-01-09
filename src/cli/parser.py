import argparse


class CLICommandParser:
    """
    Parses command-line arguments and returns parsed command
    """
    def __init__(self):
        self.parser = self._create_parser()

    def _create_parser(self):
        parser = argparse.ArgumentParser(
            description="In-Memory Python Console Todo Application",
            prog="todo"
        )
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Add command
        add_parser = subparsers.add_parser("add", help="Add a new todo item")
        add_parser.add_argument("description", nargs="*", help="Task description")

        # View command
        view_parser = subparsers.add_parser("view", help="View all todo items")

        # Update command
        update_parser = subparsers.add_parser("update", help="Update an existing todo item")
        update_parser.add_argument("id", type=int, help="ID of the task to update")
        update_parser.add_argument("description", nargs="*", help="New task description")

        # Delete command
        delete_parser = subparsers.add_parser("delete", help="Delete a todo item")
        delete_parser.add_argument("id", type=int, help="ID of the task to delete")

        # Complete command
        complete_parser = subparsers.add_parser("complete", help="Mark a todo item as completed")
        complete_parser.add_argument("id", type=int, help="ID of the task to mark as completed")

        return parser

    def parse_args(self, args=None):
        """Parse command-line arguments"""
        parsed_args = self.parser.parse_args(args)

        # Handle the case where no command is provided
        if parsed_args.command is None:
            self.parser.print_help()
            return None

        # Join description parts back into a single string
        if hasattr(parsed_args, 'description') and parsed_args.description:
            parsed_args.description = ' '.join(parsed_args.description)

        return parsed_args