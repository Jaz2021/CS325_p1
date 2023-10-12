# Running this file either requires an argument of a reddit link to a comment section.
# There is a default link, but this code will work with either old.reddit.com or www.reddit.com as long as it is comments

import praw
import regex
import argparse
import json
from module_1 import secretsPuller as s
from module_2 import getComments as g
from module_3 import recursiveCommentDownloader as rec


# print(argparser.parseArguments("test"))
maxDepth = 10





#Load the keys from a json file in the current directory called secrets.json



parser = argparse.ArgumentParser()
parser.add_argument("link", default="https://www.reddit.com/r/funny/comments/16brnzb/self_aware/", nargs="?")
#Added a default argument just to make debuggin easier
args = parser.parse_args()
link = args.link
reg = r'(reddit.com\/r\/)(.*?)/(comments)/(.*?)/.*'
code = str(regex.split(reg, link)[4])
keys = s.getSecrets()
# print(subreddit)
if code != None:
    print("Looking in id: " + subreddit)
    reddit = praw.Reddit(client_id=keys["client_id"],
                     client_secret=keys["secret_id"],
                     redirect_uri=keys["redirect_uri"],
                     user_agent=keys["user_agent"])
    reddit.read_only = True
    g.getComments(code, reddit, maxDepth)
    print("Complete, output in ./output/processed/output.json")
else:
    print("Error: could not find subreddit in link given")