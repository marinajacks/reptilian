# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:21:01 2018

@author: hello
这个函数是对结果进行分析的脚本，对于对接的结果，这里进行分析数据，并且把数据处理到本地
"""
import pandas as pd
from selenium import webdriver
import time
import os
import urllib
from sqlalchemy import create_engine

#这个函数是为了下载    
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
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\Dock1'}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\v40\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
        
    path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\TCMSP对接IPs.xlsx'  
    df=pd.read_excel(path1)
    urls=[]


    for i in range(len(df['IP'])):
        urls.append(df['IP'].iloc[i])
        
    
    for url in urls:
        try:
            driver.get(url)
            time.sleep(3)
        except:
            driver.get(url)
            time.sleep(8)
            
        driver.find_element_by_class_name('gear').click()
        time.sleep(1)
        driver.find_element_by_link_text('Docking Results Grouped by Proteins').click()
        time.sleep(5)
    
    
def getdata():
    path='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\Dock1\\'
    for i,j,k in os.walk(path):
            file=k       
    paths=[]
    for l in file:
        paths.append(path+l)
    return paths
    
        
def writebase(paths):
    engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format('root', '', 'localhost:3306', 'ecnu'))
    con = engine.connect()
    df1=pd.read_csv(paths[0])
   # df1.to_sql(name='result1', con=con, if_exists='append', index=False)
    for i in range(1,len(paths)):
        df=pd.read_csv(paths[i])
        df1=pd.concat([df1,df])#每次做一个
        #df.to_sql(name='result1', con=con, if_exists='append', index=False)
    return df1
        
    
if __name__=="__main__":
    #path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\TCMID对接结果.xlsx' 
   # downloads(path1)
    tables()
    #paths=getdata()
   # writebase(paths)
   # tables()
    paths=getdata()
    df1=writebase(paths)