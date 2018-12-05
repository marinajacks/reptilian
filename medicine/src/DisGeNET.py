# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:49:47 2018

@author: hello

这个程序可以对DisGeNET进行操作,获取到该数据库中的靶点数据并将数据下载到本地，下载
到本地使用的是excel格式，其实还可以使用其他相关的方式，例如存储到数据库里。
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import os

from selenium.webdriver.common.action_chains import ActionChains
import win32api
import win32con
#右键超链接另存为
ActionChains(driver).context_click(link).perform()
#延时2s
time.sleep(2)
#按下K键,这里用到了win32api,win32con
win32api.keybd_event(75,win32con.KEYEVENTF_KEYUP,0)#75的含义就是键盘的K




def downs(paths):
    if os.path.exists(paths):
        pass
    else:
        os.makedirs(paths) 
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    '''
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': paths}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\v40\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    '''
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
    link=driver.find_elements_by_class_name('controls')[1].find_element_by_name('download')
    ActionChains(driver).context_click(link).perform()

    
    for i,j,k in os.walk(paths):
        result=k
    return result
    

if __name__=="__main__":
    paths='D:\\apple'
    result=downs(paths)