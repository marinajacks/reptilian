#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:55:08 2018

@author: macbook
这个部分主要是为了进行模拟登陆的操作,然后进行模拟控制的操作
这个部分的数据主要是TCMID里边的数据,后边的
"""

import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.common.exceptions import NoSuchElementException 
import time
import os
import pandas as pd

#解析获取到文本的
def getdrug(drugname):
    #这个是通过模拟人的行为找到对应的药物的网页
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path=path)
    url='http://www.megabionet.org/tcmid/'
    driver.get(url)
    #模拟查询药物的相关操作
    url1=[drugname]
    driver.find_element_by_link_text('Search').click()
    driver.find_element_by_id('Channel12').click()
    driver.find_element_by_id('id_chinese_Name').clear()
    driver.find_element_by_id('id_chinese_Name').send_keys(drugname)
    #driver.current_window_handle #页面会发生跳转,这个命令用来将driver页面转换
    time.sleep(1)
    driver.find_element_by_id('id_chinese_Name').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.switch_to_window(driver.window_handles[1])
    try:
        driver.find_element_by_link_text(drugname).click()
        url1.append(driver.current_url)
    except NoSuchElementException:
        url1.append(driver.current_url)
    driver.quit()
    return url1

#解析页面所有的成分url
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
                urls.append('http://'+url.split('/')[2]+j.find('a')['href'])
            else:
                print(j.find('a').string)
    return urls


#这里的操作主要是解析页面对应的文本信息，这里主要是成分名称和PubchenCid
def durginfos(url):
    #url='http://www.megabionet.org/tcmid/ingredient/31556/'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response=requests.get(url,headers=headers)
    r=response.text
    soup=BeautifulSoup(r,'html.parser')
    titles=soup.find(class_='title text-font').string.strip().replace('Ingredient -- ','')
    pubchemid=soup.find_all(class_='section-text text-font')[2].string.strip()
    info=[]
    info.append(titles)
    info.append(pubchemid)
    return info










def PubChemUrl(module):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    driver.find_element_by_id('term').clear()
    driver.find_element_by_id('term').send_keys(module)
    driver.find_element_by_id('search').click()
    time.sleep(1)
    test=driver.find_elements_by_id('Canonical-SMILES') #确定是不是只有一个页面
    url1=[]
    if(len(test)==1):
        url1=driver.current_url
        print('唯一页面',url1)
    else:
        value=driver.find_elements_by_class_name('rsltcont')
        if(len(value)>0):
            url1=value[0].find_element_by_tag_name('a').get_attribute("href")
            print('多页面',url1)
        else:
            print('无页面')
            pass
    driver.quit()
    return url1


#这个函数用来获取药品成分对应的Url信息，输入的参数是
def PubChemUrls(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    urls=[]
    for name in modules:
        urls0=[]
        urls0.append(name)
        driver.find_element_by_id('term').clear()
        driver.find_element_by_id('term').send_keys(name)
        driver.find_element_by_id('search').click()
        '''这里默认的是第一个地址就是我们需要的那个药品的成分信息
           下面首先需要获取到的就是第一条对应的数据，这里默认的就
           是第一条数据作为需要的数据也是合理的。但是这里存在一个
           问题，就是这里在选择结果的时间，查询结果可能是空的,所以,
           这里需要进行异常设计.另外,由于问题的种类至少有两种,所以,
           这里还需要首先判断是不是单一结果,如果是单一的结果,数据
           需要首先单独的跑出来,然后再继续判断其他的异常.
        '''
        time.sleep(1)
        test=driver.find_elements_by_id('Canonical-SMILES') #确定是不是只有一个页面
        if(len(test)==1):
            url1=driver.current_url
            urls0.append(url1)
            print('唯一页面',url1)
        else:
            value=driver.find_elements_by_class_name('rsltcont')
            if(len(value)>0):
                url1=value[0].find_element_by_tag_name('a').get_attribute("href")
                urls0.append(url1)
                urls.append(urls0)
                print('多页面',url1)
            else:
                print('无页面')
                pass
        url='https://www.ncbi.nlm.nih.gov/pccompound/'
        driver.get(url)
        time.sleep(1)
    driver.quit()
    return urls


def main(drugs):
    modules=[]
    for drugname in drugs:
        url=getdrug(drugname)
        urls=Ingredient(url)
        locates=molecules(urls)
        for i in locates:
            if(i[4]=='NA'):
                url0=PubChemUrl(i[2])
                if(url0==[]):
                    pass
                else:
                    i[4]=url0.split('/')[-1]
                    i[-1]=url0
                print(i)
        for locate in locates:
            modules.append(locate)
        '''
        urls=geturls(url)
        for url0 in locates:
            modules.append(durginfo(url0))
        '''
        print(drugname+' is success!')
    return modules


if __name__=='__main__':
    drugs=['ZHE BEI MU','SAN QI','YI YI REN']
    modules=main(drugs)
    
    #处理特殊的成分的操作
    path4='D:\MarinaJacks\project\\reptilian\medicine\中药数据\TCMSP\龙血竭\龙血竭.xlsx'
    Dragon=module(path4)
    dragons=PubChemUrls(Dragon)
    for i in dragons:
        i.append('LONG XUE JIE')
        
    druginfo=[]
    for j in modules:
        info=[]
        info.append(j[0])
        info.append(j[2])
        info.append(j[4])
        info.append(j[5])
        druginfo.append(info)
        
    for k in dragons:
        info=[]
        info.append(k[2])
        info.append(k[0])
        info.append(k[1].split('/')[-1])
        info.append(k[1])
        druginfo.append(info)
        
    druginfos=[]
    for i in druginfo:
        if(i[2]=='NA'):
            pass
        else:
            druginfos.append(i)
        
    
    urls=[]
    for i in druginfos:
        urls.append(i[3])
    
    urls0=[]
    for i in urls:
        if(i not in urls0):
            urls0.append(i)
    


    SFDS_2D(address)
    

    
    

    
   
    
    
    
