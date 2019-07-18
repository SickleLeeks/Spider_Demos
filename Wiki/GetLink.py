#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : GetLink.py
@Author: Xinzhe.Pang
@Date  : 2019/7/18 20:44
@Desc  : 
"""
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Wikipedia"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

r = requests.get(url, headers=headers)
html = r.text
bsObj = BeautifulSoup(html)

for link in bsObj.find_all("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
