import praw
import logging
from comment import Comment

submissions = []

#Initialize Logging
logging.basicConfig(filename='rpi.log', encoding='utf-8', level=logging.DEBUG)
for logger_name in ("praw", "prawcore"):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG)

#Create connection to Reddit
reddit = praw.Reddit(
    client_id="your id",
    client_secret="your secret",
    user_agent="your user agent"
)

# get Instance of a subreddit
#TODO create config file of multiple subreddits and get instances of them 
subreddit = reddit.subreddit("wallstreetbets")

#TODO for Testing, needs to be removed
# print(subreddit.display_name)  # output: redditdev
# print(subreddit.title)         # output: reddit development
# print(subreddit.description)   # output: a subreddit for discussion of ...

def getEntries():
    return submissions

def getSubmissions(l=None,c='new'):
    # assume you have a Subreddit instance bound to variable `subreddit`
    call = 'subreddit.' + c +'(limit=' + str(l) + ')'
    for submission in eval(call):
        #TODO for Testing, needs to be removed
        # print('-----' + submission.title + '----- [' + submission.id + ']')  # Output: the submission's title
        # print('(' + submission.url + ')')
        # print('Score: ' + str(submission.score))
        # print('+'*45)
        # print(submission.selftext)
        # print('+'*45)
        # print("")
        submissions.append(Comment(submission.title,submission.id,submission.url,submission.selftext,int(submission.score),submission.author))
        

