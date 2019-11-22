# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:36:00 2019

@author: Renio
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests		
import re	
	
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}		

def mfw_url(url_index):
    url_r=requests.get("{}".format(url_index),headers=headers)
    print(url_r.status_code)
    url_r.encoding = 'utf-8'    
#mfw的链接数组
    url_list = []
    url_r_single = re.findall("<a href=\"/t(.*?)\".*?>",url_r.text.strip('\n'),re.S)
    for i in url_r_single:
        url_i = "https://www.mafengwo.cn/t" + i
        url_list.append(url_i)       
#    print(url_list[1])
    return (url_list)

#t = "https://www.mafengwo.cn/mdd/"   #mfw的url主页
#mfw_url(t)