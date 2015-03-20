
import praw
__author__ = 'httpnick'
useragent = 'httpnick_dev'
r = praw.Reddit(user_agent=useragent)
r.login()
submission = r.get_submission(submission_id='11v36o')
print(submission.has_fetched)
flat_comments = praw.helpers.flatten_tree(submission.comments)
already_done = set()
for comment in flat_comments:
    if not hasattr(comment, 'body') and comment.id not in already_done:
        continue
    print(comment.body)
    already_done.add(comment.id)




