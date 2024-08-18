import click
from scraper.utils import get_video_details
from scraper.text_output import output_text
from scraper.json_output import output_json
from scraper.notion_output import output_notion

def choose_format():
    """Prompt the user to select an output format using click options."""
    options = [
        ('1', 'Text'),
        ('2', 'JSON'),
        ('3', 'Notion Checklist'),
    ]

    click.echo("Choose the output format:")
    for key, option in options:
        click.echo(f"{key}. {option}")
    
    choice = click.prompt(click.style("Enter the number of your choice", fg='cyan'), type=int)

    if choice == 1:
        return 'text'
    elif choice == 2:
        return 'json'
    elif choice == 3:
        return 'notion'
    else:
        click.secho("Invalid choice. Exiting...", fg='red')
        exit(1)

@click.group()
@click.version_option('1.0.0', message=click.style('YouTube Playlist Scraper version 1.0.0', fg='green', bold=True))
def cli():
    """\b
    🎥 YouTube Playlist Scraper - A modern CLI tool to scrape YouTube playlist details.
    
    🚀 Features:
    - Scrape playlist details in text, JSON, or Notion checklist format
    - Simple and intuitive commands
    """
    pass

@cli.command()
@click.option('--format', '-f', type=str, help='Choose the output format (text, json, or notion).')
def scrape(format):
    """🔍 Scrape video details from a YouTube playlist."""
    if format is None:
        format = choose_format()

    url = click.prompt(click.style('Please enter the YouTube playlist URL', fg='cyan', bold=True), type=str)
    
    video_details = get_video_details(url)

    if format == "json":
        click.secho("\n🎉 Outputting in JSON format...\n", fg='yellow')
        output_json(video_details)
    elif format == "text":
        click.secho("\n📄 Outputting in Text format...\n", fg='yellow')
        output_text(video_details)
    elif format == "notion":
        click.secho("\n📝 Outputting as a Notion checklist...\n", fg='yellow')
        output_notion(video_details)
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
