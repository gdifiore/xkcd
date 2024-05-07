#
# xkcd_api.py - xkcd
#
# (c) 2018-2024 gdifiore <difioregabe@gmail.com>
#

import json
import urllib.request
import urllib.error

def get_comic_info(num):
    """
    Fetches the information for a specific XKCD comic.

    Args:
        num (int): The number of the XKCD comic.

    Returns:
        dict: A dictionary containing the comic information, or None if an error occurred.
    """
    url = f"https://xkcd.com/{num}/info.0.json"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
    except (urllib.error.URLError, json.JSONDecodeError) as e:
        print(f"Error fetching comic info for {num}: {e}")
        return None
    return data

def get_latest_comic_info():
    """
    Fetches the information for the latest XKCD comic.

    Returns:
        dict: A dictionary containing the latest comic information, or None if an error occurred.
    """
    url = "https://xkcd.com/info.0.json"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
    except (urllib.error.URLError, json.JSONDecodeError) as e:
        print(f"Error fetching latest comic info: {e}")
        return None
    return data