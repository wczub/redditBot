import praw

reddit = praw.Reddit('bot')

subreddit = reddit.subreddit("AskReddit")

for submission in subreddit.new(limit=5):
    print("Title: ", submission.title)
    print("Score: ", submission.score)
    print("----------------------------------\n")
