# Subreddit lister

If you have the issue where you have multiple Reddit user accounts and you 
would like to make sure that you keep your subreddit subscriptions consistant 
between your accounts.


## Prerequisites

For this to work you will need to create a personal app in each of your reddit
accounts.

Go to the [apps page}(https://www.reddit.com/prefs/apps/)
Click the `Create another App` button
Give the app an name, description and put `http://localhost` in the 
redirect URL box. 


This will show you your client_id info and your client secret. 


Copy these down and enter them into the config.py script. Do this for
each user you currently have with Reddit. 


## Usage:

    python list_subreddits.py --user=USERNAME
