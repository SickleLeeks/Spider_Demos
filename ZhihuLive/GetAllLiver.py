#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : GetAllLiver.py
@Author: Xinzhe.Pang
@Date  : 2019/7/18 23:05
@Desc  : 
"""
from pymongo import MongoClient
import requests
import json
import random
import time

client = MongoClient('111.230.95.186', 27017)
db = client.zhihu_database


def get_audience(live_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    link = "https://api.zhihu.com/lives/" + live_id + '/members?limit=10&offset=0'

    is_end = False
    while not is_end:
        r = requests.get(link, headers=headers)
        html = r.text
        decodejson = json.loads(html)
        decodejson['live_id'] = live_id
        db.live_audience.insert_one(decodejson)

        link = decodejson['paging']['next']
        is_end = decodejson['paging']['is_end']
        time.sleep(random.randint(2, 3) + random.random())


for each_page in db.live.find():
    for each in each_page['data']:
        live_id = each['live']['id']
        print(live_id)
        get_audience(live_id)
