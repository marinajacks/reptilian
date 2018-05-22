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
    
    path='/Users/macbook/downloads/geckodriver'
        
    driver = webdriver.Firefox(executable_path =path)
        
    driver.get(url)
       
    s=driver.find_element_by_id("pagebar").find_element_by_class_name('end')
    
    driver.find_element_by_class_name('end')
    
    s[0].click()


if __name__ == "main":
    test()
    