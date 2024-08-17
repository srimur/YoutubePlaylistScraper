import click
from scraper.utils import get_video_details
from scraper.text_output import output_text
from scraper.json_output import output_json

@click.group()
def cli():
    """YouTube Playlist Scraper - A modern CLI tool to scrape YouTube playlist details."""
    pass

@cli.command()
@click.option('--format', type=click.Choice(['text', 'json'], case_sensitive=False), default='text', help='Output format.')
def scrape(format):
    """Scrape video details from a YouTube playlist."""
    url = click.prompt('Please enter the YouTube playlist URL', type=str)
    
    video_details = get_video_details(url)

    if format == "json":
        output_json(video_details)
    elif format == "text":
        output_text(video_details)

@click.command()
def version():
    """Show the scraper version."""
    click.echo("YouTube Playlist Scraper version 1.0.0")

cli.add_command(scrape)
cli.add_command(version)

if __name__ == "__main__":
    cli()
