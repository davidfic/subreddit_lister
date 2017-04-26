import praw
import click
from config import client_id, client_secret, user_agent,user_info 


@click.command()
@click.option('--user', help='the user to pull subreddits from')
def make_list(user):
    if user in user_info: 
        u = user_info[user]
        reddit = praw.Reddit(client_id=u['client_id'], client_secret=u['client_secret'], user_agent=user_agent,username=user, password=u['password'])
    subscribed = list(reddit.user.subreddits(limit=None))

    for sub in subscribed:
        print(sub)


if __name__ == '__main__':
    make_list()
