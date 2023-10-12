# This recursively pulls the comments from the comment tree into lists that contain their information in the form of a dictionary followed by a list of replies
# It needs the inputs of depth (the current depth), comment (The current comment tree), and maxDepth (The max depth it will go before returning)
# It then returns that structure recursively, until the final result is a structure near identical to output.json
from praw.models import MoreComments


def recursiveCommentDownloader(depth, comment, maxDepth):
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
        myComments[1].append(recursiveCommentDownloader(depth + 1, post, maxDepth))
    # print("returning list of comment")
    # print(myComments)
    # If there were no subcomments, return myself
    
    return myComments