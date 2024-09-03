import click
from scraper.utils import get_video_details
from scraper.text_output import output_text
from scraper.json_output import output_json
from scraper.notion_output import output_notion
from concurrent.futures import ThreadPoolExecutor

def custom_theme():
    return {
        'header': {'fg': 'green', 'bold': True},
        'input': {'fg': 'cyan'},
        'error': {'fg': 'red', 'bold': True},
        'success': {'fg': 'yellow'},
        'ascii_art': {'fg': 'magenta', 'bold': True}
    }

def display_ascii_art():
    art = r"""
 __    __  ______  ____                                                               
/\ \  /\ \/\__  _\/\  _`\                                                             
\ `\`\\/'/\/_/\ \/\ \ \L\ \____    ___   _ __    __     _____   _____      __   _ __  
 `\ `\ /'    \ \ \ \ \ ,__/',__\  /'___\/\`'__\/'__`\  /\ '__`\/\ '__`\  /'__`\/\`'__\
   `\ \ \     \ \ \ \ \ \/\__, `\/\ \__/\ \ \//\ \L\.\_\ \ \L\ \ \ \L\ \/\  __/\ \ \/ 
     \ \_\     \ \_\ \ \_\/\____/\ \____\\ \_\\ \__/.\_\\ \ ,__/\ \ ,__/\ \____\\ \_\ 
      \/_/      \/_/  \/_/\/___/  \/____/ \/_/ \/__/\/_/ \ \ \/  \ \ \/  \/____/ \/_/ 
                                                          \ \_\   \ \_\               
                                                           \/_/    \/_/               
    """
    click.secho(art, **custom_theme()['ascii_art'])

@click.group()
@click.version_option('1.0.0', message=click.style('YouTube Playlist Scraper version 1.0.0', **custom_theme()['header']))
def cli():
    """\b
    🎥 YouTube Playlist Scraper - A modern CLI tool to scrape YouTube playlist details.
    
    🚀 Features:
    - Scrape playlist details in text, JSON, or Notion checklist format
    - Simple and intuitive commands
    """
    display_ascii_art()

def choose_format():
    """Prompt the user to select an output format using click options."""
    options = [
        ('1', 'Text'),
        ('2', 'JSON'),
        ('3', 'Notion Checklist'),
    ]

    click.echo(click.style("Choose the output format:", **custom_theme()['header']))
    for key, option in options:
        click.echo(f"{key}. {option}")
    
    choice = click.prompt(click.style("Enter the number of your choice", **custom_theme()['input']), type=int)

    format_map = {1: 'text', 2: 'json', 3: 'notion'}
    return format_map.get(choice, None)

@cli.command()
@click.option('--format', '-f', type=str, help='Choose the output format (text, json, or notion). If not provided, you will be prompted to choose.')
def scrape(format):
    """🔍 Scrape video details from a YouTube playlist."""
    if format is None:
        format = choose_format()

    if not format:
        click.secho("Invalid choice. Exiting...", **custom_theme()['error'])
        return

    url = click.prompt(click.style('Please enter the YouTube playlist URL', **custom_theme()['input'], bold=True), type=str)
    
    with ThreadPoolExecutor() as executor:
        video_details = executor.submit(get_video_details, url).result()

    format_map = {
        'json': ('\n🎉 Outputting in JSON format...\n', output_json),
        'text': ('\n📄 Outputting in Text format...\n', output_text),
        'notion': ('\n📝 Outputting as a Notion checklist...\n', output_notion),
    }

    output_msg, output_func = format_map.get(format, (None, None))
    if output_msg:
        click.secho(output_msg, **custom_theme()['success'])
        output_func(video_details)
    else:
        click.secho("Invalid format selected.", **custom_theme()['error'])

@cli.command()
def version():
    """ℹ️ Show the scraper version."""
    click.echo(click.style("YouTube Playlist Scraper version 1.0.0", **custom_theme()['header']))

cli.add_command(scrape)
cli.add_command(version)

if __name__ == "__main__":
    cli()
