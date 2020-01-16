# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:34:58 2020
@author: hello
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:40:04 2020

@author: macbook
"""
import requests as res 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


def mols(name):
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\\MarinaJacks\学术研究\专利软著\中药研究\成分信息'}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\selenium\chromedriver.exe'  #mac环境下驱动地址
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    
    url='http://www.chemspider.com/'
    driver.get(url)
    
    driver.find_element_by_name("ctl00$ctl00$ContentSection$ContentPlaceHolder1$simpleSearch$simple_query").clear()
    driver.find_element_by_name("ctl00$ctl00$ContentSection$ContentPlaceHolder1$simpleSearch$simple_query").send_keys(name)
    driver.find_element_by_name('search_text_button').click()
    
    #driver.find_element_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_RecordViewDetails_rptDetailsView_ctl00_ThumbnailControl1_save").click()
        
    return driver

def tests():
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\CNKI'}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\selenium\chromedriver.exe'  #mac环境下驱动地址
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    
    url='http://www.chemspider.com/'
    driver.get(url)
    
    return driver

    
def mols1(driver,name):
    
    url='http://www.chemspider.com/'
    driver.get(url)
    time.sleep(10)
    driver.find_element_by_name("ctl00$ctl00$ContentSection$ContentPlaceHolder1$simpleSearch$simple_query").clear()
    driver.find_element_by_name("ctl00$ctl00$ContentSection$ContentPlaceHolder1$simpleSearch$simple_query").send_keys(name)
    time.sleep(10)
    driver.find_element_by_name("search_text_button").click()
    time.sleep(10)
    
    No0=driver.find_elements_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_ResultViewControl1_ResultStatementControl1_plhMessage")
    No1=driver.find_elements_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_ResultStatementControl1_plhMessage")
    
    if(len(No0)==1):
        print(name+' 无')
    elif(len(No1)==1):
        print(name+' 有')
        driver.find_element_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_RecordViewDetails_rptDetailsView_ctl00_ThumbnailControl1_save").click()
        time.sleep(10)        
        chemid=driver.find_elements_by_class_name("hide-below-desktop")[1].text
        chemid=chemid.split(' ')[1].replace('ID','')
        print(name+','+chemid)
        
        
        '''
        if(number==0):
            print(name+' 无')
        elif(number==1):
            driver.find_element_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_RecordViewDetails_rptDetailsView_ctl00_ThumbnailControl1_save").click()
            time.sleep(10)        
            chemid=driver.find_elements_by_class_name("hide-below-desktop")[1].text
            chemid=chemid.split(' ')[1].replace('ID','')
            print(name+','+chemid)
    '''
    else:
        print(name+' 有')
        time.sleep(10)
        page=driver.find_elements_by_tag_name("tr")[1].find_elements_by_tag_name("td")[0].find_element_by_tag_name("a").get_attribute('href')
        driver.get(page)
        time.sleep(10)
        driver.find_element_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_RecordViewDetails_rptDetailsView_ctl00_ThumbnailControl1_save").click()
        time.sleep(10)
        chemid=driver.find_elements_by_class_name("hide-below-desktop")[1].text
        chemid=chemid.split(' ')[1].replace('ID','')
        print(name+','+chemid)
    return driver


def nameed():
    path="D:\\MarinaJacks\学术研究\专利软著\中药研究\化合物名称.xlsx"
    
    df=pd.read_excel(path,sheet_name="合并数据")
    names=[]
 
    for i in range(len(df)):
        values=[]
        values.append(df.loc[i][0])
        values.append(df.loc[i][1])
        names.append(values)
      
    name=[]
    for i in names:
        if(i[1]!= "有" and i[1]!="无"):
            name.append(i)
    return name

def main(driver):
    names=nameed()
    for name in names[300:]:
        driver=mols1(driver,name[0])
        time.sleep(10)
    

if  __name__=="__main__":
    driver=tests()
    main(driver)

