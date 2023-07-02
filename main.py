from text import create_images, create_title_img
from overlay import compose_video
from reddit import get_submission
from tts import text_to_speech


def create_story(url: str) -> None:
    submission = get_submission(url)

    text_to_speech(submission.title, './audio/title.mpeg')
    words, times = text_to_speech(submission.selftext, './audio/output.mpeg')

    create_title_img(submission.title, './images')
    create_images(words, './images')

    compose_video('./videos/Gameplay15.mp4', './audio/output.mpeg', './audio/title.mpeg', './images', times, './output')


if __name__ == '__main__':
    url = input('url: ')

    create_story(url)
