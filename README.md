# xkcd 
 xkcd - tools for xkcd comics

## Requirements 
- Python 3

## Scripts Included
    src/quick_info.py
Grab's title and alt for specified xkcd comic.

    src/download.py
Download specified xkcd as `xkcd_[number].png` into current directory.

    src/check_latest.py
Check the number and title of the latest xkcd.

## libxkcd

    lib/libxkcd.py
Functions to perform functions with the xkcd JSON api

### Examples

    title = name("233")
Set `title` to the name of the 233rd xkcd

    dl("233", "capcha")
Download the 233rd xkcd as `capcha.png` (.png is added in the function)

    num =  latest_num()
Set `num` to the number of the latest xkcd
    
    title =  latest_title()
Set `title` to the title of the latest xkcd

## Credits
The [xkcd](https://xkcd.com/) comic is created by the talented [Randall Munroe](https://twitter.com/xkcd) (or his more interesting [Wikipedia page](https://en.wikipedia.org/wiki/Randall_Munroe)). 

I only made the scripts.
