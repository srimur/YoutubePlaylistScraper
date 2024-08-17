import os
import json
from rich.console import Console

console = Console()

def output_json(video_details):
    if not video_details:
        console.print("[bold red]No videos found or there was an error.[/bold red]")
        return

    # Prompt user for file name
    file_name = console.input("Enter the name for the JSON file (without extension): ")
    save_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{file_name}.json")

    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(video_details, f, ensure_ascii=False, indent=4)

    console.print(f"[bold green]Details saved to '{save_path}'[/bold green]")
