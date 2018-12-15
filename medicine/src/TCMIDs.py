#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:55:08 2018

@author: macbook
这个部分主要是为了进行模拟登陆的操作,然后进行模拟控制的操作
这个部分的数据主要是TCMID里边的数据,后边的
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.common.exceptions import NoSuchElementException 
import time
import pandas as pd



def getdrug(drugname):
    #这个是通过模拟人的行为找到对应的药物的网页
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path=path)
    url='http://www.megabionet.org/tcmid/'
    driver.get(url)
    #模拟查询药物的相关操作
    url1=[drugname]
    driver.find_element_by_link_text('Search').click()
    driver.find_element_by_id('Channel12').click()
    driver.find_element_by_id('id_chinese_Name').clear()
    driver.find_element_by_id('id_chinese_Name').send_keys(drugname)
    #driver.current_window_handle #页面会发生跳转,这个命令用来将driver页面转换
    time.sleep(1)
    driver.find_element_by_id('id_chinese_Name').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.switch_to_window(driver.window_handles[1])
    try:
        driver.find_element_by_link_text(drugname).click()
        url1.append(driver.current_url)
    except NoSuchElementException:
        url1.append(driver.current_url)
    driver.quit()
    return url1

def Ingredient(url):
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url[-1])
    time.sleep(2)
    trs=driver.find_elements_by_tag_name('tbody')[1].find_elements_by_tag_name('tr')
    urls=[]
    for i in range(1,len(trs)):
        url0=[]
        for j in url:
            url0.append(j)
        molecule=trs[i].find_element_by_tag_name('td').find_element_by_tag_name('a').text
        locate=trs[i].find_element_by_tag_name('td').find_element_by_tag_name('a').get_attribute('href')
        url0.append(molecule)
        url0.append(locate)
        urls.append(url0)
    driver.quit()
    return urls

def molecules(urls):
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path=path)
    locates=[]
    for url in urls:
        url0=[]
        for j in url:
            url0.append(j)
        driver.get(url[-1])
        cid=driver.find_element_by_class_name('content').find_element_by_tag_name('a').text
        locate=driver.find_element_by_class_name('content').find_element_by_tag_name('a').get_attribute('href')
        url0.append(cid)
        url0.append(locate)
        locates.append(url0)
    driver.quit()
    return locates

def PubChemUrl(module):
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

#这个函数用来获取药品成分对应的Url信息，输入的参数是
def PubChemUrls(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/pccompound/'
    driver.get(url)
    urls=[]
    for name in modules:
        urls0=[]
        urls0.append(name)
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
            urls0.append(url1)
            print('唯一页面',url1)
        else:
            value=driver.find_elements_by_class_name('rsltcont')
            if(len(value)>0):
                url1=value[0].find_element_by_tag_name('a').get_attribute("href")
                urls0.append(url1)
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

def main(drugs):
    modules=[]
    for drugname in drugs:
        url=getdrug(drugname)
        urls=Ingredient(url)
        locates=molecules(urls)
        for i in locates:
            if(i[4]=='NA'):
                url0=PubChemUrl(i[2])
                if(url0==[]):
                    pass
                else:
                    i[4]=url0.split('/')[-1]
                    i[-1]=url0
                print(i)
        for locate in locates:
            modules.append(locate)
        print(drugname+' is success!')
    return modules
    

    
#该函数主要是为了将数据处理成list格式,方便进行循环读取
def module(excel):
    df=pd.read_excel(excel)
    module0=[]
    for i in range(len(df[['Molecule name']])):
        module0.append(df[['Molecule name']].loc[i].values[0])
    return module0


if __name__=='__main__':
    drugs=['ZHE BEI MU','SAN QI','YI YI REN']
    modules=main(drugs)
    
    #处理特殊的成分的操作
    path4='D:\MarinaJacks\project\\reptilian\medicine\中药数据\TCMSP\龙血竭\龙血竭.xlsx'
    Dragon=module(path4)
    dragons=PubChemUrls(Dragon)
    for i in dragons:
        i.append('LONG XUE JIE')
        
    druginfo=[]
    for j in modules:
        info=[]
        info.append(j[0])
        info.append(j[2])
        info.append(j[4])
        info.append(j[5])
        druginfo.append(info)
        
    for k in dragons:
        info=[]
        info.append(k[2])
        info.append(k[0])
        info.append(k[1].split('/')[-1])
        info.append(k[1])
        druginfo.append(info)
        
    druginfos=[]
    for i in druginfo:
        if(i[2]=='NA'):
            pass
        else:
            druginfos.append(i)
        
    writebase('drugs1',druginfos)
    
    urls=[]
    for i in druginfos:
        urls.append(i[3])
    
    urls0=[]
    for i in urls:
        if(i not in urls0):
            urls0.append(i)
    
    SFDS_3D_TCMID(urls0)
    SFDS_2D(urls0)
    SFDS_2D(address)
   