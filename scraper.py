# Imports
import sys
import os
import re
import pandas as pd 
import requests
import bs4 as bs
from bs4.element import Comment
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Webdriver options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--lang=en-EN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1280,800")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("disable-infobars")

# Function declarations

# Scrapes links from google search
def scrape_links(tab_url):
    links = []
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    ## driver.get("http://www.google.com/search?hl=en-US&q=" + query +"&num=10") <- works for opening a separate window to scrape for a specific term
    driver.get(tab_url)
    soup = bs(driver.page_source, 'html.parser')
    search = soup.findAll('div', class_="yuRUbf")
    for n in search:
        links.append(n.a.get('href'))
    driver.quit()
    return links

# Removes html tags from parsed strings
def strip_tags(html):
    stripped_text = bs(html, "lxml").text
    # Regular expression to remove non-word characters as well as "words" that are unreasonably long
    longword = re.compile(r'\W*\b\w{20,999}\b')
    stripped_text2 = longword.sub('', stripped_text)
    return stripped_text2.replace('\n', ' ').replace("\'", "")

# Ignores HTML tags that are generally not visible on a site

def tag_visible(element):
    if element.parent.name in [
            'style', 'script', 'head', 'title', 'meta', '[document]'  #footer?
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True

# Fetches HTML string from URL, returns it
def url_to_string(url):
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    try:
        driver.get(url)
    except Exception as e:
        print("driver exception")
        driver.quit()
        error_tuple = ("", "")
        return error_tuple
        
    try: 
        soup = bs(driver.page_source, 'html.parser')
        soup2 = bs(driver.page_source, 'html.parser')
    except Exception as e:
        print("soup exception")
        driver.quit()
        error_tuple = ("", "")
        return error_tuple
    
    texts_nofilter = soup2.findAll(text=True)
    visible_texts_nofilter = filter(tag_visible, texts_nofilter)
    plaintext_nofilter = u" ".join(t.strip() for t in visible_texts_nofilter)
    plaintext_nofilter = ' '.join(plaintext_nofilter.split())
    
    # Remove div classes and IDs that contain irrelevant information
    for each in ['header', 'footer', 'head']:
        s = soup.find(each)
        if s == None:
            continue
        else:
            s.decompose()

    texts = soup.findAll(text=True)
    
    visible_texts = filter(tag_visible, texts)
    
    # remove non-visible text such as html tags and formatting
    plaintext = u" ".join(t.strip() for t in visible_texts)
    
    # remove duplicate whitespaces
    plaintext = ' '.join(plaintext.split())
    
    driver.quit()
    text_tuple = (plaintext, plaintext_nofilter)
    
    if plaintext == plaintext_nofilter:
        print("nått är fel!")
    else:
        print("de skiljer sig")
        
    return text_tuple

if __name__ == '__main__':
    print("hi") 
    