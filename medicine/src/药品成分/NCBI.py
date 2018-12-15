# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:20:42 2018

@author: hello
这个是为了获取到NCBI数据库中的靶点数据书写的脚本,可以
获取到靶点相关的数据,并且将其存储到本地的数据库中
"""
from selenium import webdriver
import time
import pandas as pd 


#这个函数用来实现给定疾病对应的靶点信息，函数返回该疾病对应的所有人类的靶点的名称
def Target(name):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/gene'
    driver.get(url)
    #下面的部分是为了输入疾病名称，模拟点击操作
    driver.find_element_by_name("term").clear()
    driver.find_element_by_name("term").send_keys(name)
    driver.find_element_by_id('search').click()
    #首先确定是人类的基因信息，下面是模拟点击操作
    time.sleep(1)
    driver.find_element_by_partial_link_text('Homo sapiens').click() #点击操作，获取Human的基因
    time.sleep(3)
    n=int(driver.find_element_by_class_name("num").get_attribute('last')) #这样用来获取到页面的个数  
      
    Genes=[]        
    for i in range(n-1):
        tbodys=driver.find_element_by_tag_name("tbody")
        trs=tbodys.find_elements_by_tag_name("tr")
        for tr in trs:
            gene=[]
            td=tr.find_elements_by_tag_name("td")
            gene.append(td[0].text.strip().split('\n')[0]) #基因简写
            gene.append(td[1].text.strip().split('[')[0])  #基因名称
            Genes.append(gene)
        driver.find_element_by_link_text('Next >').click() #模拟点击进入下一个页面
        
    #最后一页信息获取
    tbodys=driver.find_element_by_tag_name("tbody")
    trs=tbodys.find_elements_by_tag_name("tr")
    for tr in trs:
        gene=[]
        td=tr.find_elements_by_tag_name("td")
        gene.append(td[0].text.strip().split('\n')[0])
        gene.append(td[1].text.strip().split('[')[0])
        Genes.append(gene)
    driver.quit()
    return Genes

#这个函数用来实现给定疾病对应的靶点信息，函数返回该疾病对应的所有人类的靶点的名称,这个函数与上面
#的主要区别就是，不进行click操作，利用数据本身的特点，如果基因名称中存在Human保留，否则删去。实际上
#这个是比较好的方式。
def Targets(name):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.ncbi.nlm.nih.gov/gene'
    driver.get(url)
    #下面的部分是为了输入疾病名称，模拟点击操作
    driver.find_element_by_name("term").clear()
    driver.find_element_by_name("term").send_keys(name)
    driver.find_element_by_id('search').click()
    
    n=int(driver.find_element_by_class_name("num").get_attribute('last')) #这样用来获取到页面的个数  
      
    Genes=[]        
    for i in range(n-1):
        tbodys=driver.find_element_by_tag_name("tbody")
        trs=tbodys.find_elements_by_tag_name("tr")
        for tr in trs:
            gene=[]
            td=tr.find_elements_by_tag_name("td")
            if('human' in td[1].text.strip()): #这主要是为了筛选Human对应的基因
                gene.append(td[0].text.strip().split('\n')[0]) #基因简写
                gene.append(td[1].text.strip().split('[')[0])  #基因名称
                Genes.append(gene)
            else:
                pass
        driver.find_element_by_link_text('Next >').click() #模拟点击进入下一个页面
    #最后一页信息获取
    tbodys=driver.find_element_by_tag_name("tbody")
    trs=tbodys.find_elements_by_tag_name("tr")
    for tr in trs:
        gene=[]
        td=tr.find_elements_by_tag_name("td")
        if('human' in td[1].text.strip()):
            gene.append(td[0].text.strip().split('\n')[0])
            gene.append(td[1].text.strip().split('[')[0])
            Genes.append(gene)
        else:
            pass
    driver.quit()
    return Genes

if __name__=="__main__":
    name='adenomyosis'
    genes=Target(name)
    print(genes)
    genes1=Targets('endometriosis')
    print(genes1)
    path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\adenomyosis_gene.xlsx'
    path2='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\endometriosis_gene.xlsx'
    path3='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\merge_gene.xlsx'
    df1=pd.DataFrame(genes)
    df2=pd.DataFrame(genes1)
    df1.to_excel(path1)
    df2.to_excel(path2)
    
    gene0=[]
    for i in genes:
        if(i in genes1):
            gene0.append(i)
            
    df3=pd.DataFrame(gene0)
    df3.to_excel(path3)
    
    
    
    