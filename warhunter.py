import praw

reddit = praw.Reddit('whbot')
subreddit = r.subreddit("csgo")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")




