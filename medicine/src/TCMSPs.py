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
import time
import os
import pandas as pd
from sqlalchemy import create_engine

#这个函数用来获取到化合物成分的页面url
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
    #下面是多种结果的情况下查找合适的药品的网页链接
    body0=[]
    tbody0=driver.find_element_by_tag_name("tbody")
    trs0=tbody0.find_elements_by_tag_name('tr')
    for tr in trs0:
        tds=tr.find_elements_by_tag_name('td')
        body0.append(tds[0].text)
    #查找成分所在的位置
    for i in range(len(body0)):
        if(body0[i]==herb):
            loc=i
    url1=(trs0[loc].find_elements_by_tag_name('td')[2].find_element_by_tag_name('a').get_attribute('href'))
    driver.get(url1)
    #下面的部分是进行页面的查找的作业
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

#这个函数用来获取到化合物成分的页面url
def getdrugur2(herb):
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
    #下面是多种结果的情况下查找合适的药品的网页链接
    body0=[]
    tbody0=driver.find_element_by_tag_name("tbody")
    trs0=tbody0.find_elements_by_tag_name('tr')
    for tr in trs0:
        tds=tr.find_elements_by_tag_name('td')
        body0.append(tds[0].text)
    #查找成分所在的位置
    for i in range(len(body0)):
        if(body0[i]==herb):
            loc=i
    url1=(trs0[loc].find_elements_by_tag_name('td')[2].find_element_by_tag_name('a').get_attribute('href'))
    driver.get(url1)
    #下面的部分是进行页面的查找的作业
    n=int(driver.find_element_by_link_text("Go to the last page").get_attribute('data-page')) #获取到点击的次数信息    
    #链接的信息数据首次获取到
    hrefs=[]
    tbodys=driver.find_elements_by_tag_name("tbody")
    trs=tbodys[0].find_elements_by_tag_name("tr")
    for tr in trs:
        td=tr.find_elements_by_tag_name("td")[1]
        href=td.find_element_by_tag_name("a").get_attribute("href")
        OB=tr.find_elements_by_tag_name("td")[6].text
        DL=tr.find_elements_by_tag_name("td")[9].text
        hrefs.append([href,OB,DL])
    #动态的点击获取到对应的数据,首次获取到的情况在后边是不需要在点击的.
    for i in range(n-1):
        driver.find_element_by_link_text("Go to the next page").click()
        time.sleep(1)
        tbodys=driver.find_elements_by_tag_name("tbody")
        trs=tbodys[0].find_elements_by_tag_name("tr")
        for tr in trs:
            td=tr.find_elements_by_tag_name("td")[1]
            href=td.find_element_by_tag_name("a").get_attribute("href")
            OB=tr.find_elements_by_tag_name("td")[6].text
            DL=tr.find_elements_by_tag_name("td")[9].text
            hrefs.append([href,OB,DL])
    driver.quit()
    return hrefs



