from setuptools import setup, find_packages

setup(
    name="playlist-scraper",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'playlist-scraper=scraper.cli:main',
        ],
    },
)
