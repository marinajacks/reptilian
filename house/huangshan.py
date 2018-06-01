#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:07:41 2018

@author: macbook
58同城房产数据爬虫
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:56:13 2018

@author: macbook
安居客卡米小镇数据的爬虫信息数据库
"""

import requests
from bs4 import BeautifulSoup
import pymysql

def test():
    url="http://huangshan.58.com/ershoufang/"
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    s1=soup.find(class_="house-list-wrap")
    s2=s1.find_all(class_="")
    '''
    path1='/Users/macbook/documents/project/reptilian/house/cami1.txt'
    name='cami2'
    path2=path1.replace('cami1',name)
    f=open(path2,'w',encoding='UTF-8')
    '''
    #s=s2[0]
    for s in s2:
        print(getvalues(s))
    #s.find(class_='infos')
    
    infos=[]
    s=s2[100]
    hd=s.find(class_='list-info')
    #.find(class_='hd').getText()
    infos.append(hd)
    info2=s.find(class_='infos').find(class_='detail').getText()
    for i in info2.strip().split('\n'):
        print(i.replace('|',''))
        infos.append(i.replace('|',''))
        
    price=s.find(class_='cbook-price').getText()
    infos.append(price)
   
#解析url获取到对应的元素数据
def getitems(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    s=soup.find(class_="cbook-list").find_all(class_='item')
    return s

#根据解析得到的数据,整理成数组存储
def getvalues(s):   
    infos=[]
    hd=s.find(class_='list-info').find(class_='hd').getText()
    infos.append(hd)
    info2=s.find(class_='infos').find(class_='detail').getText()
    for i in info2.strip().split('\n'):
        infos.append(i.replace('|',''))
        
    price=s.find(class_='cbook-price').getText()
    infos.append(price)
    return infos

#将数据写入到文件中     
def test1():
    url="http://huangshan.58.com/ershoufang/"
    s=getitems(url)
    for i in s:
        print(getvalues(i))
    path1='/Users/macbook/documents/project/reptilian/house/huangshan.txt'
    f=open(path1,'a',encoding='UTF-8')
    for i in s:
        f.write(str(getvalues(i)))
        f.write('\n')
    f.close()
    
    
def writebase(infos):
    conn = pymysql.Connect(
         host='localhost',
         port=3306,
         user='root',
         passwd='123456',
         db='ecnu',
         charset='utf8'
     )
    cursor = conn.cursor()
    
    a=infos
    if(len(infos)==7):
        cursor.executemany("insert into kami(notes,area,rooms,unitprice,floor,year,totalprice) values(%s,%s,%s,%s,%s,%s,%s)"
                           ,[(a[0],a[1],a[2],a[3],a[4],a[5],a[6])])
        conn.commit()
    else:
        pass
    cursor.close()
    conn.close()
    
    
    
    
    

if __name__ == "__main__":
    #url="https://www.anjuke.com/ks/cm608524/"
    url='https://www.anjuke.com/ks/cm656247/#filtersort'
    u='https://www.anjuke.com/ks/cm656247-p'
    urls=[]
    urls.append(url)
    for i in range(1,2):
        urls.append(u+str(i+1)+'/#filtersort')
    for url in urls:
        s=getitems(url)
        for i in s:
            a=getvalues(i)
            writebase(a)
