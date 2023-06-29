from text import create_images
from overlay import compose_video
from reddit import get_submission


if __name__ == '__main__':
    url = 'https://www.reddit.com/r/Guitar/comments/14lospk/discussion_which_guitarist_will_forever_give_you/'

    submission = get_submission(url)

    create_images(submission.selftext.split(), './images')

    times = [0] * 21
    compose_video('./videos/Minecraft1.mp4', './images', times, './output/test.mp4')
