# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:12:12 2018

@author: hello
"""



import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import os



    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.uniprot.org/uniprot/P03956'
    driver.get(url)
    
    s=driver.find_element_by_id('structure')
    s1=s.find_elements_by_id('structureFrame')
    
    s1=driver.find_element_by_id('structureFrame')
    
    
    driver.find_element_by_tag_name('tr')
    s1.find_element_by_tag_name('body')
    
    #查找对应的某一行元素
    s2=s1.find_element_by_xpath('//body')
    
    s3=s2.find_elements_by_xpath('//table')
    
    
    tbody=s3[0].find_elements_by_xpath('//table/tbody')
    
    driver.find_elements_by_xpath('//html/body//div/div/table/tbody')
    
    
    
    trs=tbodys.find_elements_by_tag_name("tr")
    
    tr=trs[0].find_elements_by_xpath('//td')


    s1.find_element_by_xpath('//body/*/div/div/table/tbody')
    

    for i in tr:
        print(i.text)
    
    for tr in trs:
        td=tr.find_elements_by_tag_name("td")[1]
        href=td.find_element_by_tag_name("a").get_attribute("href")
        hrefs.append(href)
    
    #s1.find_element_by_class_name('main-container')
    
