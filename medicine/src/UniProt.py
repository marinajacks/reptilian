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
from  NCBI import Genes1


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
    if(len(results)>0):       
        results=np.array(results)
        results=results[np.lexsort(results.T)]
        result=results.tolist()
    return  results


'''
下面的函数主要是为了定位页面获取到PDB数据
'''
def getpdbs(url):
    #url='https://www.uniprot.org/uniprot/P08253'
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址
    driver = webdriver.Firefox(executable_path=path)
   # url='https://www.uniprot.org/uniprot/P03956'
    driver.get(url)
    PDB=[]
    #由于页面是iframe嵌套的子页面，所以这里需要选择子页面操作
    iframe=driver.find_elements_by_tag_name('iframe')
    if(len(iframe)>0):
        Frame=driver.find_elements_by_id('structureFrame')
        if(len(Frame)>0):
            driver.switch_to_frame('structureFrame')
            #定位页面中的tbody的位置
            test=driver.find_elements_by_tag_name("tbody")
            if(len(test)>0):
                tbodys=driver.find_element_by_tag_name("tbody")
                trs=tbodys.find_elements_by_tag_name("tr")
            
                pdbs=[]
                for tr in trs:
                    pdb=[]
                    td=tr.find_elements_by_tag_name("td")
                    for i in td:
                        pdb.append(i.text.strip())
                    pdbs.append(pdb)
                
                if(len(sortpdbs(pdbs))>0):
                    PDB=sortpdbs(pdbs)[0]
                driver.quit()
        driver.quit()
    else:
        driver.quit()
    return PDB
    #print(PDB)
    
    
'''
下面的函数主要是为了定位页面获取到PDB数据,这个函数主要是单个条件的数据获取
'''

def PDBS(url1,Uniprots):
    #url1='https://www.uniprot.org/uniprot/'
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

#下面的函数可以批量获取到靶点信息
def PDBS1(urls):
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
    Pdbs=[]
    for url in urls:
        driver.get(url)
        time.sleep(1)
        print(url)
        #由于页面是iframe嵌套的子页面，所以这里需要选择子页面操作
        iframe=driver.find_elements_by_tag_name('iframe')
        if(len(iframe)>0):
            driver.switch_to_frame('structureFrame')
            #定位页面中的tbody的位置
            time.sleep(1)
            tbodys=driver.find_element_by_tag_name("tbody")
            trs=tbodys.find_elements_by_tag_name("tr")
            #time.sleep(1)
            pdbs=[]
            for tr in trs:
                pdb=[]
                td=tr.find_elements_by_tag_name("td")
                time.sleep(1)
                for i in td:
                    pdb.append(i.text.strip())
                pdbs.append(pdb)
                
            PDB=sortpdbs(pdbs)

           # print(PDB)
            if(len(PDB)>0):
                Pdbs.append(PDB[0])
    
    driver.quit()
    return Pdbs

#下面的函数可以根据给定基因的名称，完成单个的基因的相关蛋白质的查找。
def main(target):
    url='https://www.uniprot.org/'   #给定查询页面
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址
    driver = webdriver.Firefox(executable_path=path)
    
    driver.get(url)
    #下面的操作是为了查询特定靶点的数据
    driver.find_element_by_id('query').clear()
    driver.find_element_by_id('query').send_keys(target)
    #driver.find_element_by_id('query').send_keys(Keys.ENTER)
    driver.find_element_by_id('search-button').click()
    #这一步是选择Human的筛选
    href=driver.find_element_by_id("orgFilter-9606").get_attribute('href')
    driver.get(href)
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

#下面的函数可以根据给定基因组，批量完成基因对应相关蛋白质的查找。
def main1(targets):
    url1='https://www.uniprot.org/'   #给定查询页面
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址
    driver = webdriver.Firefox(executable_path=path)
    
    driver.get(url1)
    urls=[]
    for target in targets:
        #下面的操作是为了查询特定靶点的数据
        driver.find_element_by_id('query').clear()
        driver.find_element_by_id('query').send_keys(target)
        #driver.find_element_by_id('query').send_keys(Keys.ENTER)
        driver.find_element_by_id('search-button').click()
        #这一步是选择Human的筛选
        href=driver.find_element_by_id("orgFilter-9606").get_attribute('href')
        driver.get(href)
        time.sleep(1)
        #下面的是查询的结果
        s=driver.find_element_by_id('resultsArea')
        tbodys=s.find_element_by_tag_name('tbody')
        trs=tbodys.find_elements_by_tag_name("tr")
        #下面是为了获取到第一行查询的结果
        td=trs[0].find_elements_by_tag_name('td')
        
        #这是第二列的href数据
        url=td[1].find_element_by_tag_name("a").get_attribute("href")
        urls.append(url)
    driver.quit()
    return  urls

def getuniprot():
    path='D://MarinaJacks//project//reptilian//medicine//Data//Uniprot.txt'
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
    #target='NGFR'
   # url=main(target)

    name='adenomyosis'
    genes=Genes1(name)
    
    Gene=[]
    for i in genes:
        Gene.append(i[0])
    urls=main1(Gene)
    pdb=[]

    for url in urls:
        if(len(getpdbs(url))>0):
            pdb.append(getpdbs(url))
            print('Success!',url)
        else:
            print('There is no PDB')
    
    pdbs1=pdb[6:93]
    pdbs2=[]
    for i in pdbs1:
        pdbs2.append(i.tolist())
        
    path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\adenomyosis.xlsx'
    df1=pd.DataFrame(pdbs2)
    df1.to_excel(path1,header=True,index=False)
        
    #上面的都是一个页面的数据，是其中一种疑难杂症，下面的是另外一种病症
    
    Uniprots=getuniprot()
    path='https://www.uniprot.org/uniprot/'
    URL=[]
    for i in Uniprots:
        URL.append(path+i)
    
    endometriosis=[]
    
    for url in URL:
        if(len(getpdbs(url))>0):
            endometriosis.append(getpdbs(url))
            print('Success!',url)
        else:
            print('There is no PDB')
    #这个是获得的endometriosis的数据  
    endos=[]
    for i in endometriosis:
        if(len(i)>0):
            if(len(i[2])>0):
                endos.append(i.tolist())
        
        
    df2=pd.DataFrame(endos)
    df2.to_excel('D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\endometriosis.xlsx',header=False,index=False)
        
        
    merge=[]
    for i in pdbs2:
        if(i in endos):
            merge.append(i[0])
            
    df3=pd.DataFrame(merge,columns=['靶点']) #这里设置列名称的时候，需要在DataFrame中设置
    df3.to_excel('D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\merge.xlsx',index=False,sheet_name='靶点交集')
    
    pd.read_excel('D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\merge.xlsx')
    
    target=''
    for i in range(len(merge)-1):
        target+=merge[i]+','
    target=target+merge[-1]
        
        
        
        
        
        