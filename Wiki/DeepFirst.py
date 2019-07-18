#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : DeepFirst.py
@Author: Xinzhe.Pang
@Date  : 2019/7/18 21:13
@Desc  : 
"""
import requests
import re

exist_url = []  # 存放已爬取的网页
g_writecount = 0


def scrappy(url, depth=1):
    global g_writecount
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        url = "https://en.wikipedia.org/wiki/" + url
        r = requests.get(url, headers=headers)
        html = r.text
    except Exception as e:
        print('Failed downloading and saving', url)
        print(e)
        exist_url.append(url)
        return None

    exist_url.append(url)
    link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>', html)
    # 去掉已爬链接和重复链接
    unique_list = list(set(link_list) - set(exist_url))

    # 把所有链接写出到txt文件
    for eachone in unique_list:
        g_writecount += 1
        output = "No." + str(g_writecount) + "\t Depth:" + str(depth) + "\t" + url + ' -> ' + eachone + '\n'
        print(output)
        with open('link_12-3.txt', "a+") as f:
            f.write(output)

        # 只获取两层，"Wikipedia"算第一层
        if depth < 2:
            # 递归调用自己来访问下一层
            scrappy(eachone, depth + 1)

scrappy("Wikipedia")
