import praw
__author__ = 'httpnick'
useragent = 'httpnick_dev'
r = praw.Reddit(user_agent=useragent)
r.login()
user = r.get_redditor('put_name_here')
for comment in user.get_comments(limit=None):
    print comment.body