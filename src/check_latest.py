#
# check_latest.py - xkcd
#
# (c) gdifiore 2018 <difioregabe@gmail.com>
#

import urllib.request
import json

url = "https://xkcd.com/info.0.json" # url is link to json to latest xkcd
response = urllib.request.urlopen(url) # open url with urllib.request
data = json.loads(response.read()) # load and parse json

num = data['num'] # grab xkcd number from parsed json
title = data['title'] # grab title from parsed json

print("Latest xkcd is number " + str(num) + ": " + title) # print number and title of latest xkcd