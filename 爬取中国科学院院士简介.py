# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:42:19 2019

@author: Renio
"""
import requests		#web请求库
import re		#正则表达式库
import os
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}		#伪造浏览器访问
path = './' 
os.mkdir(path + './科学院院士简介')
r1=requests.get("http://casad.cas.cn/ysxx2017/ysmdyjj/qtysmd_124280/",headers=headers)	#院士名单网页
r1.encoding = 'utf-8'
lianjie = re.findall("<span>.*?<a href=\"(.*?)\"\s",r1.text.strip('\n'),re.S)	#提取所有院士简介网页
#print(lianjie)
for lian in lianjie:	#遍历每个网页
    r=requests.get('{}'.format(lian),headers=headers)	#添加头文件表示身份
    r.encoding = 'utf-8'
    name = re.search('<h1>(.*?)</h1>',r.text,re.S)	#选其院士名字
    print(name.group(1))
    shi =re.search("<div><p align=\"justify\">(.*?)</div></div>",r.text,re.S)	#找到爬取的文本位置
#    print(shi.group(1))
    part = re.compile('<[^>]+>',re.I)		#去除所有html文本标签
    part1 = re.compile("&nbsp;",re.I)		#去除空行
#    t1 = part1.sub('',shi.group(1))
#    t2 = part.sub('',t1)
#    print(t2)
    sentences = part1.sub('',(part.sub('',shi.group(1))))
#    print(sentences)
    file=open("./科学院院士简介/{}.txt".format(name.group(1)),"w+",encoding='utf-8')	#创建并打开文件
    shiji = "\n"+sentences
    file.write(name.group(1))		#第一行院士名字
    file.write(shiji)			#第二行开始为院士简介
    file.close()
