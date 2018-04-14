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

latest = data['num'] # grab xkcd number from parsed json
num_dl = input("Which xkcd would you like do download? Latest is " + str(latest) + ": ") # user input for picking what xkcd to download

url = "https://xkcd.com/" + num_dl + "/info.0.json" # url is link to json to latest xkcd
response = urllib.request.urlopen(url) # open url with urllib.request
data = json.loads(response.read()) # load and parse json

num = data['num'] # grab xkcd number from parsed json
img_url = data['img'] # grab img link from parsed json

print(img_url) # print url to image

new_url = "xkcd_" + str(num) + ".png" # set new download url to include custom number
urllib.request.urlretrieve(img_url, new_url) # download & save latest xkcd as xkcd_[number] with urllib.request
print("Downloaded xkcd number", num) # print download confirmation