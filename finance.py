#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:22:34 2018

@author: macbook
"""

import requests

from selenium import webdriver

from bs4 import BeautifulSoup  
import time


def test():
    url='http://fund.eastmoney.com/data/hbxfundranking.html#t;c0;r;s1yzf;ddesc;pn50;mg;os1;'
    
    url="https://www.anjuke.com/ks/cm608524-p2/#filtersort"


    path='/Users/macbook/downloads/geckodriver'
        
    driver = webdriver.Firefox(executable_path =path)
        
    driver.get(url)
       
    
    s1=driver.find_elements_by_class_name('infos')
    s2=driver.find_elements_by_class_name('cbook-price')

    
    
    s=driver.find_element_by_id("pagebar").find_element_by_class_name('end')
    
    driver.find_element_by_class_name('end')
    
    s[0].click()


if __name__ == "main":
    test()
    
    import requests 
    url='https://kyfw.12306.cn/otn/resources/js/query/train_list.js?scriptVersion=1.0'
    s=requests.get(url)
    path='/Users/macbook/downloads/test.txt'
    f=open(path,encoding='utf-8')
    f.write(str(s))
