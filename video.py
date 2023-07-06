import os
from pytube import YouTube


def download_video():
    youtube_url = 'https://www.youtube.com/watch?v=t2rfSQ9s92s'

    download_path = '/videos'

    filename = 'minecraft15.mp4'

    youtube = YouTube(youtube_url)

    if not os.path.exists(os.path.join(download_path, filename)):
        youtube.streams.get_highest_resolution().download(output_path=download_path, filename=filename)