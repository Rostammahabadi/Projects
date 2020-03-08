from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import pandas as pd
import numpy as np

url= "https://www.elephantjournal.com/"
response = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
web_page = urlopen(response).read()
page_soup = BeautifulSoup(web_page, "html.parser")

href = []
for hrefs in page_soup.find_all('a'):
    #print(re.search("\bhttps.*\b",str(link)))
    values = hrefs.get('href')
    href.append(values)

links = []
for link in test:
    if re.match('https://www.elephantjournal.com/20.*',str(link)) is not None:
        links.append(link)

for open_link in links:
    url_array = f"{open_link}"
    response = Request(url_array, headers = {'User-Agent': 'Mozilla/5.0'})
    web_page = urlopen(response).read()
    page_soup = BeautifulSoup(web_page, "html.parser")

author_name=[]
title=[]
for open_link in links[0:4]:
    url_array = open_link
    response = Request(url_array, headers = {'User-Agent': 'Mozilla/5.0'})
    web_page = urlopen(response).read()
    page_soup = BeautifulSoup(web_page, "html.parser")
    for authors in page_soup.find_all(class_ = "meta-author"):
        for author in authors.find_all(class_= "meta-author"):
            author_name.append(author.text)
    for titles in page_soup.find_all("h1"):
        title.append(titles.text)
