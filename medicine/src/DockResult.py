# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:21:01 2018

@author: hello
这个函数是对结果进行分析的脚本，对于对接的结果，这里进行分析数据，并且把数据处理到本地
"""
import pandas as pd
from selenium import webdriver
import time
import urllib

def mains():
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
        
    '''
    try:
        results=driver.find_elements_by_tag_name('tbody')
        print(len(results))
    except ConnectionAbortedError:
        results=driver.find_elements_by_tag_name('tbody')
        print(len(results))
    '''
    
    #找到图片并下载
    a=driver.find_element_by_id('vinaChartImage').get_attribute('src')
    
    urllib.request.urlretrieve(a, 'D:\\图片\\a.jpg')
    
    driver.find_element_by_id('resultTabContainer').find_element_by_id('dojox_grid_EnhancedGrid_0')
    #页面分析的时候，这里发现的情况是，每次只能定位到25个框子，所以这里要分析到底应该怎么定位所有的框子
def downloads(path1):
    #path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\TCMID对接结果.xlsx'   
    df=pd.read_excel(path1)
    urls=[]
    names=[]

    for i in range(len(df['IP'])):
        urls.append(df['IP'].iloc[i])
        names.append(df['注释'].iloc[i].split('\'')[1].replace('-','_'))

    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址
    driver = webdriver.Firefox(executable_path=path)

    for i in range(len(urls)):
        try:
            driver.get(urls[i])
            time.sleep(3)
        except:
            driver.get(urls[i])
            time.sleep(8)
          
        try:
            driver.find_element_by_link_text('STEP 4').click()
            time.sleep(5)
        except ConnectionAbortedError:
            driver.find_element_by_link_text('STEP 4').click()
            time.sleep(10)
         
        try:
            a=driver.find_element_by_id('vinaChartImage').get_attribute('src')
        except ConnectionAbortedError:
            a=driver.find_element_by_id('vinaChartImage').get_attribute('src')
            
            
        path2='D:\\图片\\'+names[i]+'.jpg'
        urllib.request.urlretrieve(a, path2)
        time.sleep(5)
        print('页面下载成功')
        
        
def tables():
    path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\TCMID对接结果.xlsx'  
    df=pd.read_excel(path1)
    urls=[]


    for i in range(len(df['IP'])):
        urls.append(df['IP'].iloc[i])
     

    path='D:\project\selenium\geckodriver'
    driver = webdriver.Firefox(executable_path=path)
    
    try:
        driver.get(urls[0])
        time.sleep(3)
    except:
        driver.get(urls[0])
        time.sleep(8)



    for i in range(len(urls)):
        try:
            driver.get(urls[i])
            time.sleep(3)
        except:
            driver.get(urls[i])
            time.sleep(8)
          
        try:
            driver.find_element_by_link_text('STEP 4').click()
            time.sleep(5)
        except ConnectionAbortedError:
            driver.find_element_by_link_text('STEP 4').click()
            time.sleep(10)
         
        try:
            a=driver.find_element_by_id('vinaChartImage').get_attribute('src')
        except ConnectionAbortedError:
            a=driver.find_element_by_id('vinaChartImage').get_attribute('src')
            
            
        path2='D:\\图片\\'+names[i]+'.jps'
        urllib.request.urlretrieve(a, path2)
        time.sleep(5)
        print('页面下载成功')
    
    
        
        
def test():
    results=driver.find_elements_by_tag_name('tbody')
    results1=driver.find_elements_by_class_name('dojoxGridCell ')
    for i in range(len(results1)):
        print(results1[i].text,'',i)
    
    for tbody in results:
        trs=tbody.find_elements_by_tag_name("tr")
        for tr in trs:
            td=tr.find_elements_by_tag_name("td")
            time.sleep(1)
            for i in td:
                print(i.text.strip(),end='\t')
            print('\n')            
    
if __name__=="__main__":
    path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\TCMID对接结果.xlsx' 
    downloads(path1)