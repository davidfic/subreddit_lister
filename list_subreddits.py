import praw
import click
from config import user_agent,user_info 

user_dict = {}
sub_list = []
def get_subreddits(user):
    u = user_info[user]
    reddit = praw.Reddit(client_id=u['client_id'], client_secret=u['client_secret'], user_agent=user_agent,username=user, password=u['password'])
    sub_list = list(reddit.user.subreddits(limit=None))
    return sub_list 


@click.command()
@click.option('--user', help='the user to pull subreddits from', required=False)
@click.option('--user_list', help='a comma separated list of users to lookup', required=False)
def get_list(user,user_list=None):

    u_list = user_list.split(',')
    for user in u_list:
        user_dict[user] = get_subreddits(user)
                 

    for k,v in user_dict.iteritems():
        print("user is {}".format(k))
        print("subreddits are as follows")
        for value in v:
            print(value)

def compare_list(user_list):
    pass

if __name__ == '__main__':
    get_list()
