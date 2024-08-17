import click
from rich.console import Console
from rich.table import Table
from scraper.utils import get_video_details
from scraper.text_output import output_text
from scraper.json_output import output_json

# Create a rich console instance
console = Console()

@click.group()
def cli():
    """YouTube Playlist Scraper - A modern CLI tool to scrape YouTube playlist details."""
    console.print("[bold magenta]YouTube Playlist Scraper[/bold magenta]", style="bold green")
    console.print("A tool to extract and manage YouTube playlist details.", style="dim")

@cli.command()
@click.option('--format', type=click.Choice(['text', 'json'], case_sensitive=False), default='text', help='Output format.')
def scrape(format):
    """Scrape video details from a YouTube playlist."""
    url = click.prompt('Please enter the YouTube playlist URL', type=str)
    
    try:
        video_details = get_video_details(url)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}", style="bold red")
        return

    if format == "json":
        output_json(video_details)
        console.print(f"[bold green]Video details have been saved to a JSON file.[/bold green]")
    elif format == "text":
        output_text(video_details)
        console.print(f"[bold green]Video details have been saved to a text file.[/bold green]")
        table = Table(title="YouTube Playlist Details")
        table.add_column("Title", style="cyan", no_wrap=True)
        table.add_column("Duration", style="magenta")
        table.add_column("URL", style="green")

        for video in video_details:
            table.add_row(video["title"], video["duration"], video["url"])

        console.print(table)

@cli.command()
def version():
    """Show the scraper version."""
    console.print("[bold cyan]YouTube Playlist Scraper version 1.0.0[/bold cyan]")

cli.add_command(scrape)
cli.add_command(version)

if __name__ == "__main__":
    cli()
