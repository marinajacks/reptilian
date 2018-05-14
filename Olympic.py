#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 20:25:20 2018
这个脚本主要是为了获得奥林匹克运动员的相关数据,从而得到相关的运动员的个人信息，
便于进行进一步的数据分析

@author: macbook
"""

import requests
from bs4 import BeautifulSoup
import re


#url='http://info.2012.163.com/athlete/584.html'
'''
res=requests.get(url)



soup=BeautifulSoup(res.text,'html.parser')

content=soup.find_all(class_='table')




print(content[0].find('h1').getText())

b=content[0].find_all('li')

#print(len(b))

for name in b:
    print(name.getText())
'''

url='http://info.2012.163.com/athlete/list/'

res=requests.get(url)


soup=BeautifulSoup(res.text,'html.parser')
    
content1=soup.find_all(class_='clearfix switch-item')

#content=soup.find_all(class_='logo')

#u=content1[9].find_all('li')#.find('a').get('href')

for content in content1:
    u=content.find_all('li')
    for u0 in u:
        url0=(u0.find('a').get('href'))
        print(u0.find('a').get('title'),end=' ')
        urls=url.replace(url.split('/')[-2],url0.split('/')[-1])
        urls=urls[0:len(urls)-1]
        print(urls)



'''
content2=soup.find_all(class_='clearfix switch-item')

u=content2[0].find_all('li')

u[0].find_all(class_='logo')
'''

#content2[19].find_all('li')



#print(content)


'''

#下面的函数用来处理运动员的相关信息,获取例如姓名、性别等相关数据
def athlete(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content=soup.find_all(class_='table')
    b=content[0].find_all('li')
    info=[]
    print(content[0].find('h1').getText())
    info.append(content[0].find('h1').getText().split('\t'))
    for name in b:
        print(name.getText())
        info.append(name.getText())
    return info
    

info=athlete(url)
'''