#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:50:52 2018

@author: macbook
"""
from bs4 import BeautifulSoup

import pymysql

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
        #print(url0+str(i+1)+'/')
        urlss.append(url0+str(i)+'/')
    return urlss

#从每个链接中获取到需要的信息
def getinfo(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    clears=soup.find_all(class_='info clear')
    return clears
    
#将初步的信息处理获取到需要的详细信息,这个数据获取到主要是为了进行文本的处理
def test(clears):
    
    #names=['title','address','flood','followInfo','tag','priceInfo','totalPrice','unitPrice']
    names=['address','flood','totalPrice','unitPrice']

    values=''
    for j in clears:
        for i in names:
            if('NoneType' in str(type(j.find(class_=i)))):
                pass
            else:
                if(i=='address'):
                    info=j.find(class_=i).getText().split('|')
                    for k in info:
                        values+=k.strip()+'\t'
                elif(i=='flood'):
                    info=j.find(class_=i).getText().split('-')
                    for l in info:
                        values+=l.strip()+'\t'
                        #print(k)
                elif(i=='unitPrice'):
                    info=j.find(class_=i).getText()
                    values+=info.replace('单价','')+'\t'
                else: 
                    #print(i+":"+str(j.find(class_=i).getText()))
                        #values+=i+":"+str(j.find(class_=i).getText())+'\t'
                    values+=str(j.find(class_=i).getText()).strip()+'\t'
        values+='\n'
   # values=values+'\n'
    
    return values

def getvalues():
       
    #names=['title','address','flood','followInfo','tag','priceInfo','totalPrice','unitPrice']
    names=['address','flood','totalPrice','unitPrice']

    values=''
    for j in clears:
        for i in names:
            if('NoneType' in str(type(j.find(class_=i)))):
                pass
            else:
                if(i=='address'):
                    info=j.find(class_=i).getText().split('|')
                    for k in info:
                        values+=k.strip()+'\n'
                elif(i=='flood'):
                    info=j.find(class_=i).getText().split('-')
                    for l in info:
                        values+=l.strip()+'\n'
                        #print(k)
                elif(i=='unitPrice'):
                    info=j.find(class_=i).getText()
                    values+=info.replace('单价','')+'\n'
                else: 
                    #print(i+":"+str(j.find(class_=i).getText()))
                        #values+=i+":"+str(j.find(class_=i).getText())+'\t'
                    values+=str(j.find(class_=i).getText()).strip()+'\n'
        values+='\n'
   # values=values+'\n'
    
    return values
    
'''将数据写入到文本中,这里在进行文本写入的时候遇到这样的问题,那就是UnicodeEncodeError,
这时候需要需要做的是在读取文件时加入指定UTF-8编码的选项,f = open('content.txt','a',
encoding='UTF-8'),另外在另外需要注意的是使用requests获取到网页之后同样要指定编码
另外需要注意的是使用requests获取到网页之后同样要指定编码.
html = requests.get(url)
html = re.sub(r'charset=(/w*)', 'charset=UTF-8', html.text)

'''
def writelocal(local,text):
    f=open(local,'a+',encoding='UTF-8')
    f.write(text)
    f.close()
  
#将数据写入到数据库中
def writebase(a):
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
    
'''   
local='/Users/macbook/documents/project/reptilian/house.txt'
f=open('/Users/macbook/documents/project/reptilian/house.txt','w',encoding='UTF-8')

f.write(values)    

'''


if __name__=="__main__":
    local='/Users/macbook/documents/project/reptilian/house.txt'
    urls=getall()
    for url in urls:
        clears=getinfo(url)
        values=test(clears)
        print(values)
        writelocal(local,values)
    print("over")
        
 