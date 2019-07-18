#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : GetLive02.py
@Author: Xinzhe.Pang
@Date  : 2019/7/18 22:52
@Desc  : 
"""
import requests
from pymongo import MongoClient
import json

client = MongoClient('111.230.95.186', 27017)
db = client.zhihu_database
collection = db.live


def scrapy(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    r = requests.get(link, headers=headers)
    return (r.text)


link = "https://api.zhihu.com/lives/homefeed?includes=live"
is_end = False
while not is_end:
    html = scrapy(link)
    decodejson = json.loads(html)
    collection.insert_one(decodejson)

    link = decodejson['paging']['next']
    is_end = decodejson['paging']['is_end']
