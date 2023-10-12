# This expects a secrets.json file in the parent directory and returns the keys from that json file.
# 



import json

def getSecrets():
    keys = json.load(open("./secrets.json"))
    return keys