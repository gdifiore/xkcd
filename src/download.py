#
# download.py - xkcd
#
# (c) 2018 gdifiore <difioregabe@gmail.com>
#

import urllib.request
import json

url = "https://xkcd.com/info.0.json" # url is link to json to latest xkcd
response = urllib.request.urlopen(url) # open url with urllib.request
data = json.loads(response.read()) # load and parse json

num = data['num'] # grab xkcd number from parsed json
img_url = data['img'] # grab img link form parsed json


print(img_url) # print url to image

urllib.request.urlretrieve (img_url, "xkcd_latest.png") # download & save latest xkcd as xkcd_latest with urllib.request
print()
print("Downloaded xkcd number", num)
