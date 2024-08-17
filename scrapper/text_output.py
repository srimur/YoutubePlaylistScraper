import os
from rich.console import Console
from rich.table import Table

console = Console()

def output_text(video_details):
    if not video_details:
        console.print("[bold red]No videos found or there was an error.[/bold red]")
        return

    # Prompt user for file name
    file_name = console.input("Enter the name for the text file (without extension): ")
    save_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{file_name}.txt")

    with open(save_path, "w", encoding="utf-8") as f:
        for i, video in enumerate(video_details, start=1):
            f.write(f"{i}. {video['title']} ({video['url']})\n")

    console.print(f"[bold green]Titles saved to '{save_path}'[/bold green]")

    table = Table(title="YouTube Playlist Video Titles")
    table.add_column("No.", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta", no_wrap=True)

    for i, video in enumerate(video_details, start=1):
        table.add_row(str(i), f"[link={video['url']}] {video['title']}[/link]")

    console.print(table)
