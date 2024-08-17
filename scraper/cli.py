import click
from scraper.utils import get_video_details
from scraper.text_output import output_text
from scraper.json_output import output_json

@click.group()
@click.version_option('1.0.0', message=click.style('YouTube Playlist Scraper version 1.0.0', fg='green', bold=True))
@click.option('--help', '-h', is_flag=True, callback=lambda ctx, param, value: ctx.invoke(cli) if value else None, expose_value=False, is_eager=True, help='Show this message and exit.')
@click.pass_context
def cli(ctx):
    """\b
    🎥 YouTube Playlist Scraper - A modern CLI tool to scrape YouTube playlist details.
    
    🚀 Features:
    - Scrape playlist details in text or JSON format
    - Simple and intuitive commands
    """
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@cli.command()
@click.option('--format', '-f', type=click.Choice(['text', 'json'], case_sensitive=False), default='text', help='Choose the output format (default: text).')
def scrape(format):
    """\b
    🔍 Scrape video details from a YouTube playlist.
    """
    url = click.prompt(click.style('Please enter the YouTube playlist URL', fg='cyan', bold=True), type=str)
    
    video_details = get_video_details(url)

    if format == "json":
        click.secho("\n🎉 Outputting in JSON format...\n", fg='yellow')
        output_json(video_details)
    elif format == "text":
        click.secho("\n📄 Outputting in Text format...\n", fg='yellow')
        output_text(video_details)

@click.command()
def version():
    """\b
    ℹ️  Show the scraper version.
    """
    click.echo(click.style("YouTube Playlist Scraper version 1.0.0", fg='green', bold=True))

cli.add_command(scrape)
cli.add_command(version)

if __name__ == "__main__":
    cli()
