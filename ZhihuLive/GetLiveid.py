#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : GetLiveid.py
@Author: Xinzhe.Pang
@Date  : 2019/7/18 22:59
@Desc  : 
"""
from pymongo import MongoClient

client = MongoClient('111.230.95.186', 27017)
db = client.zhihu_database
collection = db.live

first_page = collection.find_one()
for each in first_page['data']:
    print(each['live']['id'])
