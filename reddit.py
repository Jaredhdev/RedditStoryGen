import praw
from praw import Reddit

client_id = "8Rm6I3YxkOyM4NHYRrl4_Q"
client_secret = "n2Q1SkyssQRy4H5F4JF1GlHp7B1BoA"
user_agent = "RedditStoryGen"


def get_submission(url: str) -> Reddit.submission:
    reddit: Reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    return reddit.submission(url=url)
