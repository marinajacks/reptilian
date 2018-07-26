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
  
      
#主函数
if __name__ == '__main__':
 
    url = "http://search.cnki.net/Search.aspx?q=浙贝母&rank=relevant&cluster=all&val=&p=0"
    path='D:\\project\\selenium\\geckodriver'
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url)
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