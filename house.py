#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:50:52 2018

@author: macbook
"""
from bs4 import BeautifulSoup

import pymysql

import requests

'''
url='https://sh.lianjia.com/ershoufang/'


res=requests.get(url)


soup=BeautifulSoup(res.text,'html.parser')

clears=soup.find_all(class_='clear')


clears1=soup.find_all(class_='info clear')
'''
#获取到所有的链接数据
def getall(city):
    urlss=[]
    url0='https://'+city+'.lianjia.com/ershoufang/pg'
    urlss.append(url0)
    for i in range(1,100):
        #print(url0+str(i+1)+'/')
        urlss.append(url0+str(i)+'/')
    return urlss

#从每个链接中获取到需要的信息
def getinfo(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
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
  
city='sh'
#将数据写入到数据库中
def writebase(city,values):
    conn = pymysql.Connect(
         host='localhost',
         port=3306,
         user='root',
         passwd='123456',
         db='ecnu',
         charset='utf8'
     )
    cursor = conn.cursor()
    
    house=values.split('\n')
    for h in house:
        a=h.split('\t')
        if(len(a)==10):
            cursor.executemany("insert into house(city,village,rooms,area,orientation,lift,floor,address,totalprice,unitprice) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                        ,[(city,a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8])])
            conn.commit()
        else:
            pass
    cursor.close()
    conn.close()
    
'''   
local='/Users/macbook/documents/project/reptilian/house.txt'
f=open('/Users/macbook/documents/project/reptilian/house.txt','w',encoding='UTF-8')

f.write(values)    

'''


if __name__=="__main__":
    local='/home/macbook/project/reptilian/house3.txt'
    city=input('输入城市编码')
    city1=city+'1'
    urls=getall(city)
    local=local.replace('house3',city1)
    for url in urls:
        clears=getinfo(url)
        values=test(clears)
        print(values)
        #writelocal(local,values)
        writebase(city,values)
    print("over")
        
 