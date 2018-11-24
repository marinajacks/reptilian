# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:49:47 2018

@author: hello

这个程序可以对DisGeNET进行操作,获取到该数据库中的靶点数据并将数据下载到本地，
下载到本地使用的是

"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import os

def downs(paths):
    if os.path.exists(paths):
        pass
    else:
        os.makedirs(paths) 
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': paths}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\v40\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    driver.get('http://www.disgenet.org/')
    driver.find_element_by_link_text('Search').click()
    
    driver.find_element_by_class_name('search').clear()
    driver.find_element_by_class_name('search').send_keys('Atherosclerosis')
    driver.find_elements_by_class_name('search')[1].click()
    time.sleep(5)
    driver.find_element_by_link_text('Top 10 gene associations for this disease').click()
    time.sleep(5)
    driver.find_element_by_partial_link_text('Browse details').click()
    time.sleep(20)
    driver.find_element_by_link_text('download').click()
    time.sleep(5)
    Select(driver.find_element_by_id('fileFormat')).select_by_value('1')
    driver.find_elements_by_class_name('controls')[1].find_element_by_name('download').click()
    for i,j,k in os.walk(paths):
        result=k
    return result
    
    
        
if __name__=="__main__":
    paths='D:\\apple'
    result=downs(paths)