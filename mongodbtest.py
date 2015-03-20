import praw
import pymongo
from pymongo import MongoClient

client = MongoClient()

db = client.test_reddit_database
users = db.user_test

useragent = 'httpnick_dev'
r = praw.Reddit(user_agent=useragent)
user = r.get_redditor('httpNick')
comments = []
for comment in user.get_comments(limit=None):
    comments.append(comment.body)
post = {'username': user.name, 'comments': comments}
users.insert_one(post)