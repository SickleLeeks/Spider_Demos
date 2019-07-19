#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : GetCityPark.py
@Author: Xinzhe.Pang
@Date  : 2019/7/19 0:07
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
province_list = ['江苏省', '浙江省', '广东省', '福建省', '山东省', '河南省', '河北省', '四川省', '辽宁省', '云南省',
                 '湖南省', '湖北省', '江西省', '安徽省', '山西省', '广西壮族自治区', '陕西省', '黑龙江省', '内蒙古自治区',
                 '贵州省', '吉林省', '甘肃省', '新疆维吾尔自治区', '海南省', '宁夏回族自治区', '青海省', '西藏自治区']

for eachprovince in province_list:
    decodejson = getjson(link, eachprovince)
    try:
        for eachcity in decodejson['results']:
            city = eachcity['name']
            num = eachcity['num']
            print(city, num)
            output = '\t'.join([city, str(num)]) + '\r\n'
            with open('cities.txt', "a+", encoding='utf-8') as f:
                f.write(output)
                f.close()
    except Exception as e:
        print(e)
