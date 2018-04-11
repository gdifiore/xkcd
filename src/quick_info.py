#
# quick_info.py - xkcd
#
# (c) 2018 gdifiore <difioregabe@gmail.com>
#

import urllib.request
import json

url = "https://xkcd.com/info.0.json" # url is link to json of latest xkcd
response = urllib.request.urlopen(url) # open url with urllib.request
data = json.loads(response.read()) # load and parse json

title = data['title'] # grab title from parsed json
alt = data['alt'] # grab alt text from parsed json

print(title + ": " + alt) # grab title + alt data from parsed json
