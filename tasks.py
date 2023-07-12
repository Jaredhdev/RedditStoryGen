from celery import Celery
import os
import csv

from text import create_images, create_title_img
from overlay import compose_video
from tts import text_to_speech
from video import download_video, upload_video

# Initialize Celery
celery = Celery(__name__)

redis_url = 'redis://:pa835a2983f9cf8e5e85c13198a0d3f4a1433518e2afec3ef88a9b0ab321b17e7@ec2-3-219-149-39.compute-1' \
            '.amazonaws.com:24019'

# Set Celery configuration to use Heroku Redis
celery.conf.broker_url = redis_url
celery.conf.result_backend = redis_url


@celery.task
def process_video(title: str, text: str, unique_id: str):
    dir_path = './' + unique_id
    os.makedirs(dir_path)

    download_video()
    text_to_speech(title, f'{dir_path}/title.mpeg')
    words, times = text_to_speech(text, f'{dir_path}/text.mpeg')
    create_title_img(title, dir_path)
    create_images(words, dir_path)
    compose_video(dir_path, times, unique_id)
    upload_video(f"{dir_path}/{unique_id}.mp4")

    print('Video generation completed.')
