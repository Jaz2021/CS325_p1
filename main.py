import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("link", default="old.reddit.com/r/funny/comments/16brnzb/self_aware", nargs="?")
args = parser.parse_args()
link = args.link
if (not (link.startswith("http://") or link.startswith("https://"))):
    link = "http://" + link
page = requests.get(link)
# This will almost always give me an error for too many requests in the output.txt

file = open("./output.txt", "w")

file.writelines(page.text)
file.close()
