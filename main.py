from text import create_images, create_title_img
from overlay import compose_video
from reddit import get_submission
from tts import text_to_speech

if __name__ == '__main__':
    title = ''
    text = ''

    text_to_speech(title, './audio/title.mpeg')
    words, times = text_to_speech(text, './audio/output.mpeg')

    images_folder = './images'
    create_title_img(title, images_folder)
    create_images(words, images_folder)

    compose_video('./videos/Gameplay15.mp4', './audio/output.mpeg', './audio/title.mpeg', images_folder, times, './output')
