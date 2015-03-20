__author__ = 'httpnick'
import praw
from pprint import pprint
r = praw.Reddit('Submission variables testing by /u/_Daimon_')
submission = r.get_submission(submission_id = "105aru")
pprint(submission.short_link)