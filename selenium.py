#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 15:13:12 2018

这个主要是为了学习selenium这个框架设计的相关知识
@author: macbook
"""

import requests

from selenium import webdriver

from bs4 import BeautifulSoup  
import time

def test(n,m):
    path='/Users/macbook/downloads/geckodriver'
    
    driver = webdriver.Firefox(executable_path =path)
    
    url="http://info.2012.163.com/athlete/list/"
    
    driver.get(url)
    
    m0=driver.find_elements_by_class_name("right_arrow")
    
    for i in range(n):
        m0[0].click()
       # print('click it')
        #time.sleep(1) #休眠一次
    
    for j in range(m):
        m0[1].click()
        #print('click it')
        #time.sleep(1) #休眠一次
    #使用find_elements_by_xpath这个方法显然可以按照地址获取到更详细的信息
    href=driver.find_elements_by_xpath("//*[@href]")
    hrefs=[]
    hrefss=[]
    for i in href:
        #这一部分的主要目的是为了将href信息获取到
        if('athlete' in i.get_attribute('href').split('/') 
        and i.get_attribute('href').split('.')[-1]=='html'
        and 'list_alphabet' not in i.get_attribute('href').split('/')):
            #print(i.get_attribute('href'))
            hrefs.append(i.get_attribute('href'))
          #  print('write one')
    #这个代码主要是为了将重复的部分去除掉
    for i in hrefs:
         if i not in hrefss:
             hrefss.append(i)
            # print('get it')
 
    driver.quit()
    return hrefss

    href=driver.find_elements_by_xpath("//*[@src]") 
#这个函数采用的是
def main(driver,n):
    for i in range(n):
        m=driver.find_elements_by_class_name("left_arrow")
        m[1].click()
        time.sleep(2)
        s=driver.find_elements_by_class_name("MContent-list2")
        #time.sleep(2)
        
        a=s[1].text.split('\n')
        b=[]
        for i in a:
            if i=='':
                pass
            else:
                b.append(i)
        for i in b:
            print(i)

#获取运动员的相关信息
def athlete(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content=soup.find_all(class_='table')
    b=content[0].find_all('li')
    info=[]
    info.append(content[0].find('h1').getText().split('\t'))
    infos=[]
    infos.append('姓名：'+info[0][0].split(' ')[0])
    infos.append('拼音：'+info[0][0].replace(info[0][0].split(' ')[0],'').strip())
    for name in b:
       # info.append(name.getText())
        infos.append(name.getText())
       # print(name.getText())
    #这里主要是为了使得海外的运动的信息也能够保持完整,对于最后一个籍贯也补充完整
    if(len(infos)<9):
        infos.append('籍贯：')
        #infos.append('注册单位：') 这里应该是由注册单位的,但是我们并不把这个数据放到数据库中
    return infos

#这个函数主要是为了讲数据写入到数据库中
def writebase(a):
    b=[]
   
    for i in a:
        b.append(i.split('：')[1])
  
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
    
    cursor.executemany("insert into athlete(name,spell,gender,nation,birthday,height,weight,item,province) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                   ,[(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8])])
    conn.commit()
    cursor.close()
    conn.close()

def compus():
    url='https://portal1.ecnu.edu.cn/cas/login?service=http%3A%2F%2Fportal.ecnu.edu.cn%2Fneusoftcas.jsp'
    path='/Users/macbook/downloads/geckodriver'
    
    driver = webdriver.Firefox(executable_path =path)
    
    
    driver.get(url)
    
    driver.find_element_by_id('un').send_keys('51174500004')
        
    driver.find_element_by_id('pd').send_keys('han1990yan')
    
    driver.find_element_by_class_name('ide_code_input').send_keys('3003')

    driver.find_element_by_id('index_login_btn').click()


if __name__ == "__main__":
    
    hrefs=test(5,5)
    wrong=0
    for i in hrefs:
        if(len(athlete(i))<9):
            wrong+=1
            pass
        else:
           # writebase(athlete(i))
            print(athlete(i))
        
    
    
    
