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
      



def is_element_exist(text):
    s = driver.find_elements_by_link_text(text)
    if len(s) == 0:
        print ("元素未找到:%s"%text)
        return False
    elif len(s) == 1:
        return True
    else:
        print ("找到%s个元素：%s"%(len(s),text))
        return False
    
      
#主函数
if __name__ == '__main__':
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.dir', 'd:\\迅雷下载')
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    
    url='http://nvsm.cnki.net/'
    path='D:\\project\\selenium\\geckodriver'
    driver = webdriver.Firefox(executable_path=path,firefox_profile=profile)
    
    driver.get(url)
    driver.find_element_by_id("txt_SearchText").clear()
    driver.find_element_by_id("txt_SearchText").send_keys("网络药理学")
    driver.find_element_by_class_name("search-btn").click()
    driver.current_url
    
    #url = "http://search.cnki.net/Search.aspx?q=浙贝母&rank=relevant&cluster=all&val=&p=0"
    #path='D:\\project\\selenium\\geckodriver'
    #driver = webdriver.Firefox(executable_path=path)
    #driver.get(url)
    
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
    
    
 
    tag=content[7]
    tag.click()
    driver.switch_to_window(driver.window_handles[1])
    
    if is_element_exist("整本下载"):
        driver.find_element_by_link_text("整本下载").click()
    elif is_element_exist("CAJ下载"):
        driver.find_element_by_link_text("CAJ下载").click()
    elif is_element_exist("PDF下载"):
        driver.find_element_by_link_text("PDF下载").click()
        
    driver.switch_to_window(driver.window_handles[0])    

    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.dir', 'd:\\迅雷下载')
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False) 
    driver.find_element_by_link_text("整本下载").click()
    sleep(3) 
    driver.quit()
    
    

    #实例化一个火狐配置文件
    fp = webdriver.FirefoxProfile()
    
    
    #设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。
    
    #设置成0代表下载到浏览器默认下载路径；设置成2则可以保存到指定目录
    fp.set_preference("browser.download.folderList",2)
    
    
    #是否显示开始,(个人实验，不管设成True还是False，都不显示开始，直接下载)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    
    
    #下载到指定目录
    fp.set_preference("browser.download.dir","d:\\迅雷下载")
    
    
    #不询问下载路径；后面的参数为要下载页面的Content-type的值
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")
    
    
    #启动一个火狐浏览器进程，以刚才的浏览器参数
    driver = webdriver.Firefox(executable_path=path,firefox_profile=fp)
    






