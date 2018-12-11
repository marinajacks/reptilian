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
import numpy as np 
from sqlalchemy import create_engine


#这个函数用来实现给定疾病对应的靶点信息，函数返回该疾病对应的所有人类的靶点的名称,这个函数与上面
#的主要区别就是，不进行click操作，利用数据本身的特点，如果基因名称中存在Human保留，否则删去。实际上
#这个是比较好的方式。
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
    time.sleep(1)
    n=int(driver.find_element_by_class_name("num").get_attribute('last')) #这样用来获取到页面的个数  
      
    genes=[]        
    for i in range(n-1):
        tbodys=driver.find_element_by_tag_name("tbody")
        trs=tbodys.find_elements_by_tag_name("tr")
        for tr in trs:
            gene=[]
            td=tr.find_elements_by_tag_name("td")
            if('human' in td[1].text.strip()): #这主要是为了筛选Human对应的基因
                gene.append(td[0].text.strip().split('\n')[0]) #基因简写
                gene.append(td[1].text.strip().split('[')[0])  #基因名称
                genes.append(gene)
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
            #gene.append(td[1].text.strip().split('[')[0])
            genes.append(gene)
        else:
            pass
    driver.quit()
    return genes


#下面的函数可以根据给定基因的名称，完成单个的基因的相关蛋白质的查找。
def UniProtID(target):
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
    time.sleep(1)
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

#查询所有的靶点的UniProtID信息
def UniProtIDs(targets):
    urls=[]
    for target in targets:
        urls.append(UniProtID(target))
    
    return urls
      
#这个是对靶点的PDBID进行排序选择最优的PDBID的脚本  
def sortpdbs(pdbs):
    results=[]
    for pdb in pdbs:
          result=[]
          for i in range(3):
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

#这个函数可以拿来进行回去到每个靶点蛋白的全部信息，例如uniprotid、Protein、gene信息。
def Pdb(url):
    #url='https://www.uniprot.org/uniprot/P08253'
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url)
    time.sleep(1)
    meta=[]
    #由于页面是iframe嵌套的子页面，所以这里需要选择子页面操作
    iframe=driver.find_elements_by_tag_name('iframe')
    if(len(iframe)>0):
        Frame=driver.find_elements_by_id('structureFrame')
        if(len(Frame)>0):
            uniprotid=url.split('/')[-1]
            Protein=driver.find_element_by_id('content-protein').text
            gene=driver.find_element_by_id('content-gene').text
            meta=[uniprotid,Protein,gene]
            driver.switch_to_frame('structureFrame')
            time.sleep(1)
            #定位页面中的tbody的位置
            test=driver.find_elements_by_tag_name("tbody")
            if(len(test)>0):
                tbodys=driver.find_element_by_tag_name("tbody")
                trs=tbodys.find_elements_by_tag_name("tr")
                time.sleep(1)
                pdbs=[]
                for tr in trs:
                    pdb=[]
                    td=tr.find_elements_by_tag_name("td")
                    for i in td:
                        pdb.append(i.text.strip())
                    pdbs.append(pdb)
                
                if(len(sortpdbs(pdbs))>0):
                    meta.append(sortpdbs(pdbs)[0][0])
                driver.quit()
        driver.quit()
    else:
        driver.quit()
    return meta

#这个函数可以获取到所有的靶点的信息，把前面的都循环遍历一遍获取到全部信息。
def Pdbs(urls):
    Protein=[]
    for url in urls:
        Protein.append(Pdb(url))
        
    #下面对处理好的数据进行去重以及去掉无用的数据
    Proteins=[]
    for i in Proteins:
        if(i not in Protein and len(i)>0):
            Proteins.append(i)
            
    return Proteins
#还要把数据写道对应的数据库里边
def writebase(table,data):
    #这里的table是表名称，data是数据，本质上是一个
    engine = create_engine("mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4".format('root', '', 'localhost:3306', 'ecnu'))
    con = engine.connect()
    df=pd.DataFrame(data)
    df.to_sql(name=table, con=con, if_exists='append', index=False)
    
    
#主函数可以得到全部数据。一次性获得全部。
if __name__=="__main__":
    name='adenomyosis'
    genes=Target(name)
    urls=UniProtIDs(genes)
    Proteins=Pdbs(urls)
    writebase('targets',Proteins)