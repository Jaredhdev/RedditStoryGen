import os
import gdown


def download_video():
    url = 'https://drive.google.com/uc?id=1weRn9yhOsq1Sf8t8lz6yg6Sy-ZOOj3o7'
    output = 'videos/minecraft15.mp4'  # path to where you want the file

    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)