#这个函数用来获取到化合物成分的的成分
def getmodule(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='http://lsp.nwu.edu.cn/tcmsp.php'
    driver.get(url)
    #模拟查询药物的相关操作
    results=[]
    driver.find_element_by_tag_name('button').click()
    driver.find_element_by_link_text('Chemical name').click()  #这个部分是为了进行
    for compound in modules:
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys(compound)
        driver.find_element_by_id('searchBtTcm').click()
        time.sleep(1)
        #下面是多种结果的情况下查找合适的药品的网页链接
        test=driver.find_elements_by_link_text(compound)
        if(len(test)>0):
            driver.find_element_by_link_text(compound).click()
            time.sleep(1)
            mol=driver.find_element_by_class_name('tableRst2')
            molname=mol.find_elements_by_tag_name('tr')[1].find_element_by_tag_name('td').text
            c=driver.find_elements_by_tag_name('tbody')[0].find_element_by_tag_name('tr')
            tds=c.find_elements_by_tag_name('td')
            OB=tds[4].text
            DL=tds[7].text
            PubchemCid=mol.find_elements_by_tag_name('tr')[7].find_element_by_tag_name('td').text
            compounds=[molname,OB,DL,PubchemCid]
            results.append(compounds)
        time.sleep(1)
    driver.quit()
    return results
        
#这个函数用来获取到化合物成分的的成分
def getbyInChIKeys(modules):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='http://lsp.nwu.edu.cn/tcmsp.php'
    driver.get(url)
    #模拟查询药物的相关操作
    results=[]
    driver.find_element_by_tag_name('button').click()
    driver.find_element_by_link_text('InChIKey').click()  #这个部分是为了进行
    time.sleep(1)
    for compound in modules:
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys(compound)
        driver.find_element_by_id('searchBtTcm').click()
        time.sleep(2)
        #下面是多种结果的情况下查找合适的药品的网页链接
        test=driver.find_elements_by_link_text(compound)
        if(len(test)>0):
            driver.find_element_by_link_text(compound).click()
            time.sleep(1)
            mol=driver.find_element_by_class_name('tableRst2')
            molname=mol.find_elements_by_tag_name('tr')[1].find_element_by_tag_name('td').text
            c=driver.find_elements_by_tag_name('tbody')[0].find_element_by_tag_name('tr')
            tds=c.find_elements_by_tag_name('td')
            OB=tds[4].text
            DL=tds[7].text
            PubchemCid=mol.find_elements_by_tag_name('tr')[7].find_element_by_tag_name('td').text
            compounds=[molname,OB,DL,PubchemCid]
            results.append(compounds)
        time.sleep(1)
    driver.quit()
    return results
    
#这个函数用来获取到化合物成分的的成分
def getbyInChIKey(compound):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='http://lsp.nwu.edu.cn/tcmsp.php'
    driver.get(url)
    #模拟查询药物的相关操作
    driver.find_element_by_tag_name('button').click()
    driver.find_element_by_link_text('InChIKey').click()  #这个部分是为了进行
 
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys(compound)
    driver.find_element_by_id('searchBtTcm').click()
    time.sleep(2)
    #下面是多种结果的情况下查找合适的药品的网页链接
    test=driver.find_elements_by_link_text(compound)
    if(len(test)>0):
        driver.find_element_by_link_text(compound).click()
        time.sleep(1)
        mol=driver.find_element_by_class_name('tableRst2')
        molname=mol.find_elements_by_tag_name('tr')[1].find_element_by_tag_name('td').text
        c=driver.find_elements_by_tag_name('tbody')[0].find_element_by_tag_name('tr')
        tds=c.find_elements_by_tag_name('td')
        OB=tds[4].text
        DL=tds[7].text
        PubchemCid=mol.find_elements_by_tag_name('tr')[7].find_element_by_tag_name('td').text
        compounds=[molname,OB,DL,PubchemCid]
    else:
        compounds=[]
    driver.quit()
    return compounds

#这个函数用来批量获取到化合物成分的页面url
def moduleurls(compound):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='http://lsp.nwu.edu.cn/tcmsp.php'
    driver.get(url)
    #模拟查询药物的相关操作
    driver.find_element_by_tag_name('button').click()
    driver.find_element_by_link_text('Chemical name').click()  #这个部分是为了进行
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys(compound)
    driver.find_element_by_id('searchBtTcm').click()
    time.sleep(1)
    #下面是多种结果的情况下查找合适的药品的网页链接
    driver.find_element_by_link_text(compound).click()
    a=driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('td')[1]
    url=a.find_element_by_tag_name('a').get_attribute('href')
    driver.quit()
    return url
    



#这个函数可以根据成分的url遍历获取成分的名称、OB、DL、PubChemID等相关信息
def getmodules1(url):
    #url='http://lsp.nwu.edu.cn/molecule.php?qn=4450'
    path='D:\project\selenium\geckodriver' 
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url)
    mol=driver.find_element_by_class_name('tableRst2')
    molname=mol.find_elements_by_tag_name('tr')[1].find_element_by_tag_name('td').text
    c=driver.find_elements_by_tag_name('tbody')[0].find_element_by_tag_name('tr')
    tds=c.find_elements_by_tag_name('td')
    OB=tds[4].text
    DL=tds[7].text
    PubchemCid=mol.find_elements_by_tag_name('tr')[7].find_element_by_tag_name('td').text
    compound=[molname,OB,DL,PubchemCid]
    driver.quit()
    return compound

    



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
    driver.quit()
    time.sleep(2)

#获取药品成分的名称信息即可
def druginfo(url):
    #解析每个页面获取到想要的信息，主要是解析页面吗，并且把页面的数据弄到本地数据库中
    #url='http://lsp.nwu.edu.cn/tcmspsearch.php?qr=Fritillariae%20Thunbrgii%20Bulbus&qsr=herb_en_name&token=77088eff74d45b12d933c73b1ce1a00a'
    #url='http://lsp.nwu.edu.cn/molecule.php?qn=1004'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    r=res.text
    
    soup=BeautifulSoup(r,'html.parser')
    tables = soup.findAll(class_='tableRst2')  
    tab = tables[0]  
    trs=tab.findAll('tr')
    info=(trs[1].find('td').getText()) #获取药品成分的名称信息
    return info


