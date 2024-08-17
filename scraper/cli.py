import click
from prompt_toolkit.shortcuts import radiolist_dialog
from scraper.utils import get_video_details
from scraper.text_output import output_text
from scraper.json_output import output_json

def prompt_for_format():
    """Prompt the user to select an output format using a dialog with radio buttons."""
    format_options = [
        ("Text", "text"),
        ("JSON", "json")
    ]
    
    result = radiolist_dialog(
        title="Choose Output Format",
        text="Select the output format:",
        values=format_options,
    ).run()

    if result is None:
        click.secho("No format selected. Exiting...", fg='red')
        exit(1)
    return result

@click.group()
@click.version_option('1.0.0', message=click.style('YouTube Playlist Scraper version 1.0.0', fg='green', bold=True))
def cli():
    """\b
    🎥 YouTube Playlist Scraper - A modern CLI tool to scrape YouTube playlist details.
    
    🚀 Features:
    - Scrape playlist details in text or JSON format
    - Simple and intuitive commands
    """
    pass

@cli.command()
@click.option('--format', '-f', type=str, help='Choose the output format (text or json).')
def scrape(format):
    """🔍 Scrape video details from a YouTube playlist."""
    if format is None:
        format = prompt_for_format()

    url = click.prompt(click.style('Please enter the YouTube playlist URL', fg='cyan', bold=True), type=str)
    
    video_details = get_video_details(url)

    if format == "json":
        click.secho("\n🎉 Outputting in JSON format...\n", fg='yellow')
        output_json(video_details)
    elif format == "text":
        click.secho("\n📄 Outputting in Text format...\n", fg='yellow')
        output_text(video_details)
    else:
        click.secho("Invalid format selected.", fg='red')

@cli.command()
def version():
    """ℹ️  Show the scraper version."""
    click.echo(click.style("YouTube Playlist Scraper version 1.0.0", fg='green', bold=True))

cli.add_command(scrape)
cli.add_command(version)

if __name__ == "__main__":
    cli()
