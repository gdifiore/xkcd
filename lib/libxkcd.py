#
# libxkcd.py - xkcd
#
# (c)2018 gdifiore <difioregabe@gmail.com> 
#

import urllib.request
import json

def name(num):
    url = "https://xkcd.com/info.0.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    latest = data['num']

    if (int(num) > latest):
        print("xkcd number larger than latest xkcd")
        exit()
    else:
        url = "https://xkcd.com/" + num + "/info.0.json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        title = data['title']

        return title

def dl(num, filename):
    url = "https://xkcd.com/info.0.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    latest = data['num']
    if (int(num) > latest):
        print("xkcd number larger than latest xkcd")
        exit()
    else:
        url = "https://xkcd.com/" + num + "/info.0.json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        num = data['num']
        img_url = data['img']

        img = filename + ".png"
        urllib.request.urlretrieve(img_url, img)

def latest_num():
    url = "https://xkcd.com/info.0.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    num = data['num']

    return str(num)

def latest_title():
    url = "https://xkcd.com/info.0.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    title = data['title']

    return title