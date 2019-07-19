#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : GetCityPark_MysqlSave.py
@Author: Xinzhe.Pang
@Date  : 2019/7/19 21:07
@Desc  : 
"""
import requests
import json
import MySQLdb

city_list = list()
with open('cities.txt', 'r', encoding='UTF-8') as txt_file:
    for eachLine in txt_file:
        if eachLine != "" and eachLine != "\n":
            fileds = eachLine.split("\t")
            city = fileds[0]
            city_list.append(city)
    txt_file.close()

conn = MySQLdb.connect(host='111.230.95.186', user='scraping', passwd='scrape0707', db='scraping', charset='utf8')
cur = conn.cursor()
link = "http://api.map.baidu.com/place/v2/search"


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


for eachCity in city_list:
    not_last_page = True
    page_num = 0
    while not_last_page:
        decodejson = getjson(link, eachCity, page_num)
        print(eachCity, page_num)
        if decodejson['results']:
            for eachone in decodejson['results']:
                try:
                    park = eachone['name']
                except:
                    park = None
                try:
                    location_lat = eachone['location']['lat']
                except:
                    location_lat = None
                try:
                    location_lng = eachone['location']['lng']
                except:
                    location_lng = None
                try:
                    address = eachone['address']
                except:
                    address = None
                try:
                    street_id = eachone['street_id']
                except:
                    street_id = None
                try:
                    uid = eachone['uid']
                except:
                    uid = None
                sql = """INSERT INTO scraping.city(city,park,location_lat,location_lng,address,street_id,uid) VALUES(%s,%s,%s,%s,%s,%s,%s);"""
                cur.execute(sql, (eachCity, park, location_lat, location_lng, address, street_id, uid,))
                conn.commit()
            page_num += 1
        else:
            not_last_page = False
cur.close()
conn.close()
