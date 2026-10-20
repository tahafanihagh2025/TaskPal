from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_dashboard():
    console.print(
        Panel(
            "[bold cyan]TaskPal[/bold cyan]\n"
            "Your personal task management system!\nWhat's on your mind today?",
            border_style="cyan",
            title="Welcome to TaskPal",
        )
    )

    table = Table(title="HOME")

    table.add_column("", justify="right")
    table.add_column("Home Menu")

    table.add_row("1", "Add a Task")
    table.add_row("2", "Complete / Delete a Task")
    table.add_row("3", "Edit a Task")
    table.add_row("4", "View Tasks")
    table.add_row("5", "AI Assistant")
    table.add_row("0", "Exit")

    console.print(table)
