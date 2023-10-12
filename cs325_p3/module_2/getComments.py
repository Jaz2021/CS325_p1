# This module has the inputs of code (The character/number code that specifies the post ex: 16brnzb)
# reddit (The reddit api from praw so that it does not have to be created with every file)
# and maxDepth (The max recursive depth to search for comments)
# It outputs a file into output/processed/output.json that contains all of the comments it found in a format where every comment is a list
# of itself followed by all of the replies to the comment

#
import sys
from praw.models import MoreComments
import json
sys.path.append("../module_3")
from module_3 import recursiveCommentDownloader as r
def getComments(code, reddit, maxDepth):
    sub = reddit.submission(str(link))

    
    # print(link)
    postData = []
    for post in sub.comments:
        if isinstance(post, MoreComments):
            continue
        postData.append(r.recursiveCommentDownloader(0, post, maxDepth))
    
    # print(sub.comments)
    # try:

    # except:
    #     raise Exception("Could not find thread")
    jsonPosts = json.dumps(postData, indent=4)
    file = open("./output/processed/output.json", "w")
    file.writelines(jsonPosts)
    file.close()