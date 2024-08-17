from setuptools import setup, find_packages

setup(
    name='youtube_playlist_scraper',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pytube',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'playlist-scraper=scraper.cli:cli',
        ],
    },
)