#这个函数可以获取到药品化合物全面的成分
def druginfos(url):
    #解析每个页面获取到想要的信息，主要是解析页面吗，并且把页面的数据弄到本地数据库中
    #url='http://lsp.nwu.edu.cn/tcmspsearch.php?qr=Fritillariae%20Thunbrgii%20Bulbus&qsr=herb_en_name&token=77088eff74d45b12d933c73b1ce1a00a'
    #url='http://lsp.nwu.edu.cn/molecule.php?qn=1004'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    r=res.text
    
    soup=BeautifulSoup(r,'html.parser')
    tables = soup.findAll(class_='tableRst2')  
    tab = tables[0]  
    trs=tab.findAll('tr')
    info=[]
    for i in range(3):
        if(i==2):
            #获取到第二个元素的数据,然后将这个图片的url存储下来.
            u=url.split('//')[1].split('/')[0]
            info.append('imgs:'+u+'/'+trs[i].find("img").get('src'))
        else:
            info.append(trs[i].find('th').getText()+':'+trs[i].find('td').getText())
    return info


#这个函数可以获取到药品化合物全面的成分,这个使用selenium来进行成分的解析
def druginfos1(urls):
    #解析每个页面获取到想要的信息，主要是解析页面吗，并且把页面的数据弄到本地数据库中
    #url='http://lsp.nwu.edu.cn/tcmspsearch.php?qr=Fritillariae%20Thunbrgii%20Bulbus&qsr=herb_en_name&token=77088eff74d45b12d933c73b1ce1a00a'
    #url='http://lsp.nwu.edu.cn/molecule.php?qn=1004'
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='http://lsp.nwu.edu.cn/tcmsp.php'
    driver.get(url)
    infos=[]
    for url in urls:
        driver.get(url)
        mol=driver.find_element_by_class_name('tableRst2')
        molname=mol.find_elements_by_tag_name('tr')[1].find_element_by_tag_name('td').text
        c=driver.find_elements_by_tag_name('tbody')[0].find_element_by_tag_name('tr')
        tds=c.find_elements_by_tag_name('td')
        OB=tds[4].text
        DL=tds[7].text
        PubchemCid=mol.find_elements_by_tag_name('tr')[7].find_element_by_tag_name('td').text
        compound=[molname,OB,DL,PubchemCid]
        infos.append(compound)
    driver.quit()
    return infos




#这个函数可以获取到所有的成分的化合物信息
def wholedrugs(urls):
    chems=[]
    for url in urls:
        chems.append(druginfo(url))
    return chems


 #这个函数可以给定药品的名称完全获得对应的       
def main(drugs):
    module=[]
    for herb in drugs:
        urls=getdrugurl(herb)
        infos=druginfos1(urls)
        for info in infos:
            info.append(herb)
        module.append(infos)
    
    modules=[]
    for i in module:
        for j in i:
            modules.append(j)
    return modules




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




def writebase(paths):
    engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format('root', '', 'localhost:3306', 'ecnu'))
    con = engine.connect()
    df1=pd.read_csv(paths[0])
    df1.to_sql(name='Compound', con=con, if_exists='append', index=False)
    for i in range(1,len(paths)):
        df=pd.read_csv(paths[i])
        df1=pd.concat([df1,df])#每次做一个
        df.to_sql(name='result1', con=con, if_exists='append', index=False)
    return df1
        


if __name__=='__main__':
    drugs=['浙贝母','三七','薏苡仁']
    #drugs=['鱼腥草','金银花','赤芍','艾叶','薄荷']
    #drugs=['半夏','黄连','黄芩','干姜','人参','大枣','甘草']
    modules=main(drugs)
    df=pd.DataFrame(modules)
    path4='D:\MarinaJacks\project\\reptilian\medicine\中药数据\TCMSP\龙血竭\龙血竭.xlsx'
    df1=pd.read_excel(path4)
    dragon=[]
    df1['Molecule name']
    for i in range(len(df1['Molecule name'])):
        name=[]
        name.append(df1['Molecule name'].iloc[i])
        for j in range(3):
            name.append('')
        name.append('龙血竭')
        dragon.append(name)
    modules1=modules
    modules1.extend(dragon)
    
    



    engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format('root', '', 'localhost:3306', 'ecnu'))
    con = engine.connect()
    df.to_sql(name='Compound', con=con, if_exists='append', index=False)
    
    
    
    
    
    
    herb='三七'
    urls=getdrugurl(herb)
    infos=druginfos1(urls)
    for info in infos:
        info.append(herb)
    df=pd.DataFrame(infos)
    engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format('root', '', 'localhost:3306', 'ecnu'))
    con = engine.connect()
    df.to_sql(name='Compound', con=con, if_exists='append', index=False)
    
    
    
    
    '''
    path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\浙贝母等成分.xlsx'
    df=pd.DataFrame(modules,columns={'module'})
    df.to_excel(path1)
    '''
    
    
    '''
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
        print(druginfo(url))
        name=druginfo(url)
        value=[]
        for n in name:
            value.append(n)
        chems.append(value)
        #chems.append(test(url))
    
    df=pd.DataFrame(chems)
    p1=p+herb+'.xlsx'
    df.to_excel(p1,sheet_name=herb,header=False)
    
    imgsdownloads(p,chems)
    '''

    