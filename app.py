import praw
import pdb
import re
import os

# This allows me to use the same code for multiple subreddits
def subCheck(file, sub, numPosts):
    # Opens a file full of acronyms for talesfromtechsupport
    with open(file, "r") as f:
        temp = f.read()
        temp = temp.split("\n")
        temp = list(filter(None, temp))

    # Creates a list the acronyms from the file.
    abr = []
    # Splits each acronym and meaning into a 2D array
    for l in temp:
        abr.append(l.split("_"))


    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=numPosts):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            post = False
            reply = "Acronym|Meaning\n:--|:--\n"
            for item in abr:
                if re.search(item[0], submission.selftext, re.IGNORECASE):
                    # Store the current id into our list
                    post = True

                    reply += item[0] + "|" + item[1] + "\n"
            reply += "\n*This was an automated response.*  \n*Please PM me if there were any mistakes.*"

            # If an abreviation was found, then post a reply, and store post in replied to file
            if (post):
                posts_replied.append(submission.id)
                submission.reply(reply)
                print("Bot replying to : ", submission.title)

# Create the Reddit instance
reddit = praw.Reddit('bot')

# Creates file incase it doesn't exist
if not os.path.isfile("replied.txt"):
    posts_replied = []

else:
    # Creates an array of posts replied to
    with open("replied.txt", "r") as f:
        posts_replied = f.read()
        posts_replied = posts_replied_to.split("\n")
        posts_replied = list(filter(None, posts_replied_to))

subCheck("tfts.txt", "pythonforengineers", 5)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in replied:
        f.write(post_id + "\n")
