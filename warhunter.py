import praw

reddit = praw.Reddit('whbot')
subreddit = reddit.subreddit("csgo")

for submission in subreddit.hot(limit=7):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")




