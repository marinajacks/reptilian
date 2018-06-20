#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:55:08 2018

@author: macbook
这个部分主要是为了进行模拟登陆的操作,然后进行模拟控制的操作.
"""

import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys  
import urllib.request
import time

def geturls(url):
    #下面的数据主要是为了获取到页面的药品链接信息
    #url='http://www.megabionet.org/tcmid/herb/5615/'
    #url='http://www.megabionet.org/tcmid/herb/2186/'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response=requests.get(url,headers=headers)
    urls=[]
    soup=BeautifulSoup(response.text,'html.parser')
    drugs=soup.find_all(class_='table table-striped table-bordered table-hover')[1]
    for i in drugs.find_all('tr'):
        j=i.find_all('td')[0]#J
        if(j.find('a') is None):
            print(' ')
        else:
            if('tcmid' in (j.find('a')['href'])):
                #print('www.megabionet.org/'+j.find('a')['href'])
                urls.append('http://www.megabionet.org/'+j.find('a')['href'])
            else:
                print(j.find('a').string)
    
    return urls
    
    
    




#这里的操作主要是解析页面对应的文本信息
def durginfo(url):
    #url='http://www.megabionet.org/tcmid/ingredient/31556/'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response=requests.get(url,headers=headers)
    r=response.text
    #b = r.encode('ISO-8859-1').decode(response.apparent_encoding)
    #path='D:\project\reptilian\medicine\imgs'
    soup=BeautifulSoup(r,'html.parser')
    #￥title=soup.find(class_='title text-font').string.strip()
    titles=soup.find(class_='title text-font').string.strip().replace('Ingredient -- ','')
    formula=soup.find_all(class_='section-text text-font')[0].string.strip()
    pubchemid=soup.find_all(class_='section-text text-font')[2].string.strip()
    smile=soup.find_all(class_='section-text text-font')[3].string.strip()
    #structure=url.split('//')[1].split('/')[0]+soup.find_all(class_='section-text text-font')[4].find("img").get('src')
    #imgs=title.split('--')[1].strip()+"."+structure.split('/')[-1].split('.')[1]
    #paths=path+'\\'+imgs
    
    info=[]
    info.append(titles)
    info.append(formula)
    info.append(pubchemid)
    info.append(smile)
    return info


def getdrug(drugname):
    #这个是通过模拟人的行为找到对应的药物的网页
    #path='D:\project\selenium\geckodriver'
    path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path=path)
    url='http://www.megabionet.org/tcmid/'
    driver.get(url)
    #模拟查询药物的相关操作
    driver.find_element_by_link_text('Search').click()
    driver.find_element_by_id('Channel12').click()
    driver.find_element_by_id('id_chinese_Name').clear()
    driver.find_element_by_id('id_chinese_Name').send_keys(drugname)
    driver.current_window_handle #页面会发生跳转,这个命令用来将driver页面转换
    time.sleep(1)
    driver.find_element_by_id('id_chinese_Name').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.switch_to_window(driver.window_handles[1])
    url1=driver.current_url
    return url1


if __name__=='__main__':
    drugname=input('请输入中药名称:')
    url=getdrug(drugname)
    num=input('输入页面个数:')
    p='/Users/macbook/documents/project/reptilian/medicine'
    #p=r'D:\project\reptilian\medicine'
    
    urls=geturls(url)
    drugs=[]
    drugs.append(['titles','formula','pubchemid','smile'])
    for url0 in urls:
        print(durginfo(url0))
        drugs.append(durginfo(url0))
    drug=pd.DataFrame(drugs)
    p=p+'\\'+drugname+num+'.xlsx'
    drug.to_excel(p,sheet_name=drugname,header =False)
        