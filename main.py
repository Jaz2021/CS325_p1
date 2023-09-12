import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("link", default="google.com", nargs="?")
args = parser.parse_args()
link = args.link
if (not (link.startswith("http://") or link.startswith("https://"))):
    link = "http://" + link
page = requests.get(link)

file = open("./output.html", "w")
file.writelines(page.text)
file.close()
