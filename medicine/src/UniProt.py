# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:12:12 2018

@author: hello
"""



import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import pandas as pd
import time
import os
import numpy as np



def sortpdbs(pdbs):
    '''
    这个函数用来排序爬虫获取到的PDB数据，选择Method为X-ray，同时按照Resolution (Å)
    从小到大的方式进行排序，返回排序后的数组，排序后的数组仅选择X-ray，同时仅有三个
    元素，分别是PDB entry、Method、Resolution (Å)。
    '''
    results=[]
    for pdb in pdbs:
       result=[]
       for i in range(3):
           #判断
           if('X-ray' not in pdb[1]):
               pass
           else:
               if(i==2):
                   result.append(pdb[i].split(' ')[0])
               else:
                   result.append(pdb[i])
       if(len(result)>1):
           results.append(result)
 
    results=np.array(results)
    results=results[np.lexsort(results.T)]
    return  results.tolist()

'''
下面的函数主要是为了定位页面获取到PDB数据
'''
def getpdbs(url):
    url='https://www.uniprot.org/uniprot/P08253'
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址
    driver = webdriver.Firefox(executable_path=path)
   # url='https://www.uniprot.org/uniprot/P03956'
    driver.get(url)
    #由于页面是iframe嵌套的子页面，所以这里需要选择子页面操作
    driver.switch_to_frame('structureFrame')
    #定位页面中的tbody的位置
    tbodys=driver.find_element_by_tag_name("tbody")
    trs=tbodys.find_elements_by_tag_name("tr")

    pdbs=[]
    for tr in trs:
        pdb=[]
        td=tr.find_elements_by_tag_name("td")
        for i in td:
            pdb.append(i.text.strip())
        pdbs.append(pdb)
        
    PDB=sortpdbs(pdbs)
    print(PDB)
    
    
    '''
下面的函数主要是为了定位页面获取到PDB数据
'''

def PDBS(Uniprots):
    url1='https://www.uniprot.org/uniprot/'
    urls=[]
    for i in Uniprots:
        urls.append(url1+i)
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\CNKI'}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\v40\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    driver.get('https://www.uniprot.org')
    ''' 这里使用的是火狐浏览器的效果，上面的是使用谷歌浏览器的效果
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址
    driver = webdriver.Firefox(executable_path=path)
    driver.get('https://www.uniprot.org')
    '''
    time.sleep(1)
    PDBS1=[]
    urls=urls[1:20]
    for url in urls:
        driver.get(url)
        time.sleep(1)
        print(url)
        #由于页面是iframe嵌套的子页面，所以这里需要选择子页面操作
        iframe=driver.find_elements_by_tag_name('iframe')
        if(len(iframe)>0):
            driver.switch_to_frame('structureFrame')
            #定位页面中的tbody的位置
            tbodys=driver.find_element_by_tag_name("tbody")
            trs=tbodys.find_elements_by_tag_name("tr")
        
            pdbs=[]
            for tr in trs:
                pdb=[]
                td=tr.find_elements_by_tag_name("td")
                for i in td:
                    pdb.append(i.text.strip())
                pdbs.append(pdb)
                
            PDB=sortpdbs(pdbs)
            print(PDB)
            
            PDBS1.append(PDB[0])
    
    driver.quit()
    return PDBS1

#下面的函数

def main(target):
    target='NGFR'
    url='https://www.uniprot.org/'   #给定查询页面
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址
    driver = webdriver.Firefox(executable_path=path)
   # url='https://www.uniprot.org/uniprot/P03956'
   
    driver.get(url)
    #下面的操作是为了查询特定靶点的数据
    driver.find_element_by_id('query').clear()
    driver.find_element_by_id('query').send_keys(target)
    #driver.find_element_by_id('query').send_keys(Keys.ENTER)
    driver.find_element_by_id('search-button').click()
    #这一步是选择Human的筛选
    
    time.sleep(1)
    driver.find_element_by_id("orgFilter-9606").click()
    time.sleep(1)
    #下面的是查询的结果
    s=driver.find_element_by_id('resultsArea')
    tbodys=s.find_element_by_tag_name('tbody')
    trs=tbodys.find_elements_by_tag_name("tr")
    #下面是为了获取到第一行查询的结果
    td=trs[0].find_elements_by_tag_name('td')
    
    #这是第二列的href数据
    url=td[1].find_element_by_tag_name("a").get_attribute("href")
    driver.quit()
    return  url


def getuniprot():
    path='D:/MarinaJacks/project/reptilian/medicine/Datas/Uniprot.txt'
    f=open(path,'r')
    lines=f.readlines()
    lists=[]
    for line in lines:
        uni=line.strip().split(';')[0]
        if(len(uni)>0):
            lists.append(uni)
    return lists
        
    
if __name__=="__main__":
    '''
    target='Beta-2 adrenergic receptor'
    url=main(target)
    getpdbs(url)
    '''
    Uniprots=getuniprot()
    PDBS1=PDBS(Uniprots)

    

