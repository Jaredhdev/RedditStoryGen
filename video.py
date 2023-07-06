import os
import gdown

url = 'https://drive.google.com/uc?id=1weRn9yhOsq1Sf8t8lz6yg6Sy-ZOOj3o7'
output = '/tmp/minecraft15.mp4'

if not os.path.exists(output):
    gdown.download(url, output, quiet=False)