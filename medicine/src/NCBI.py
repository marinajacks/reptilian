# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:20:42 2018

@author: hello
这个是为了获取到NCBI数据库中的靶点数据书写的脚本,可以
获取到靶点相关的数据,并且将其存储到本地的数据库中
"""

import requests as res 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import os



def test():
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/'
    driver.get(url)
    driver.find_element_by_name("term").clear()
    driver.find_element_by_name("term").send_keys("adenomyosis")
    driver.find_element_by_id('search').click()
    
    
    
    
    
    
    
    
    
if __name__=="__main__":
    test()