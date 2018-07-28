# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:37:44 2018

@author: hello
"""
import re      
from selenium import webdriver
import time
 
#这个函数用来判断是不是存在某个文本链接,如果不存在的话返回False,否则返回True
def is_element_exist(text):
    s = driver.find_elements_by_link_text(text)
    if len(s) == 0:
        print ("元素未找到:%s"%text)
        return False
    elif len(s) == 1:
        print("元素找到:%s"%text)
        return True
    else:
        print ("找到%s个元素：%s"%(len(s),text))
        return False
    
    
if __name__=="__main__":
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\CNKI'}
    options.add_experimental_option('prefs', prefs)
     
    driver = webdriver.Chrome(executable_path='D:\\project\\selenium\\chromedriver.exe', chrome_options=options)

    url='http://search.cnki.net/'
    driver.get(url)
    driver.find_element_by_id("txtSearchKey").clear()
    driver.find_element_by_id("txtSearchKey").send_keys("浙贝母")
    driver.find_element_by_id("btntijiao").click()
 
    n=10
    for j in range(n):
        #标题
        content = driver.find_elements_by_xpath("//div[@class='wz_content']/h3")
        #摘要
        abstracts = driver.find_elements_by_xpath("//div[@class='width715']")
        #出版杂志+年份
        other = driver.find_elements_by_xpath("//span[@class='year-count']/span[1]")
        mode = re.compile(r'\d+\.?\d*')
        #下载次数 被引次数
        num = driver.find_elements_by_xpath("//span[@class='count']")
        
        mainHandle = driver.current_window_handle  #获取当前的主页句柄
        
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
            time.sleep(0.5)
    
        #获取所有当前window handle
        allHandles = driver.window_handles 
        #对每个window handle,都设法获取到对应的文章下载信息
        for i in range(1,len(allHandles)):
            time.sleep(0.5)
            driver.switch_to_window(allHandles[i])
            if is_element_exist("整本下载"):
                driver.find_element_by_link_text("整本下载").click()
            elif is_element_exist("PDF下载"):
                driver.find_element_by_link_text("PDF下载").click()
            elif is_element_exist("CAJ下载"):
                driver.find_element_by_link_text("CAJ下载").click()
            else:
                pass
            time.sleep(0.5)
            driver.close()
            
        driver.switch_to_window(mainHandle)
        time.sleep(1)
        driver.find_element_by_link_text("下一页").click()
        time.sleep(1)
        
\    