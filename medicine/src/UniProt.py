# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:12:12 2018
@author: hello
"""

from selenium import webdriver
import pandas as pd
import time
import numpy as np
from sqlalchemy import create_engine

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
            uniprotid=url.split('/')[-1]
            Protein=driver.find_element_by_id('content-protein').text
            gene=driver.find_element_by_id('content-gene').text
            meta=[uniprotid,Protein,gene]
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
            if(len(PDB)>0):
                meta.append(PDB[0])
                Pdbs.append(meta)
    
    driver.quit()
    return Pdbs

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
def Uniprots(targets):
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
        time.sleep(3)
        urls.append(url)
        driver.quit()
        driver = webdriver.Firefox(executable_path=path)
        driver.get(url1)
        time.sleep(3)
        print('Success!')
    driver.quit()
    return  urls

#下面的方案可以用来进行化简获取基因靶点的操作，它可以根据给定基因组，批量完成基因对应相关蛋白质的查找。
#但是,下面的程序存在一个问题就是，在进行筛选的时候，页面没有跳转就进行了下一步，导致地址的获取是错误的。
#比较好的处理方式是每次打开一个页面，否则就会导致出现上述的问题。
def main2(targets):
    url1='https://www.uniprot.org/'   #给定查询页面
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver' #这个对应的mac的驱动的地址    
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url1)
    time.sleep(3)
    urls=[]
    for target in targets:
        #下面的操作是为了查询特定靶点的数据
        target=target+'\tAND organism:"Homo sapiens (Human) [9606]"' #这里直接限定是Human
        driver.find_element_by_id('query').clear()
        driver.find_element_by_id('query').send_keys(target)
        #driver.find_element_by_id('query').send_keys(Keys.ENTER)
        driver.find_element_by_id('search-button').click()
        #下面的是查询的结果
        time.sleep(1)
        s=driver.find_element_by_id('resultsArea')
        tbodys=s.find_element_by_tag_name('tbody')
        trs=tbodys.find_elements_by_tag_name("tr")
        #下面是为了获取到第一行查询的结果
        td=trs[0].find_elements_by_tag_name('td')
        #这是第二列的href数据
        url=td[1].find_element_by_tag_name("a").get_attribute("href")
        urls.append(url)
        time.sleep(1)
        
    driver.quit()
    return  urls
    

if __name__=="__main__":
    #基因获取部分    
    name='adenomyosis'
    genes=Genes1(name)
    
    urls=[]
    for gene in genes:
        urls.append(main(gene[0]))
        
    gene0=[]
    for i in genes:
        gene0.append(i[0])
    
    Uniprots(gene0)
        
        
        
        
    #下面的操作是为了获取到对应的靶点相关信息 
    pdb=[]
    for url in urls:
        if(len(getpdbs(url))>0):
            pdb.append(getpdbs(url))
            print('Success!',url)
        else:
            print('There is no PDB')
    '''       
    path0='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\merge_pdb.xlsx'
    df=pd.DataFrame(pdb)
    df.to_excel(path0)
    '''
    
    result=[]
    for i in range(len(pdb)):
        if(len(pdb[i])==4):
            result.append(pdb[i])
            
    
    path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\merge_pdbs.xlsx'

    df=pd.read_excel(path1)
    
    engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format('root', '', 'localhost:3306', 'ecnu'))
    con = engine.connect()
    df.to_sql(name='Target', con=con, if_exists='append', index=False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
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
        
    '''
        
        
        
        