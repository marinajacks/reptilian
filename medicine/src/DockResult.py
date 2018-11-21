# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:21:01 2018

@author: hello
这个函数是对结果进行分析的脚本，对于对接的结果，这里进行分析数据，并且把数据处理到本地
"""
import pandas as pd
from selenium import webdriver


#这部分数据是为了进行解析结果数据而得到的 
path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\对接结果.xlsx'   
df=pd.read_excel(path1)
urls=[]
for i in range(len(df['结果地址'])):
    urls.append(df['结果地址'].iloc[i])


    url1='https://www.uniprot.org/'   #给定查询页面
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址
    driver = webdriver.Firefox(executable_path=path)
    try:
        driver.get(urls[0])
    except:
        driver.get(urls[0])
      
    try:
        driver.find_element_by_link_text('STEP 4').click()
    except ConnectionAbortedError:
        driver.find_element_by_link_text('STEP 4').click()
   
    results=driver.find_elements_by_class_name('dojoxGridRow')
    
  