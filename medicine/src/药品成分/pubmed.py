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
from sqlalchemy import create_engine
from TCMSP import getbyInChIKey



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
    
#这个函数主要是为了获取到化合物的3D结构并将其下载到本地,这里选择下载的都是3D的结构
#    name='trans-feruloylcampesterol'
def SDFS(name):
    options = webdriver.ChromeOptions()
    downloads='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\3D'
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': downloads}
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
#下面的函数是事先获取到对应的页面的url信息，然后直接进行点击下载操作，便于批量作业，
#这里选择下载的都是3D的结构
def SDFS1(url):
    options = webdriver.ChromeOptions()
    downloads='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\3D'
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': downloads}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    driver.get(url)
    time.sleep(2)
    value=driver.find_element_by_id('3D-Conformer')  #这个找到对应的3D的位置
    value.find_elements_by_class_name('menu-btn')[1].click()  #这个是点击下载操作部分
    driver.find_element_by_link_text('Save').click() #这一部分模拟点击下载操作，进行下载
    
#这个函数同样是下载药品成分的一串url，对这些给定的url页面进行对应的下载操作
#,这里选择下载的都是3D的结构
def SFDS_3D(urls):
    options = webdriver.ChromeOptions()
    downloads='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\3D'
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': downloads}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    for url in urls:
        driver.get(url)
        print(url)
        time.sleep(2)
        test=driver.find_elements_by_id('3D-Conformer')  #这个找到对应的3D的位置,用来判断是不是存在3D结构
        if(len(test)>0):
            value=driver.find_element_by_id('3D-Conformer')  #这个找到对应的3D的位置
            #下面的脚本可以稍作修改
            value.find_elements_by_class_name('menu-btn')[1].click()  #这个是点击下载操作部分 
            driver.find_element_by_link_text('Save').click() #这一部分模拟点击下载操作，进行下载
            print('Success!')
        else:
            print('No 3D Conformer')
            
#这个函数同样是下载药品成分的一串url，对这些给定的url页面进行对应的下载操作
#,这里选择下载的都是3D的结构
def SFDS_3D_TCMID(urls):
    options = webdriver.ChromeOptions()
    downloads='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\TCMID_1'
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': downloads}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    #modules=[]
    for url in urls:
        driver.get(url)
        print(url)
        time.sleep(3)
        test=driver.find_elements_by_id('3D-Conformer')  #这个找到对应的3D的位置,用来判断是不是存在3D结构
        if(len(test)>0):
            ''' 
            module=[]
            pubchemcid=driver.find_element_by_tag_name('tbody').find_element_by_tag_name('td').text
             #下面的脚本可以稍作修改
            '''
            value=driver.find_element_by_id('3D-Conformer')  #这个找到对应的3D的位置
            time.sleep(2)
            value.find_elements_by_class_name('menu-btn')[1].click()  #这个是点击下载操作部分 
            driver.find_element_by_link_text('Save').click() #这一部分模拟点击下载操作，进行下载
            print('Success!')
            '''module.append(url[1])
            module.append(url[2])
            module.append(pubchemcid)
            modules.append(module)
            '''
        else:
            print('No 3D Conformer')
    #return modules
#这个函数同样是下载药品成分的一串url，对这些给定的url页面进行对应的下载操作
#,这里选择下载的都是3D的结构
def SFDS_2D(urls):
    options = webdriver.ChromeOptions()
    downloads='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\TCMID_2D_1'
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': downloads}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('disable-infobars')
    path='D:\\project\\selenium\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    for url in urls:
        driver.get(url)
        print(url,end=' ')
        time.sleep(2)
        test=driver.find_elements_by_id('2D-Structure')  #这个找到对应的3D的位置,用来判断是不是存在3D结构
        if(len(test)>0):
            value=driver.find_element_by_id('2D-Structure')  #这个找到对应的2D的位置
            value.find_elements_by_class_name('menu-btn')[1].click()  #这个是点击下载操作部分
            driver.find_element_by_link_text('Save').click() #这一部分模拟点击下载操作，进行下载
            print('Success!')
        else:
             print('No 2D Structure')

'''   
该函数主要是将上述部分信息合并起来,然后再查询的这样一个脚本,这个脚本
可以完全进行全部的搜索任务，有一个小点需要注意的就是这里还需要进行进一步
的修改,确保能够实现可以动态输入或者是文本的方式导入对应的数据。
'''
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

#这个脚本主要是为了处理给定的一个list数据，然后得到smiles
def SMILES(modules):
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
        
    #这里比较有意思的是,不同的数据对应的数据是不一样的,有些成分需要使用rsltcont
    #来进行定位，但是有些成分的获取则需要使用section-content来进行判断
    return drugs   

