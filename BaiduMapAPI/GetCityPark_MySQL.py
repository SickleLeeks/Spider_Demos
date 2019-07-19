#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : GetCityPark_MySQL.py
@Author: Xinzhe.Pang
@Date  : 2019/7/19 20:07
@Desc  : 
"""
import MySQLdb

conn = MySQLdb.connect(host='111.230.95.186', user='scraping', passwd='scrape0707', db='scraping', charset='utf8')
cur = conn.cursor()

sql = """CREATE TABLE city(
id INT NOT NULL AUTO_INCREMENT,
city VARCHAR(200) NOT NULL,
park VARCHAR(200) NOT NULL,
location_lat FLOAT,
location_lng FLOAT,
address VARCHAR(200),
street_id VARCHAR(200),
uid VARCHAR(200),
created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(id)
);"""
cur.execute(sql)
conn.commit()
conn.close()
