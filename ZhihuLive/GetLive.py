#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : GetLive.py
@Author: Xinzhe.Pang
@Date  : 2019/7/18 22:32
@Desc  : 
"""
import requests
import json


def scrapy(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    r = requests.get(link, headers=headers)
    return (r.text)


link = "https://api.zhihu.com/lives/homefeed?includes=live"
html = scrapy(link)
print(html)

decodejson = json.loads(html)
next_page = decodejson['paging']['next']
is_end = decodejson['paging']['is_end']
print(next_page)
print(is_end)
