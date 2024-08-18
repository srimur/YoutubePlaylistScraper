# YouTube Playlist Scraper

A simple CLI tool to scrape video details from a YouTube playlist. 

## Features
- Extract video titles and save them in a text file with clickable links.
- Extract detailed video information and save it in a JSON file.
- Easy-to-use CLI with clear output options.

## Demo

![gif11](https://github.com/user-attachments/assets/962086dd-35fc-408d-a77e-1676bd56ca24)

### Text output
<img width="619" alt="pic11" src="https://github.com/user-attachments/assets/d1eb6bf9-410e-4226-813d-e7ca85787eca">

### JSON Output
<img width="649" alt="pic12" src="https://github.com/user-attachments/assets/0b84eb9a-f30c-421e-95d4-f56f217cc23d">


## Usage
```bash
playlist-scraper scrape --format text
```
After selecting the format, the tool will prompt you to enter the YouTube playlist URL.

## Steps to Set Up and Use the Project

### 1. Clone the Repository:
```bash
git clone https://github.com/srimur/YoutubePlaylistScraper.git
```
```bash
cd YoutubePlaylistScraper
```

### 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 3. Install the CLI Tool:
```bash
pip install -e .
```



