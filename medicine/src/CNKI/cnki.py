# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:15:39 2018

@author: hello
这个项目主要是用来进行pdf文本解析的方式进行的。本文的应该是有两个部分组成的,分别是文本的
下载和文本的解析,文本的下载主要是文本
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



def downloads(name):
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd://CNKI//'}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\v40\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    url='http://cnki.net/'
    driver.get(url)
    driver.switch_to_window(driver.window_handles[1])
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    #首先要做的是查找到文件的标题,根据文章的题目进行搜索,这里主要是进行查询药材的操作
    driver.find_element_by_id("txt_SearchText")
    driver.find_element_by_id("txt_SearchText").clear()
    driver.find_element_by_id("txt_SearchText").send_keys(name)
    driver.find_element_by_id("txt_SearchText").send_keys(Keys.ENTER)
    

    driver.switch_to_frame('iframeResult')
    s1=driver.find_element_by_class_name('GridTableContent')
    s2=s1.find_element_by_tag_name('tbody')
    s3=s2.find_elements_by_tag_name('tr')
    
    s3[1].find_elements_by_tag_name('td')[1].find_element_by_tag_name('a').click()
    driver.switch_to_window(driver.window_handles[1])
    driver.find_element_by_id('pdfDown').click()
    driver.close()
    driver.switch_to_window(driver.window_handles[0]) 
    
    for i in range(1,len(s3)):
        s1=driver.find_element_by_class_name('GridTableContent')
        s2=s1.find_element_by_tag_name('tbody')
        s3=s2.find_elements_by_tag_name('tr')
        s3[i].find_elements_by_tag_name('td')[1].find_element_by_tag_name('a').click()
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_id('pdfDown').click()
        driver.close()
        driver.switch_to_window(driver.window_handles[0]) 
        time.sleep(2)

