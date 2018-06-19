#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:55:08 2018

@author: macbook
这个部分主要是为了进行模拟登陆的操作,然后进行模拟控制的操作.
"""

import requests as res 
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

def getdurg(drugname,p,n):
    #url='http://www.chemcpd.csdb.cn/cmpref/Tcm_Multi/R_tcd_Comp.asp'
    #headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    #response=requests.get(url,headers=headers)
    #现在我们发现为什么在使用编码的时候出现原始的代码的问题,主要就是原始的代码出现父编码与本层的编码
    #格式出现不一致的问题.另外,从这里可以看到,实际上我们需要使用到动态的网页爬虫技术来进行网页的登陆
    path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path =path)
    url1='http://lsp.nwu.edu.cn/tcmspsearch.php?qs=herb_all_name&q=&token=725a2aa9848eaf89e7c0a2fc98a61d96'
    driver.get(url1)
    
    
    
    driver.find_element_by_class_name('input-xlarge').clear()
    
    driver.find_element_by_id('inputVarTcm').send_keys('浙贝母')
    
    driver.find_element_by_id('searchBtTcm').click()
    
    
    #下面是模拟登陆的页面
    driver.find_element_by_name('Username').clear()   #清除用户名字
    driver.find_element_by_name('Username').send_keys('marina')#输入用户名
    driver.find_element_by_name('Password').clear()   #清除用户密码
    driver.find_element_by_name('Password').send_keys('han#1990@yan')#输入用户密码
    driver.find_element_by_name('login').click()   #点击登陆
    #文本检索数据信息
    driver.find_element_by_link_text('中药药材检索').click()
    #driver.find_element_by_link_text('中药药材检索').get_attribute("href") 这部分的数据主要是为了
    #获取到中药药材检索对应的href数据,其实不一定是为了获取到这些数据,还可以直接click来跳转到对应的网页
    
    driver.find_element_by_name('Specname').clear()
    driver.find_element_by_name('Specname').send_keys(drugname)
    driver.find_element_by_id('submit1').click()
    driver.find_element_by_name('FID').click()