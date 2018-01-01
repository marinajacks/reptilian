#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:53:36 2017

@author: macbook
"""

#import urllib.request
import requests
from bs4 import BeautifulSoup
import re

url='http://faculty.ecnu.edu.cn/search/teacherMain.faces?siteId=10&pageId=0'
res=requests.get(url)
res.status_code
res.encoding='utf-8'


soup=BeautifulSoup(res.text,'html.parser')

content=soup.find_all(href=re.compile("teacherList"))

teacherurls=[]
for k in content:
    teacherurl=[]
    teacherurl.append(url[:url.find('/search')]+k.get('href'))
    print(k.get('href'))  #获取对应的地址
    print(k.string)
    teacherurls.append(teacherurl)




url='http://faculty.ecnu.edu.cn/search/teacherMain.faces?siteId=10&pageId=0'
'''这个函数是根据学校的教师信息的主页获取的各院系的url,但是现在有一个问题是有可能地址下面还存
在二级子目录,这需要进一步的处理'''
def academyurl(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')

    content=soup.find_all(href=re.compile("teacherList"))
    academys=[]
    for k in content:
        academy=[]
        academy.append(url[:url.find('/search')]+k.get('href'))
        print(k.get('href'))  #获取对应的地址
        print(k.string)
        academys.append(academy)
    return academys
    
    


#院系的主页url
url='http://faculty.ecnu.edu.cn/search/teacherList.faces?siteId=10&pageId=0&nodeId=18'

'''这个函数是根据院系的主网URL,获取到教师的个人主页url'''
def teacherurl(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content=soup.find_all(href=re.compile("main.jspy"),target='_blank')
    urls=[]
    for k in content:
        urls.append(url[:url.find('/search')]+k.get('href'))
    return urls



#这个函数是为了获取老师的信息
url='http://faculty.ecnu.edu.cn/s/3140/main.jspy'

url='http://faculty.ecnu.edu.cn/s/436/main.jspy'

url='http://faculty.ecnu.edu.cn/s/920/main.jspy'

url='http://faculty.ecnu.edu.cn/s/1567/main.jspy'
'''teacherinfo函数是为了获取老师的个人信息,输入的信息是老师的个人主页url'''
def teacherinfo(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    
    content0=soup.find_all(id="xingming") #获取姓名
    xingming=content0[0].string.strip() 
    '''
    content00=soup.find_all(id="touxiang") #获取头像
    touxiang=url[:url.find('/s')]+content00[0].find('img').get('src')
    '''
    content01=soup.find_all(id="zhicheng") #获取职称
    zhicheng=content01[0].string.strip()
    
    content02=soup.find_all(id="zhiwu")  #获取职务
    if('NoneType' in str(type(content02[0].find('table')))):
        zhiwu=''
    else:
        zhiwu=content02[0].find('table').find('td').find('tr').getText().strip()
    
    content1=soup.find_all(id="danwei") #获取学院
    danwei=content1[0].string.strip() 

    content2=soup.find_all(id="danwei2") #获取院系  
    if('NoneType' in str(type(content2[0].find('table')))):
        danwei2=''
    else:
        danwei2=content2[0].find('table').find('td').find('tr').getText().strip()

    
    content3=soup.find_all(id="lxdh") #获取联系电话
    if('NoneType' in str(type(content3[0].find('table')))):
        lxdh=''
    else:
        lxdh=content3[0].find('table').find('td').find('tr').getText().strip()

    
    content4=soup.find_all(id="bgsj") #获取办公时间
    if('NoneType' in str(type(content4[0].find('table')))):
        bgsj=''
    else:
        bgsj=content4[0].find('table').find('td').find('tr').getText().strip()
    
    content5=soup.find_all(id="cz") #获取传真
    if('NoneType' in str(type(content5[0].find('table')))):
        cz=''
    else:
        cz=content5[0].find('table').find('td').find('tr').getText().strip()
        
    content6=soup.find_all(id="zywz")  #获取主页网址
    if('NoneType' in str(type(content6[0].find('table')))):
        zywz=''
    else:
        zywz=url[:url.find('/s')]+content6[0].find('table').find('td').find('tr').getText().strip()
        
    content7=soup.find_all(id="bgdd")  #获取办公地址
    if('NoneType' in str(type(content7[0].find('table')))):
        bgdd=''
    else:
        bgdd=content7[0].find('table').find('td').find('tr').getText().strip()
    
    content8=soup.find_all(id="dzyx")  #获取电子邮箱
    if('NoneType' in str(type(content8[0].find('table')))):
        dzyx=''
    else:
        dzyx=content8[0].find('table').find('td').find('tr').getText().strip()
    
    content9=soup.find_all(id="txdz")  #通讯地址
    if('NoneType' in str(type(content9[0].find('table')))):
        txdz=''
    else:
        txdz=content9[0].find('table').find('td').find('tr').getText().strip()
    '''    
    content10=soup.find_all(id="yjfx")
    if('NoneType' in str(type(content10[0].find('table')))):
        yjfx=''
    else:
        yjfx=content10[0].find('table').find('td').find('tr').getText().strip().replace('\n',',')
    
    content11=soup.find_all(id="shjz")
    if('NoneType' in str(type(content11[0].find('table')))):
        shjz=''
    else:
        shjz=content11[0].find('table').find('td').find('tr').getText().strip().replace('\n',',')


    content12=soup.find_all(id="xscg")
    if('NoneType' in str(type(content12[0].find('table')))):
        xscg=''
    else:
        xscg=content12[0].find('table').find('td').find('tr').getText().strip().replace('\n','.').replace('\r','')
    '''
    '''
    teacher={'xingming':[xingming],'touxiang':[touxiang],'zhicheng':[zhicheng],
             'zhiwu':[zhiwu],'danwei':[danwei],'danwei2':[danwei2],'lxdh':[lxdh],
             'bgsj':[bgsj],'cz':[cz],'zywz':[zywz],'bgdd':[bgdd],'dzyx':[dzyx],
             'txdz':[txdz],'yjfx':[yjfx],'shjz':[shjz],'xscg':[xscg]}
    '''
    teacher1={'xingming':[xingming],'zhicheng':[zhicheng],'zhiwu':[zhiwu],
              'danwei':[danwei],'danwei2':[danwei2],'lxdh':[lxdh],'bgsj':[bgsj],
              'cz':[cz],'zywz':[zywz],'bgdd':[bgdd],'dzyx':[dzyx],'txdz':[txdz]}
    return teacher1
    
    
   
    



url1='http://faculty.ecnu.edu.cn/search/teacherList.faces?siteId=10&pageId=0&nodeId=59'
url2='http://faculty.ecnu.edu.cn/search/teacherList.faces?siteId=10&pageId=0&nodeId=12'
    
    
'''
def getname(n,name):
    print('content'+str(n)+'=soup.find_all(id="'+name+'\")')
    print(name+'=content'+str(n)+'[0].string.strip()')
'''    

'''在将数据写入数据库之前,需要在数据库中建立相关的表,然后再将数据导入到数据库中,




'''  
    
    
#下面的函数是为了进行数据的写入,将数据写入到数据库中
import pymysql
import pandas as pd
conn = pymysql.Connect(
     host='localhost',
     port=3306,
     user='root',
     passwd='123456'
 )
cursor = conn.cursor()
sql="select * from test.qq"

df=pd.read_sql(sql,conn)