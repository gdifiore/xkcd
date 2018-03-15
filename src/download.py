#
# download.py - xkcd
#
# (c) gdifiore 2018 <difioregabe@gmail.com>
#

import urllib.request
import json

url = "https://xkcd.com/info.0.json" # url is link to json to latest xkcd
response = urllib.request.urlopen(url)
data = json.loads(response.read()) # load and parse json

num = data['num']
img_url = data['img'] # grab img link form parsed json


print(img_url)

urllib.request.urlretrieve (img_url, "xkcd_latest.png")
print()
print("Downloaded xkcd number", num)