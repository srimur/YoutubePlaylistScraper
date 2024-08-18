from setuptools import setup, find_packages

setup(
    name="playlist-scraper",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'rich',
        'pytube',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'playlist-scraper=scraper.cli:cli',
        ],
    },
)
