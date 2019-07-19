#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : GetBeijingPark.py
@Author: Xinzhe.Pang
@Date  : 2019/7/18 23:49
@Desc  : 
"""
import requests
import json


def getjson(link, loc, page_num=0):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    pa = {'query': '公园',
          'region': loc,
          'scope': '2',
          'page_size': 20,
          'page_num': page_num,
          'output': 'json',
          'ak': 's1zg5ulBihNVisCAVt6Si1X66yNOWdSA'
          }
    r = requests.get(link, params=pa, headers=headers)
    decodejson = json.loads(r.text)
    return decodejson


link = "http://api.map.baidu.com/place/v2/search"
loc = '北京'
print(getjson(link, loc))