def PubChemCIDS(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    Keys=[]
    for name in modules:
        Key=[]
        Key.append(name)
        print(name)
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
        time.sleep(1)
        test=driver.find_elements_by_id('Canonical-SMILES') #确定是不是只有一个页面
        if(len(test)==1):
            Key.append(driver.find_element_by_tag_name('tbody').find_element_by_tag_name('td').text)
            Keys.append(Key)
            print('单页面')
        else:
            value=driver.find_elements_by_class_name('rsltcont')
            if(len(value)>0):
                url1=value[0].find_element_by_tag_name('a').get_attribute("href")
                driver.get(url1)
                time.sleep(2)
                Key.append(driver.find_element_by_tag_name('tbody').find_element_by_tag_name('td').text)
                Keys.append(Key)
                print('多页面')
            else:
                print('无页面')
                pass
        #Keys.append(Key)
        url='https://www.ncbi.nlm.nih.gov/pccompound/'
        driver.get(url)
        time.sleep(1)
    driver.quit()
    return Keys



  

#该函数主要是为了将数据处理成list格式,方便进行循环读取
def module(excel):
    df=pd.read_excel(excel)
    module0=[]
    for i in range(len(df[['Molecule name']])):
        module0.append(df[['Molecule name']].loc[i].values[0])
    return module0

#这个函数用来获取药品成分对应的Url信息，输入的参数是
def geturls(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    urls=[]
    for name in modules:
        urls0=[]
        driver.find_element_by_id('term').clear()
        driver.find_element_by_id('term').send_keys(name[0])
        driver.find_element_by_id('search').click()
        '''这里默认的是第一个地址就是我们需要的那个药品的成分信息
           下面首先需要获取到的就是第一条对应的数据，这里默认的就
           是第一条数据作为需要的数据也是合理的。但是这里存在一个
           问题，就是这里在选择结果的时间，查询结果可能是空的,所以,
           这里需要进行异常设计.另外,由于问题的种类至少有两种,所以,
           这里还需要首先判断是不是单一结果,如果是单一的结果,数据
           需要首先单独的跑出来,然后再继续判断其他的异常.
        '''
        time.sleep(1)
        test=driver.find_elements_by_id('Canonical-SMILES') #确定是不是只有一个页面
        if(len(test)==1):
            url1=driver.current_url
            urls0.append(url1)
            for j in name:
                urls0.append(j)
            urls.append(urls0)
            print('唯一页面',url1)
        else:
            value=driver.find_elements_by_class_name('rsltcont')
            if(len(value)>0):
                url1=value[0].find_element_by_tag_name('a').get_attribute("href")
                urls0.append(url1)
                for j in name:
                    urls0.append(j)
                urls.append(urls0)
                print('多页面',url1)
            else:
                print('无页面')
                pass
        url='https://www.ncbi.nlm.nih.gov/pccompound/'
        driver.get(url)
        time.sleep(1)
    driver.quit()
    return urls

#单独获取url
def geturl(module):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    driver.find_element_by_id('term').clear()
    driver.find_element_by_id('term').send_keys(module)
    driver.find_element_by_id('search').click()
    time.sleep(1)
    test=driver.find_elements_by_id('Canonical-SMILES') #确定是不是只有一个页面
    url1=[]
    if(len(test)==1):
        url1=driver.current_url
        print('唯一页面',url1)
    else:
        value=driver.find_elements_by_class_name('rsltcont')
        if(len(value)>0):
            url1=value[0].find_element_by_tag_name('a').get_attribute("href")
            print('多页面',url1)
        else:
            print('无页面')
            pass
    driver.quit()
    return url1
    
#这个函数同样是下载药品成分的一串url,获取到对应的成分的id信息，可以与成分的名称关联起来
#这个函数用来获取药品成分对应的Url信息，输入的参数是
def PubChemID(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    pubchems=[]
    for name in modules:
        pubchem=[]
        pubchem.append(name)
        print(name)
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
        time.sleep(1)
        test=driver.find_elements_by_id('Canonical-SMILES') #确定是不是只有一个页面
        if(len(test)==1):
            url1=driver.current_url
            print('唯一页面',url1)
            pubchem.append(url1.split('/')[-1])
        else:
            value=driver.find_elements_by_class_name('rsltcont')
            if(len(value)>0):
                url1=value[0].find_element_by_tag_name('a').get_attribute("href")
                print('多页面',url1)
                pubchem.append(url1.split('/')[-1])
            else:
                print('无页面')
                pubchem.append([])
                pass
        pubchems.append(pubchem)
        url='https://www.ncbi.nlm.nih.gov/pccompound/'
        driver.get(url)
        time.sleep(1)
    driver.quit()
    return pubchems

#这个函数同样是下载药品成分的一串url,获取到对应的成分的id信息，可以与成分的名称关联起来
#这个函数用来获取药品成分对应的Url信息，输入的参数是
def InChIKeys(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    Keys=[]
    for name in modules:
        Key=[]
        Key.append(name)
        print(name)
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
        time.sleep(1)
        test=driver.find_elements_by_id('InChI-Key') #确定是不是只有一个页面
        if(len(test)==1):
            s1=driver.find_element_by_id('InChI-Key')
            Key.append(s1.find_element_by_class_name('section-content-item').text)
            Keys.append(Key)
            print('单页面')
        else:
            value=driver.find_elements_by_class_name('rsltcont')
            if(len(value)>0):
                url1=value[0].find_element_by_tag_name('a').get_attribute("href")
                driver.get(url1)
                time.sleep(2)
                s1=driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
                time.sleep(1)
                for j in range(len(s1)):
                    tagname=s1[j].find_element_by_tag_name('th').text
                    #print(tagname)
                    if('InChI' in tagname):
                        Tag=j
                time.sleep(1)
                Key.append(s1[Tag].find_element_by_tag_name('td').text)
                Keys.append(Key)
                print('多页面')
            else:
                print('无页面')
                pass
        #Keys.append(Key)
        url='https://www.ncbi.nlm.nih.gov/pccompound/'
        driver.get(url)
        time.sleep(1)
    driver.quit()
    return Keys

def InChIKey(name):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    Key=[]
    print(name)
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
    time.sleep(1)
    test=driver.find_elements_by_id('InChI-Key') #确定是不是只有一个页面
    if(len(test)==1):
        s1=driver.find_element_by_id('InChI-Key')
        Key=s1.find_element_by_class_name('section-content-item').text
        print('单页面')
    else:
        value=driver.find_elements_by_class_name('rsltcont')
        if(len(value)>0):
            url1=value[0].find_element_by_tag_name('a').get_attribute("href")
            driver.get(url1)
            time.sleep(1)
            s1=driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
            for j in range(len(s1)):
                tagname=s1[j].find_element_by_tag_name('th').text
                if('InChI' in tagname):
                    Tag=j
            Key=s1[Tag].find_element_by_tag_name('td').text
            print('多页面')
        else:
            print('无页面')
            pass
    driver.quit()
    return Key

    
def writebase(table,data):
    #这里的table是表名称，data是数据，本质上是一个
    engine = create_engine("mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4".format('root', '', 'localhost:3306', 'ecnu'))
    con = engine.connect()
    df=pd.DataFrame(data)
    df.to_sql(name=table, con=con, if_exists='append', index=False)
            
            

if __name__=="__main__":
    #name=input("输入药品成分名字:")
    #mains1(name)
    #下面的操作主要还是把对应的三种药品的成分数据搞出来，然后存在特定的数据里
    path1='D:\MarinaJacks\project\\reptilian\medicine\中药数据\TCMSP\薏苡仁\薏苡仁.xlsx'
    path2='D:\MarinaJacks\project\\reptilian\medicine\中药数据\TCMSP\浙贝母\浙贝母.xlsx'
    path3='D:\MarinaJacks\project\\reptilian\medicine\中药数据\TCMSP\三七\三七.xlsx'
    path4='D:\MarinaJacks\project\\reptilian\medicine\中药数据\TCMSP\龙血竭\龙血竭.xlsx'
    paths=[path1,path2,path3,path4]
    modules=[]
    for path in paths:
        for mole in module(path):
            value=[]
            value.append(mole)
            value.append(path.split('\\')[-2])
            modules.append(value)
            
    
    drugs=[]
    for i in modules:
        if(i not in drugs):
            drugs.append(i)
            
    #将数据写入到对应的        
    IDs=PubChemID(modules)
    
    Keys=[]
    for drug in drugs:
        Keys.append(InChIKey(drug))
    
    Keys=InChIKeys(drugs)
    
    Key=[]
    for i in range(len(Keys)):
        Key.append(Keys[i][1])
    
    Compounds=getbyInChIKey(Keys)
    
    
    Compounds=[]
    for i in Key:
        Compounds.append(getbyInChIKey(i))
    longxuejie=[]
    for i in Compounds:
        if(len(i)>0):
            i.append('龙血竭')
            longxuejie.append(i)
            
    df1=pd.DataFrame(longxuejie)      
    
    path4='D:\MarinaJacks\project\\reptilian\medicine\Data\龙血竭成分.xlsx'   
    
    df1=pd.read_excel(path4)
    
    df2=pd.concat([df,df1])
    
           

    


    urls=geturls(modules1)

    names=[]
    for i in urls:
        name=[]
        name.append(i[0].split('/')[-1])
        for j in range(1,len(i)):
            name.append(i[j])
        names.append(name)
    
    path5='D:\MarinaJacks\project\\reptilian\medicine\Data\某种中药成分信息.xlsx'   
    df=pd.DataFrame(names)
    df.to_excel(path5)
    
    writebase('druginfos1',names)
    
    names=SFDS_3D_TCMID(urls)
    
    SFDS_2D(urls)
    writebase(table,data)
    
    


    
    
    