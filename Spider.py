# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
import os
import io

if __name__ == '__main__':
    req = requests.get("https://wall.alphacoders.com/search.php?search=your+name")
    print (req)
    #校正网页的编码格式，否则会出现乱码现象
    req.encoding = req.apparent_encoding
    #开始解析网页
    #lxml HTML 解析器
    soup = BeautifulSoup(req.text, 'lxml')
    # print (soup)

    # find()：第一个参数放置标签，第二个参数放标签属性（class 数据比较特殊需要加一个下划线）
    div = soup.find("div", class_="thumb-container-big")
    # get()：参数为标签里的属性，用于获取标签中某个属性的属性值
    img_src = div.find('img').get("data-src")
    print ("img url : %s" %(img_src))

    # 下载图片
    req = requests.get(img_src)
    with open('1.jpg', 'wb') as f:
        f.write(req.content)

