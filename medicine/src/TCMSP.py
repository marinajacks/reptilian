#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:38:22 2018

@author: macbook
这数据库的数据集来源于tcmsp,这里查询到a的所有的成分都是来自于这个
tcmsp数据库,从这个数据库里边获取到的数据是根据药品的名称获取到对
应的小分子的名称信息,存储到对应的Excel文件夹里边。
"""

import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import os


def getdrugurl(herb):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='http://lsp.nwu.edu.cn/tcmsp.php'
    driver.get(url)
    
    #模拟查询药物的相关操作
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys(herb)
    driver.find_element_by_id('searchBtTcm').click()
    time.sleep(1)
    
    #定位查找药品信息,这里值得注意的是,不能直接找到对应的药品数据,
    s=driver.find_elements_by_class_name('k-grid-content')
    trs = s[0].find_elements_by_tag_name('tr')
    tds=trs[0].find_elements_by_tag_name('td')
    #定位到对应的药品的链接信息
    #print(tds[2].find_element_by_tag_name("a").get_attribute('href'))
    time.sleep(1)
    url1=tds[2].find_element_by_tag_name("a").get_attribute('href')
    driver.get(url1)
    
    n=int(driver.find_element_by_link_text("Go to the last page").get_attribute('data-page')) #获取到点击的次数信息    
    
    #链接的信息数据首次获取到
    hrefs=[]
    tbodys=driver.find_elements_by_tag_name("tbody")
    trs=tbodys[0].find_elements_by_tag_name("tr")
    for tr in trs:
        td=tr.find_elements_by_tag_name("td")[1]
        href=td.find_element_by_tag_name("a").get_attribute("href")
        hrefs.append(href)
    
    #动态的点击获取到对应的数据,首次获取到的情况在后边是不需要在点击的.
    for i in range(n-1):
        driver.find_element_by_link_text("Go to the next page").click()
        time.sleep(1)
        tbodys=driver.find_elements_by_tag_name("tbody")
        trs=tbodys[0].find_elements_by_tag_name("tr")
        for tr in trs:
            td=tr.find_elements_by_tag_name("td")[1]
            href=td.find_element_by_tag_name("a").get_attribute("href")
            hrefs.append(href)
    driver.quit()
    return hrefs
       
def test1(herbs):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='http://lsp.nwu.edu.cn/tcmsp.php'
    driver.get(url)
    #模拟查询药物的相关操作
    for herb in herbs:
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys(herb)
        driver.find_element_by_id('searchBtTcm').click()
        time.sleep(2)
    driver.quit()
    
def test2(herb):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='http://lsp.nwu.edu.cn/tcmsp.php'
    driver.get(url)
    #模拟查询药物的相关操作
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys(herb)
    driver.find_element_by_id('searchBtTcm').click()
    time.sleep(2)


def test(url):
    #解析每个页面获取到想要的信息，主要是解析页面吗，并且把页面的数据弄到本地数据库中
    #url='http://lsp.nwu.edu.cn/tcmspsearch.php?qr=Fritillariae%20Thunbrgii%20Bulbus&qsr=herb_en_name&token=77088eff74d45b12d933c73b1ce1a00a'
    #url='http://lsp.nwu.edu.cn/molecule.php?qn=1004'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    r=res.text
   # b = r.encode('ISO-8859-1').decode(res.apparent_encoding)
    
    
    soup=BeautifulSoup(r,'html.parser')
    #soup.find(class_='left_header')
        
    tables = soup.findAll(class_='tableRst2')  
    tab = tables[0]  
  
    trs=tab.findAll('tr')
    nums=len(trs)
    info=[]
    for i in range(3):
        if(i==2):
            #获取到第二个元素的数据,然后将这个图片的url存储下来.
            u=url.split('//')[1].split('/')[0]
            #print(u+'/'+trs[i].find("img").get('src'))
            info.append('imgs:'+u+'/'+trs[i].find("img").get('src'))
        else:
            #print(trs[i].find('th').getText()+':'+trs[i].find('td').getText())
            info.append(trs[i].find('th').getText()+':'+trs[i].find('td').getText())
    return info

#这个函数用来进行下载图片到本地，但是实际山这个是不需要的
def imgsdownloads(folder,chems):
    #url='lsp.nwu.edu.cn/strctpng/MOL000869.png'
    folder=folder+'imags/'
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder) 
        
    for i in range(1,len(chems)):
        url=chems[i][2]
        name=chems[i][1]
        types=chems[i][2].split('/')[-1].split('.')[-1]
        
        if(len(name)>32):
            name=name[:32]
        
        adds='http://'+url
        path=folder+name+'.'+types
        
        html=requests.get(adds)
        with open(path,'wb') as f:
            f.write(html.content)
            f.flush()
        f.close()
        time.sleep(1)
        print('下载完成第'+str(i)+'图片')
    print('抓取完成')  



if __name__=='__main__':
    herb=input('输入药品名称(中文):')
    #ids=input('次数')
    urls=getdrugurl(herb)
    
    p='D:/project/reptilian/medicine/中药数据/TCMSP/'
    if os.path.exists(p+herb):
        pass
    else:
        os.makedirs(p+herb) 
    p=p+herb+'/'
    chems=[]
    chems.append(['Molecule ID','Molecule name','imgs'])
    for url in urls:
        print(test(url))
        name=test(url)
        value=[]
        for n in name:
            value.append(n.split(':')[1])
        chems.append(value)
        #chems.append(test(url))
    df=pd.DataFrame(chems)
    p1=p+herb+'.xlsx'
    df.to_excel(p1,sheet_name=herb,header=False)
    
    imgsdownloads(p,chems)
    

    