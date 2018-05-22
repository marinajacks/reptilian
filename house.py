#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:50:52 2018

@author: macbook
"""
from bs4 import BeautifulSoup

import requests

import sys

from imp import reload

reload(sys)
'''
url='https://sh.lianjia.com/ershoufang/'


res=requests.get(url)


soup=BeautifulSoup(res.text,'html.parser')

clears=soup.find_all(class_='clear')


clears1=soup.find_all(class_='info clear')
'''
#获取到所有的链接数据
def getall():
    urlss=[]
    url0='https://sh.lianjia.com/ershoufang/pg'
    urlss.append(url0)
    for i in range(1,100):
        print(url0+str(i+1)+'/')
        urlss.append(url0+str(i)+'/')
    return urlss

#从每个链接中获取到需要的信息
def getinfo(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    clears=soup.find_all(class_='info clear')
    return clears
    
#将初步的信息处理获取到需要的详细信息
def test(clears):
    
    names=['title','address','flood','followInfo','tag','priceInfo']
    values=''
    for j in clears:
        for i in names:
            if('NoneType' in str(type(j.find(class_=i)))):
                pass
            else:
                print(i+":"+str(j.find(class_=i).getText()))
                values+=i+":"+str(j.find(class_=i).getText())+'\t'
    values=values+'\n'
    return values
    
#将数据写入到文本中
def writelocal(local,text):
    f=open(local,'w')
    
    f.write(text)
    f.close()
  
#将数据写入到数据库中
def writebase():
    import pymysql
    conn = pymysql.Connect(
         host='localhost',
         port=3306,
         user='root',
         passwd='123456',
         db='ecnu',
         charset='utf8'
     )
    cursor = conn.cursor()
    
    cursor.executemany("insert into house(xingming,zhicheng,zhiwu,danwei,danwei2,lxdh,bgsj,cz,zywz,bgdd,dzyx,txdz) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                    ,[(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11])])
    conn.commit()
    cursor.close()
    conn.close()
    
    
local='/Users/macbook/documents/project/reptilian/house.txt'
f=open(local,'w')

f.write(values)    


#clears[10].find(class_='title').getText()


if __name__=="__main__":
    local='/Users/macbook/documents/project/reptilian/house.txt'
    urls=getall()
    for i in range(10):#len(urls)):
        clears=getinfo(urls[i])
        values=test(clears)
        values.encode("utf8")
       # writelocal(local,values)
        
 