#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 19:54:36 2018

@author: macbook
这个程序主要是为了进行医药数据的分析得来的
"""
import requests as res 
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import os


def getdurg(drugname,p,name,password):
    #url='http://www.chemcpd.csdb.cn/cmpref/Tcm_Multi/R_tcd_Comp.asp'
    #headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    #response=requests.get(url,headers=headers)
    #现在我们发现为什么在使用编码的时候出现原始的代码的问题,主要就是原始的代码出现父编码与本层的编码
    #格式出现不一致的问题.另外,从这里可以看到,实际上我们需要使用到动态的网页爬虫技术来进行网页的登陆
   # path='/Users/macbook/downloads/geckodriver'
    path='D:\project\selenium\geckodriver'
    driver = webdriver.Firefox(executable_path =path)
    url1='http://www.chemcpd.csdb.cn/cmpref/main/tcm_introduce.asp?n%20Count=6077992'
    driver.get(url1)
    
    #下面是模拟登陆的页面
    driver.find_element_by_name('Username').clear()   #清除用户名字
    driver.find_element_by_name('Username').send_keys(name)#输入用户名
    driver.find_element_by_name('Password').clear()   #清除用户密码
    driver.find_element_by_name('Password').send_keys(password)#输入用户密码
    driver.find_element_by_name('login').click()   #点击登陆
    #文本检索数据信息
    driver.find_element_by_link_text('中药药材检索').click()
    #driver.find_element_by_link_text('中药药材检索').get_attribute("href") 这部分的数据主要是为了
    #获取到中药药材检索对应的href数据,其实不一定是为了获取到这些数据,还可以直接click来跳转到对应的网页
    
    driver.find_element_by_name('Specname').clear()
    driver.find_element_by_name('Specname').send_keys(drugname)
    driver.find_element_by_id('submit1').click()
    driver.find_element_by_name('FID').click()
    driver.find_element_by_name('Tcd_Comp_ID').click()
    n=int((driver.find_elements_by_tag_name('font')[-1]).find_element_by_tag_name('b').text)

    '''
    drugs=[]
    #这里使用表格的数据查询方式,给出数据的处理方式
    for cl in range(2):
        table = driver.find_element_by_class_name('newform')
        table_rows = table.find_elements_by_tag_name('tr')
        
        for i in table_rows:
            drug=[]
            for j in range(0,len(i.find_elements_by_tag_name('td'))):
                drug.append((i.find_elements_by_tag_name('td'))[j].text)
                print((i.find_elements_by_tag_name('td'))[j].text)
            drugs.append(drug)
            print(i.text)
        driver.find_element_by_name('next').click()
     '''   
    
     #下面是另外的一种写法,这种写法可以有效的把开头的数据清理掉
    drugs=[]
    names=[]
     
    table = driver.find_element_by_class_name('newform')
    table_rows = table.find_elements_by_tag_name('tr')
    tds=table_rows[0].find_elements_by_tag_name('td')
    for i in range(1,len(tds)):
           names.append(tds[i].text)
    drugs.append(names)
        
    for cl in range(1,n):
       table = driver.find_element_by_class_name('newform')
       table_rows = table.find_elements_by_tag_name('tr')
    
       for i in range(1,len(table_rows)):
           drug=[]
           tds=table_rows[i].find_elements_by_tag_name('td')
           for j in range(1,len(tds)):
               drug.append(tds[j].text)
               print(tds[j].text)
           drugs.append(drug)
           print(table_rows[i].text)
            
       driver.find_element_by_name('next').click()
      
    table = driver.find_element_by_class_name('newform')
    table_rows = table.find_elements_by_tag_name('tr')
    
    for i in range(1,len(table_rows)):
           drug=[]
           tds=table_rows[i].find_elements_by_tag_name('td')
           for j in range(1,len(tds)):
               drug.append(tds[j].text)
               print(tds[j].text)
           drugs.append(drug)
           print(table_rows[i].text)
           
        
    df=pd.DataFrame(drugs)
    
    df.to_excel(p)
    driver.quit()

    
    
    
def test():
    url=driver.current_url
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response=requests.get(url,headers=headers)
    r=response.text
    #b = r.encode('ISO-8859-1').decode(response.apparent_encoding)
    
    
    
    
    '''#这部分的数据主要是模拟登陆的样例
    driver.find_element_by_name('Username').clear()   #清除用户名字
    driver.find_element_by_name('Username').send_keys('marina')#输入用户名
    driver.find_element_by_name('Password').clear()   #清除用户密码
    driver.find_element_by_name('Password').send_keys('han#1990@yan')#输入用户密码
    driver.find_element_by_name('login').click()   #点击登陆
    url=driver.current_url
    driver.find_element_by_name('txtQuery')
    '''

    
    r=response.text 
   # b = r.encode('ISO-8859-1').decode(response.apparent_encoding) 
    #print(b)



    soup=BeautifulSoup(res.text,'html.parser')
   






if __name__=="__main__":

    print('hello world!')
    herb=input('中药名称(中文)')
    name=input("输入用户名:")
    password=input("输入用户密码:")
    '''
    #这个是mac的地址
    #p='/Users/macbook/documents/project/reptilian/medicine/中药数据/上海有机/'
    p1=r'D:\project\reptilian\medicine\中药数据\上海有机所1'+'\\'+herb
    if os.path.exists(p1):
        pass
    else:
        os.makedirs(p1) 
    #p1=p+herb+'/'+herb+'.xlsx' win下的设计
    p=p1+'\\'+herb+'.xlsx'
    '''
    herb='浙贝母'

    p1='d://2.xlsx'
    getdurg(herb,p1,name,password)
