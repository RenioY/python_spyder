# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
这是mfw景点地址
"""

import requests		
import re	
import mfw_url_list
import os

def mfw_url_jd(*args):
    #print(url_list1[0])
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    path = './' 
	os.mkdir(path + './景点简介')	
    for url_list1 in url_list:
        url_r=requests.get("{}".format(url_list1),headers=headers)
        url_r.encoding = 'utf-8' 
        url_r_single = re.findall("<li><a href=\"/jd(.*?)\".target=\"_blank\">(.*?)</a></li>",url_r.text.strip('\n'),re.S)
        #print(url_r_single)
        try:  
            url_area = "https://www.mafengwo.cn/jd" + url_r_single[0][0]
        except IndexError:
            log = open("log.txt","w+",encoding='utf-8')
            log_error = "\n"+ url_list1
            log.write("url列表溢出")
            log.write(log_error)
            log.close()
        else:
            #print(url_area)
            url_areal=requests.get("{}".format(url_area),headers=headers)
            url_area_file = re.findall("<p.style=\"display:.none;\">(.*?)</span>",url_areal.text.strip("\n"),re.S)
            #print(type(url_area_file))
            part = re.compile('<[^>]+>',re.I)		#去除所有html文本标签
            part1 = re.compile("&ensp;",re.I)		#去除空行
            part2 = re.compile("&nbsp;",re.I)
            try:
                sentences = part2.sub('',(part1.sub('',(part.sub('',url_area_file[0])))))
            except IndexError:
                log = open("log.txt","w+",encoding='utf-8')
                log_error = "\n"+ url_area
                log.write(url_r_single[0][1])
                log.write(log_error)
                log.close()
            else:
#                print(sentences)
                print(url_r_single[0][1])
                file=open("./景点简介/{}.txt".format(url_r_single[0][1]),"w+",encoding='utf-8')	
                file.write(sentences)			
                file.close()

url = "https://www.mafengwo.cn/mdd/"   #mfw的url主页
url_list = mfw_url(url)
mfw_url_jd(url_list)
