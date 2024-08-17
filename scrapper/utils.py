from pytube import Playlist, YouTube
from rich.progress import track

def get_video_details(playlist_url: str):
    try:
        playlist = Playlist(playlist_url)
        video_details = []

        for video in track(playlist.videos, description="Scraping videos..."):
            yt_video = YouTube(video.watch_url)
            video_info = {
                'title': video.title,
                'url': video.watch_url,
                'duration': video.length,
                'views': video.views,
                'author': video.author,
                'description': yt_video.description,
                'publish_date': video.publish_date.isoformat() if video.publish_date else None,
            }
            video_details.append(video_info)

        return video_details

    except Exception as e:
        print(f"Error: {str(e)}")
        return []
