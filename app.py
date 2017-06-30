import praw
import pdb
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot')


# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
        
with open("tfts.txt", "r") as f:
    temp = f.read()
    temp = temp.split("\n")
    temp = list(filter(None, temp))
print temp
tfts = []
for l in temp:
    tfts.append(l.split("_"))
print tfts
# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=2):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:
        
        post = False
        reply = "Acronym|Meaning\n:--|:--\n"
        for abr in tfts:
            if re.search(abr[0], submission.selftext, re.IGNORECASE):
                # Store the current id into our list
                post = True
                
                reply += abr[0] + "|" + abr[1] + "\n"
        reply += "\n*This was an automated response.*  \n*Please PM me if there were any mistakes.*"
                
        # If an abreviation was found, then post a reply, and store post in replied to file
        if (post):
            posts_replied_to.append(submission.id)
            submission.reply(reply)
            print("Bot replying to : ", submission.title)

        

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")