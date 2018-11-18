# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:58:22 2018

@author: hello
在进行小分子数据的获取的时候,其实主要需要弄的就是小分子的SMILES结构信息,
但是，前期实际上需要把原先给定的数据读取到对应的名称，然后从相应的数据库
中找到对应的SMILES结构信息。
"""

import requests as res 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import os



#这部分函数主要是用来进行获取到对应的SMILES数据的程序段
def test(url):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://pubchem.ncbi.nlm.nih.gov/compound/11005'
    driver.get(url)
    s1=driver.find_element_by_id('Canonical-SMILES')
    smiles=s1.find_element_by_class_name('section-content-item').text
    return smiles
    
    

#这部分的函数主要是为了查询化合物相关的信息。
def smiles():
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    driver.find_element_by_id('term').clear()
    driver.find_element_by_id('term').send_keys("myristic acid")
    driver.find_element_by_id('search').click()
    
#这个函数主要是为了获取到化合物的3D结构并将其下载到本地
#    name='trans-feruloylcampesterol'
def SDFS(name):
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\CNKI'}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)

    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    driver.find_element_by_id('term').clear()
    driver.find_element_by_id('term').send_keys(name)
    driver.find_element_by_id('search').click()
    
    #这里默认的是第一个地址就是我们需要的那个药品的成分信息
    #下面首先需要获取到的就是第一条对应的数据，这里默认的就
    #是第一条数据作为需要的数据也是合理的。
    value=driver.find_element_by_id('3D-Conformer')  #这个找到对应的3D的位置
    value.find_elements_by_class_name('menu-btn')[1].click()  #这个是点击下载操作部分
    driver.find_element_by_link_text('Save').click() #这一部分模拟点击下载操作，进行下载
    
    url='https://pubchem.ncbi.nlm.nih.gov/compound/13786591'
#下面的函数是事先获取到对应的页面的url信息，然后直接进行点击下载操作，便于批量作业
def SDFS1(url):
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\CNKI'}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    driver.get(url)
    time.sleep(2)
    value=driver.find_element_by_id('3D-Conformer')  #这个找到对应的3D的位置
    value.find_elements_by_class_name('menu-btn')[1].click()  #这个是点击下载操作部分
    driver.find_element_by_link_text('Save').click() #这一部分模拟点击下载操作，进行下载
    
#该函数主要是将上述部分信息合并起来,然后再查询的这样一个脚本,这个脚本
#可以完全进行全部的搜索任务，有一个小点需要注意的就是这里还需要进行进一步
#的修改,确保能够实现可以动态输入或者是文本的方式导入对应的数据。
def mains():
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    driver.find_element_by_id('term').clear()
    driver.find_element_by_id('term').send_keys("myristic acid")
    driver.find_element_by_id('search').click()
    #这里默认的是第一个地址就是我们需要的那个药品的成分信息
    #下面首先需要获取到的就是第一条对应的数据，这里默认的就
    #是第一条数据作为需要的数据也是合理的。
    value=driver.find_element_by_class_name('rsltcont') 
    url1=value.find_element_by_tag_name('a').get_attribute("href")
    driver.get(url1)
    time.sleep(0.5)
    s1=driver.find_element_by_id('Canonical-SMILES')
    smiles=s1.find_element_by_class_name('section-content-item').text
    print(smiles)


#这个程序可以根据输入的名称数据找到对应的SMILES结构
def  mains1(name):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    driver.find_element_by_id('term').clear()
    driver.find_element_by_id('term').send_keys(name)
    driver.find_element_by_id('search').click()
    #这里默认的是第一个地址就是我们需要的那个药品的成分信息
    #下面首先需要获取到的就是第一条对应的数据，这里默认的就
    #是第一条数据作为需要的数据也是合理的。
    value=driver.find_element_by_class_name('rsltcont') 
    url1=value.find_element_by_tag_name('a').get_attribute("href")
    driver.get(url1)
    time.sleep(0.5)
    s1=driver.find_element_by_id('Canonical-SMILES')
    smiles=s1.find_element_by_class_name('section-content-item').text
    print(smiles)
    
    
def mains2(name):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    driver.find_element_by_id('term').clear()
    driver.find_element_by_id('term').send_keys(name)
    driver.find_element_by_id('search').click()
    '''这里默认的是第一个地址就是我们需要的那个药品的成分信息
       下面首先需要获取到的就是第一条对应的数据，这里默认的就
       是第一条数据作为需要的数据也是合理的。但是这里存在一个
       问题，就是这里在选择结果的时间，查询结果可能是空的,所以,
       这里需要进行异常设计.
    '''
    try:
        value=driver.find_element_by_class_name('rsltcont')
        url1=value.find_element_by_tag_name('a').get_attribute("href")
        driver.get(url1)
        time.sleep(0.5)
        s1=driver.find_element_by_id('Canonical-SMILES')
        smiles=s1.find_element_by_class_name('section-content-item').text
        print(smiles)
    except NoSuchElementException as msg:
        smiles=None
#        pass
    #这里比较有意思的是,不同的数据对应的数据是不一样的,有些成分需要使用rsltcont
    #来进行定位，但是有些成分的获取则需要使用section-content来进行判断
  
   
     


        #print (u"查找元素异常%s"%msg)
    return smiles
   
 
def mains3(name):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    driver.find_element_by_id('term').clear()
    driver.find_element_by_id('term').send_keys(name)
    driver.find_element_by_id('search').click()
    '''这里默认的是第一个地址就是我们需要的那个药品的成分信息
       下面首先需要获取到的就是第一条对应的数据，这里默认的就
       是第一条数据作为需要的数据也是合理的。但是这里存在一个
       问题，就是这里在选择结果的时间，查询结果可能是空的,所以,
       这里需要进行异常设计.另外,由于问题的种类至少有两种,所以,
       这里还需要首先判断是不是单一结果,如果是单一的结果,数据
       需要首先单独的跑出来,然后再继续判断其他的异常.
    '''
    try:
        s1=driver.find_element_by_id('Canonical-SMILES')
        smiles=s1.find_element_by_class_name('section-content-item').text
    except NoSuchElementException as msg:
        try:
            value=driver.find_element_by_class_name('rsltcont')
            url1=value.find_element_by_tag_name('a').get_attribute("href")
            driver.get(url1)
            time.sleep(0.5)
            s1=driver.find_element_by_id('Canonical-SMILES')
            smiles=s1.find_element_by_class_name('section-content-item').text
        except NoSuchElementException as msg:
            smiles=None
        smiles=None
#        pass
    #这里比较有意思的是,不同的数据对应的数据是不一样的,有些成分需要使用rsltcont
    #来进行定位，但是有些成分的获取则需要使用section-content来进行判断
    return smiles   

#这个脚本主要是为了处理给定的一个list数据，然后
def mains4(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    drugs=[]
    for name in modules:
        driver.find_element_by_id('term').clear()
        driver.find_element_by_id('term').send_keys(name)
        driver.find_element_by_id('search').click()
        '''这里默认的是第一个地址就是我们需要的那个药品的成分信息
           下面首先需要获取到的就是第一条对应的数据，这里默认的就
           是第一条数据作为需要的数据也是合理的。但是这里存在一个
           问题，就是这里在选择结果的时间，查询结果可能是空的,所以,
           这里需要进行异常设计.另外,由于问题的种类至少有两种,所以,
           这里还需要首先判断是不是单一结果,如果是单一的结果,数据
           需要首先单独的跑出来,然后再继续判断其他的异常.
        '''
        try:
            s1=driver.find_element_by_id('Canonical-SMILES')
            smiles=s1.find_element_by_class_name('section-content-item').text
        except NoSuchElementException as msg:
            try:
                value=driver.find_element_by_class_name('rsltcont')
                url1=value.find_element_by_tag_name('a').get_attribute("href")
                driver.get(url1)
                time.sleep(1)
                s1=driver.find_element_by_id('Canonical-SMILES')
                smiles=s1.find_element_by_class_name('section-content-item').text
            except NoSuchElementException as msg:
                smiles=None
           
        drugs.append(smiles)
        print(drugs)
        url='https://www.ncbi.nlm.nih.gov/pccompound/'
        driver.get(url)
        time.sleep(1)
        
#        pass
    #这里比较有意思的是,不同的数据对应的数据是不一样的,有些成分需要使用rsltcont
    #来进行定位，但是有些成分的获取则需要使用section-content来进行判断
    return drugs   
    

#该函数主要是为了将数据处理成list格式,方便进行循环读取
def module(excel):
    df=pd.read_excel(excel)
    module=[]
    for i in range(len(df[['Molecule name']])):
        module.append(df[['Molecule name']].loc[i].values[0])
    return module
    

if __name__=="__main__":
    name=input("输入药品成分名字:")
    #mains1(name)
   # path='D:\MarinaJacks\project\\reptilian\medicine\中药数据\TCMSP\浙贝母\浙贝母.xlsx'
   # modules=module(path)
    drugs=mains3(name)
    #mains3(name)