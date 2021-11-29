#!/usr/bin/env python
#Author: sYc
#Date: 2021-02-06 17:09:27
#Version: 0.1
#Description: net-spider downloader

import requests
from bs4 import BeautifulSoup

url = "http://c.biancheng.net/view/2011.html"
str_html = requests.get(url)
soup = BeautifulSoup(str_html.text, "lxml")
data = soup.select("#arc-body > div > img")

print(data)
