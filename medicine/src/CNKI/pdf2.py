# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 20:45:14 2018

@author: hello
"""
from selenium import webdriver
from time import sleep
 
path='D:\\project\\selenium\\geckodriver'
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', 'd:\\迅雷下载')
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
 
driver = webdriver.Firefox(firefox_profile=profile,executable_path=path)
 
driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
sleep(3)
driver.quit()




# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:50:08 2018

@author: hello
"""

import time              
import re              
import sys    
import codecs    
import urllib   
from selenium import webdriver            
from selenium.webdriver.common.keys import Keys      
from time import sleep 
      
  
      
#主函数
if __name__ == '__main__':
    url='http://search.cnki.net/'
    path='D:\\project\\selenium\\geckodriver'
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.dir', 'd:\\')
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False) 
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')

    driver = webdriver.Firefox(executable_path=path,firefox_profile=fp)
    driver.get(url)
    driver.find_element_by_id("txtSearchKey").clear()
    driver.find_element_by_id("txtSearchKey").send_keys("浙贝母")
    driver.find_element_by_id("btntijiao").click()
    driver.current_url
    
    #标题
    content = driver.find_elements_by_xpath("//div[@class='wz_content']/h3")
    #摘要
    abstracts = driver.find_elements_by_xpath("//div[@class='width715']")
    #出版杂志+年份
    other = driver.find_elements_by_xpath("//span[@class='year-count']/span[1]")
    mode = re.compile(r'\d+\.?\d*')
    #下载次数 被引次数
    num = driver.find_elements_by_xpath("//span[@class='count']")
 
    #获取内容
    i = 0
    for tag in content:
        print (tag.text)
        print (abstracts[i].text)
        print (other[i].get_attribute("title"))
        number = mode.findall(other[i].text)
        print (number[0]) #年份
        number = mode.findall(num[i].text)
        if len(number)==1: #由于存在数字确实 如(100) ()
            print (number[0])
        elif len(number)==2:
            print (number[0],number[1])
        print ('')
        
        i = i + 1
        tag.click()
        time.sleep(1)
    
    
 
    tag=content[8]
    tag.click()
    driver.switch_to_window(driver.window_handles[1])
    

    driver.find_element_by_link_text("PDF下载").click()
    sleep(3) 
    driver.quit()
    
    








