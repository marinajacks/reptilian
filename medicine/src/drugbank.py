# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:17:04 2018

@author: hello
这个脚本用来使用drugbank来进行药品成分的查询
"""

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys  
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import time

def test():
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.drugbank.ca/'
    driver.get(url)
    #模拟查询药物的相关操作
    herb='nonanoic acid'
    driver.find_element_by_id("query").clear()
    driver.find_element_by_id("query").send_keys(herb)
    driver.find_element_by_id('searcher_drugs').send_keys(Keys.ENTER)
    driver.find_element_by_class_name('hit-link').click()
    '''#这里使用的方法与上面使用click()得到的效果是一样的。
    href=driver.find_element_by_class_name('hit-link')
    url=href.find_element_by_tag_name('a').get_attribute('href')
    '''
    s=driver.find_element_by_tag_name('dl')
    s.find_elements_by_tag_name('dd')[-1].text
    
    
def smiles(com):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.drugbank.ca/'
    driver.get(url)
    #模拟查询药物的相关操作
    driver.find_element_by_id("query").clear()
    driver.find_element_by_id("query").send_keys(com)
    driver.find_element_by_id('searcher_drugs').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_class_name('hit-link').click()
    '''#这里使用的方法与上面使用click()得到的效果是一样的。
    href=driver.find_element_by_class_name('hit-link')
    url=href.find_element_by_tag_name('a').get_attribute('href')
    '''
    time.sleep(1)
    s=driver.find_element_by_tag_name('dl')
    smiles=s.find_elements_by_tag_name('dd')[-1].text
    return smiles

def batch_smiles(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.drugbank.ca/'
    driver.get(url)
    drugs=[]
    #模拟查询药物的相关操作
    for com in modules:
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys(com)
        time.sleep(1)
        driver.find_element_by_id('searcher_drugs').send_keys(Keys.ENTER)
        time.sleep(1)
        try:
            driver.find_element_by_class_name('hit-link').click()
            '''#这里使用的方法与上面使用click()得到的效果是一样的。
            href=driver.find_element_by_class_name('hit-link')
            url=href.find_element_by_tag_name('a').get_attribute('href')
            '''
            time.sleep(1)
            s=driver.find_element_by_tag_name('dl')
            smiles=s.find_elements_by_tag_name('dd')[-1].text
            drugs.append(smiles)
            print(smiles)
        except NoSuchElementException as msg:
            drugs.append(None)
            print(None)
         
        url1='https://www.drugbank.ca/'
        driver.get(url1)
        time.sleep(1)
        
    return drugs
    
def module(excel):
    df=pd.read_excel(excel)
    module=[]
    for i in range(len(df[['Molecule name']])):
        module.append(df[['Molecule name']].loc[i].values[0])
    return module

if __name__=="__main__":
    #com=input('输入成分名称:')
   # smiles=smiles(com)
    
    path='D:\MarinaJacks\project\\reptilian\medicine\中药数据\TCMSP\浙贝母\浙贝母.xlsx'
    modules=module(path)
    drugs=batch_smiles(modules)
    