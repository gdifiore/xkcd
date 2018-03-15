#
# quick_info.py - xkcd
#
# (c) gdifiore 2018 <difioregabe@gmail.com>
#

import urllib.request
import json

url = "https://xkcd.com/info.0.json" # url is link to json to latest xkcd
response = urllib.request.urlopen(url)
data = json.loads(response.read()) # load and parse json

print(data['title'] + ": " ,data['alt']) # grab title + alt data form parsed json