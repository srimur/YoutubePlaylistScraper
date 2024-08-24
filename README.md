# YouTube Playlist Scraper

A simple CLI tool to scrape video details from a YouTube playlist. 
(New - Notion Checklist Mardown as Output)

## Features
- Extract video titles and save them in a text file along with a table with clickable links.
- Extract detailed video information and save it in a JSON file.
- **Output Video Titles as Checklist Hyperlinks for Notion (Copy Paste Markdown) - Use to keep track of videos completed watching**
- Easy-to-use CLI with clear output options.

## Demo

![gif11](https://github.com/user-attachments/assets/962086dd-35fc-408d-a77e-1676bd56ca24)

### Notion Markdown Output (Copies to Clipboard)
<img width="860" alt="image" src="https://github.com/user-attachments/assets/7a08104e-60de-4042-9df0-60f3ec366d33">
<br>

- The Markdown automatically gets copied to clipboard (or you can manually copy it from the output provided)
- Paste the Markdown in you Notion Page
- Now you can keep track of watched videos and strike it as you complete, These are hyperlinks to the videos.
  
<br>
<img src="https://github.com/user-attachments/assets/387b0de1-6a50-44a6-a1cf-b90e625c37c3" alt="gif11" width="800"/>


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



