#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : CreateCityParkInfo.py
@Author: Xinzhe.Pang
@Date  : 2019/7/19 21:30
@Desc  : 
"""
import MySQLdb

conn = MySQLdb.connect(host='111.230.95.186', user='scraping', passwd='scrape0707', db='scraping', charset='utf8')
cur = conn.cursor()

sql = """CREATE TABLE park (
         id INT NOT NULL AUTO_INCREMENT,
         park VARCHAR(200) NOT NULL,
         location_lat FLOAT,
         location_lng FLOAT,
         address VARCHAR(200),
         street_id VARCHAR(200),
         telephone VARCHAR(200),
         detail INT,
         uid VARCHAR(200),
         tag VARCHAR(200),
         type VARCHAR(200),
         detail_url VARCHAR(800),
         price INT,
         overall_rating FLOAT,
         image_num INT,
         comment_num INT,
         shop_hours VARCHAR(800),
         alias VARCHAR(800),
         keyword VARCHAR(800),
         scope_type VARCHAR(200),
         scope_grade VARCHAR(200),
         description VARCHAR(9000),
         created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         PRIMARY KEY (id)
         );"""
cur.execute(sql)
conn.commit()
conn.close()
