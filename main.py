import praw
import regex
from praw.models import MoreComments
import argparse
import json
global maxDepth
maxDepth = 10

def getComments(link):
    global reddit
    sub = reddit.submission(str(link))

    
    # print(link)
    postData = []
    for post in sub.comments:
        if isinstance(post, MoreComments):
            continue
        postData.append(recursiveCommentDownloader(0, post))
    
    # print(sub.comments)
    # try:

    # except:
    #     raise Exception("Could not find thread")
    jsonPosts = json.dumps(postData, indent=4)
    file = open("./output.json", "w")
    file.writelines(jsonPosts)
    file.close()

def recursiveCommentDownloader(depth, comment):
    global maxDepth
    if(depth > maxDepth):
        return {
                'Body': comment.body,
                'Score': comment.score, #The upvotes minus downvotes
                'Author': str(comment.author), #The post author
                'ID': comment.id #The post ID, whether this is needed will be to be determined
            }
    myComments = [{
            'Body': comment.body,
            'Score': comment.score, #The upvotes minus downvotes
            'Author': str(comment.author), #The post author
            'ID': comment.id #The post ID, whether this is needed will be to be determined
        },[]]
    for post in comment.replies: 
        if isinstance(post, MoreComments):
            continue
        myComments[1].append(recursiveCommentDownloader(depth + 1, post))
    # print("returning list of comment")
    # print(myComments)
    # If there were no subcomments, return myself
    
    return myComments

#Load the keys from a json file in the current directory called secrets.json
keys = json.load(open("./secrets.json"))


parser = argparse.ArgumentParser()
parser.add_argument("link", default="https://www.reddit.com/r/funny/comments/16brnzb/self_aware/", nargs="?")
#Added a default argument just to make debuggin easier
args = parser.parse_args()
link = args.link
reg = r'(reddit.com\/r\/)(.*?)/(comments)/(.*?)/.*'
subreddit = regex.split(reg, link)[4]

# print(subreddit)
if subreddit != None:
    print("Looking in id: " + subreddit)
    global reddit
    reddit = praw.Reddit(client_id=keys["client_id"],
                     client_secret=keys["secret_id"],
                     redirect_uri=keys["redirect_uri"],
                     user_agent=keys["user_agent"])
    reddit.read_only = True
    getComments(subreddit)
    print("Complete, output in ./output.json")
else:
    print("Error: could not find subreddit in link given")