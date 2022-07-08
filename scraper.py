# Imports
import sys
import os
import re
import pandas as pd 
import requests
import bs4 as bs

# Function declarations

# Removes html tags from parsed strings
def strip_tags(html):
    stripped_text = bs(html, "lxml").text
    # Regular expression to remove non-word characters as well as "words" that are unreasonably long
    longword = re.compile(r'\W*\b\w{20,999}\b')
    stripped_text2 = longword.sub('', stripped_text)
    return stripped_text2.replace('\n', ' ').replace("\'", "")


# Fetches HTML string from URL, returns it
def string_from_url(url):
    f = requests.get(url)
    return strip_tags(f.text)


if __name__ == '__main__':
    print("hi") 
    