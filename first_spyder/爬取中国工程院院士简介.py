# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 23:11:50 2019

@author: Administrator
"""

import requests		#web请求库
import re		#正则表达式库
import os
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}		#伪造浏览器访问
path = './' 
os.mkdir(path + './工程院院士简介')
r1=requests.get("http://www.cae.cn/cae/html/main/col48/column_48_1.html",headers=headers)	#院士名单网页
r1.encoding = 'utf-8'
lianjie = re.findall("<li class=\"name_list\"><a href=\"(.*?)\"\starget=\"_blank\">(.*?)</a></li>",r1.text.strip('\n'),re.S)	#提取所有院士简介网页
#print(lianjie)
for lian in lianjie:	#遍历每个网页
    lian1 = "http://www.cae.cn" + lian[0]
    name = lian[1]
    print(name)
    r=requests.get('{}'.format(lian1),headers=headers)	#添加头文件表示身份
    r.encoding = 'utf-8'
    shi =re.search("<div.class=\"intro\">\s*<p>(.*?)</p>\s*</div>",r.text,re.S)	#找到爬取的文本位置						         
#    print(shi.group(1))
    part = re.compile('<[^>]+>',re.I)		#去除所有html文本标签
    part1 = re.compile("&ensp;",re.I)		#去除空行
    part2 = re.compile("&nbsp;",re.I)
    try:
        sentences = part2.sub('',(part1.sub('',(part.sub('',shi.group(1))))))
    except AttributeError:
        log = open("./工程院院士简介/log.txt","w+",encoding='utf-8')
        log_error = "\n"+lian1
        log.write(name)
        log.write(log_error)
        log.close()
    else:
#       print(sentences)
        file=open("./工程院院士简介/{}.txt".format(name),"w+",encoding='utf-8')	#创建并打开文件
        shiji = "\n"+sentences
        file.write(name)		#第一行院士名字
        file.write(shiji)			#第二行开始为院士简介
        file.close()
