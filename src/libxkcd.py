#
# libxkcd.py - xkcd
#
# (c) 2018-2024 gdifiore <difioregabe@gmail.com>
#

import urllib.request
from .xkcd_api import get_comic_info, get_latest_comic_info

def get_title(num):
    """
    Returns the title of a specific XKCD comic.

    Args:
        num (int): The number of the XKCD comic.

    Returns:
        str: The title of the comic, or None if an error occurred.
    """
    latest_info = get_latest_comic_info()
    if latest_info is None:
        return None

    latest_num = latest_info['num']
    if int(num) > latest_num:
        print("xkcd number larger than latest xkcd")
        return None

    comic_info = get_comic_info(num)
    if comic_info is None:
        return None

    title = comic_info['title']
    return title

def get_alt_text(num):
    """
    Returns the alt text of a specific XKCD comic.

    Args:
        num (int): The number of the XKCD comic.

    Returns:
        str: The alt text of the comic, or None if an error occurred.
    """
    latest_info = get_latest_comic_info()
    if latest_info is None:
        return None

    latest_num = latest_info['num']
    if int(num) > latest_num:
        print("xkcd number larger than latest xkcd")
        return None

    comic_info = get_comic_info(num)
    if comic_info is None:
        return None

    alt_text = comic_info['alt']
    return alt_text

def download(num, filename):
    """
    Downloads the image for a specific XKCD comic.

    Args:
        num (int): The number of the XKCD comic.
        filename (str): The filename to save the image as (without extension).
    """
    latest_info = get_latest_comic_info()
    if latest_info is None:
        return

    latest_num = latest_info['num']
    if int(num) > latest_num:
        print("xkcd number larger than latest xkcd")
        return

    comic_info = get_comic_info(num)
    if comic_info is None:
        return

    img_url = comic_info['img']
    img_path = f"{filename}.png"
    try:
        urllib.request.urlretrieve(img_url, img_path)
    except urllib.error.URLError as e:
        print(f"Error downloading image for {num}: {e}")

def get_latest_num():
    """
    Returns the number of the latest XKCD comic.

    Returns:
        str: The number of the latest comic, or None if an error occurred.
    """
    latest_info = get_latest_comic_info()
    if latest_info is None:
        return None

    num = latest_info['num']
    return str(num)

def get_latest_title():
    """
    Returns the title of the latest XKCD comic.

    Returns:
        str: The title of the latest comic, or None if an error occurred.
    """
    latest_info = get_latest_comic_info()
    if latest_info is None:
        return None

    title = latest_info['title']
    return title

def get_raw_json(num):
    return get_comic_info(num)