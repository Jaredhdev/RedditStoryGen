from text import create_images
from overlay import compose_video
from reddit import get_submission
from tts import text_to_speech


if __name__ == '__main__':
    url = 'https://www.reddit.com/r/TrueOffMyChest/comments/14n3u4r/i_was_kidnapped_by_my_childhood_best_friend_and/'

    submission = get_submission(url)

    words, times = text_to_speech(submission.selftext, './audio/output.mp3')

    create_images(words, './images')

    compose_video('./videos/Minecraft1.mp4', './audio/output.mp3', './images', times, './output')

