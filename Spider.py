# -*- coding: utf-8 -*-

import requests,time
from bs4 import BeautifulSoup
import sys
import os
import io
"""
    简单爬虫程序的编写分为四个步骤：

    第一步：发送请求
        请求的发送借助 Requests 库,安装：
            pip install requests
        导入：
            import requests
        发送请求：
            req = requests.get(url, timeout=10)
        获取请求码：
            req.status_code

    第二步：解析网页
        用 Beautiful Soup 库对其进行解析
        在对网页进行解析前我们需要校正网页的编码格式，否则会出现乱码现象：
            req.encoding = req.apparent_encoding
        开始解析网页：
            soup = BeautifulSoup(req.text, 'lxml')
            lxml 为解析器，除此解析器还有Python 标准库，lxml HTML 解析器， lxml XML 解析器， html5lib
        此步输出的结果就是将目标网站的源码解析成BeautifulSoup类，便于后续查找标签等操作

    第三步：定位标签
    以https://wall.alphacoders.com/search.php?search=your+name为例，定位网页中要爬取的图片：
    方法，将鼠标放到图面上后右键——> 检查，可以看到 img 标签中 src 后面的就是这张图片的存放地址（URL）
        1.定位到 class="thumb-container-big" 的 div 标签；（见代码）
        2.在 1 的基础上定位存放图片地址的 img 标签。（见代码）

    第四步：保存数据
"""


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
    time.sleep(2)

