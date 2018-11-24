#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:55:08 2018

@author: macbook
这个部分主要是为了进行模拟登陆的操作,然后进行模拟控制的操作
这个部分的数据主要是TCMID里边的数据,后边的
"""

import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.common.exceptions import NoSuchElementException 
import time
import os

def geturls(url):
    #下面的数据主要是为了获取到页面的药品链接信息
    #url='http://www.megabionet.org/tcmid/herb/5615/'
    #url='http://www.megabionet.org/tcmid/herb/2186/'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response=requests.get(url,headers=headers)
    urls=[]
    soup=BeautifulSoup(response.text,'html.parser')
    drugs=soup.find_all(class_='table table-striped table-bordered table-hover')[1]    
    for i in drugs.find_all('tr'):
        j=i.find_all('td')[0]#J
        if(j.find('a') is None):
            print(' ')
        else:
            if('tcmid' in (j.find('a')['href'])):
                #print('www.megabionet.org/'+j.find('a')['href'])
                urls.append('http://'+url.split('/')[2]+j.find('a')['href'])
                #urls.append('http://www.megabionet.org/'+j.find('a')['href'])
            else:
                print(j.find('a').string)
    return urls
    

#这里的操作主要是解析页面对应的文本信息
def durginfo(url):
    #url='http://www.megabionet.org/tcmid/ingredient/31556/'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response=requests.get(url,headers=headers)
    r=response.text
    #path='D:\project\reptilian\medicine\imgs'
    soup=BeautifulSoup(r,'html.parser')
    #￥title=soup.find(class_='title text-font').string.strip()
    titles=soup.find(class_='title text-font').string.strip().replace('Ingredient -- ','')
    return titles

#这里的操作主要是解析页面对应的文本信息
def durginfos(url):
    #url='http://www.megabionet.org/tcmid/ingredient/31556/'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response=requests.get(url,headers=headers)
    r=response.text
    #path='D:\project\reptilian\medicine\imgs'
    soup=BeautifulSoup(r,'html.parser')
    #￥title=soup.find(class_='title text-font').string.strip()
    titles=soup.find(class_='title text-font').string.strip().replace('Ingredient -- ','')
    formula=soup.find_all(class_='section-text text-font')[0].string.strip()
    pubchemid=soup.find_all(class_='section-text text-font')[2].string.strip()
    smile=soup.find_all(class_='section-text text-font')[3].string.strip()
    structure=url.split('//')[1].split('/')[0]+soup.find_all(class_='section-text text-font')[4].find("img").get('src')  #页面地址
    info=[]
    info.append(titles)
    info.append(formula)
    info.append(pubchemid)
    info.append(smile)
    info.append(structure)
    return info

def getdrug(drugname):
    #这个是通过模拟人的行为找到对应的药物的网页
    path='D:\project\selenium\geckodriver'
    #path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path=path)
    url='http://www.megabionet.org/tcmid/'
    driver.get(url)
    #模拟查询药物的相关操作
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
        url1=driver.current_url
    except NoSuchElementException:
        url1=driver.current_url
    driver.quit()
    return url1


def main(drugs):
    modules=[]
    for drugname in drugs:
        url=getdrug(drugname)
        urls=geturls(url)
        for url0 in urls:
            modules.append(durginfo(url0))
        print(drugname+' is success!')
    return modules
    
def imgsdownloads(folder,chems):#将url对应的页面的图片存储到本地
    #url='lsp.nwu.edu.cn/strctpng/MOL000869.png'
    folder=folder+'imags/'
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder) 
    for i in range(1,len(chems)):
        url=chems[i][4]
        name=chems[i][0]
        types=chems[i][4].split('/')[-1].split('.')[-1]
        
        flag=chems[i][4].split('/')[-1].split('.')[0]
        adds='http://'+url
        path=folder+name+'.'+types
        if(flag=='NA'):
            pass
        else:
            html=requests.get(adds)
            with open(path,'wb') as f:
                f.write(html.content)
                f.flush()
            f.close()
            time.sleep(1)
            print('下载完成第'+str(i)+'图片')
    print('抓取完成')  
    
if __name__=='__main__':
    drugs=['ZHE BEI MU','SAN QI','YI YI REN']
    modules=main(drugs)
    
    
    
    
    '''
    drugname=input('请输入中药名称(拼音大写):')
   # num=input('输入页面个数:')
    #p='/Users/macbook/documents/project/reptilian/medicine/中药数据/'
    p='D:/project/reptilian/medicine/中药数据/TCMID/'
    if os.path.exists(p+drugname):
        pass
    else:
        os.makedirs(p+drugname) 
    #p=r'D:\project\reptilian\medicine\'
    p=p+drugname+'/'

    url=getdrug(drugname)
    
    urls=geturls(url)
    
    drugs=[]
    drugs.append(['titles','formula','pubchemid','smile','structure'])
    for url0 in urls:
        print(durginfo(url0))
        drugs.append(durginfo(url0))
    drug=pd.DataFrame(drugs)
    #p=p+'\\'+drugname+num+'.xlsx' 这个地址是在win下使用的
    p1=p+drugname+'.xlsx'
    drug.to_excel(p1,sheet_name=drugname,header =False) #将数据写入到对应的excel中
    
    #下面的操作是进行图片写入的操作.           
    #folder='/Users/macbook/documents/project/reptilian/medicine/'
    #判断文件夹是否存在,如果不存在就新建,否则就不改变
    imgsdownloads(p,drugs)
    '''