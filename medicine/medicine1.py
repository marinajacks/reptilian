#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:38:22 2018

@author: macbook

"""

import requests 
from bs4 import BeautifulSoup

def test(url):
    #url='http://lsp.nwu.edu.cn/tcmspsearch.php?qr=Fritillariae%20Thunbrgii%20Bulbus&qsr=herb_en_name&token=77088eff74d45b12d933c73b1ce1a00a'
    url='http://lsp.nwu.edu.cn/molecule.php?qn=1004'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    r=res.text
    b = r.encode('ISO-8859-1').decode(res.apparent_encoding)
    
    
    soup=BeautifulSoup(r,'html.parser')
    #soup.find(class_='left_header')
        
    tables = soup.findAll(class_='tableRst2')  
    tab = tables[0]  
  
    trs=tab.findAll('tr')
    nums=len(trs)
    
    for i in range(nums):
        if(i==2):
            #获取到第二个元素的数据,然后将这个图片的url存储下来.
            u=url.split('//')[1].split('/')[0]
            print(u+'/'+trs[i].find("img").get('src'))
        else:
            print(trs[i].find('th').getText()+':'+trs[i].find('td').getText())
    
    
    
    
    
    
def TCMSP(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    r=res.text
    b = r.encode('ISO-8859-1').decode(res.apparent_encoding) #修改编码,防止数据编码出现问题.
    
    soup=BeautifulSoup(r,'html.parser')
        
    tables = soup.findAll(class_='tableRst2')  
    tab = tables[0]  
  
    trs=tab.findAll('tr')
    nums=len(trs)
    
    for i in range(nums):
        if(i==2):
            #获取到第二个元素的数据,然后将这个图片的url存储下来.
            u=url.split('//')[1].split('/')[0]
            print(u+'/'+trs[i].find("img").get('src'))
        if(i==3):
            num=trs[i].findall('tr')
        else:
            print(trs[i].find('th').getText()+':'+trs[i].find('td').getText())
    
    #上面计算的过程中,发现比较难获取的数据是
    
    soup.find(class_='k-grid-header-wrap')
    
    
    
    
    
    
    
    
    
    
    
    ''' 
    for tr in tab.findAll('tr'):  
        for th in tr.findAll('th'):#,tr.findAll('td'):  
            print(th.getText())
    '''


def pagevalue(url):
    
    
    return 0

if __name__=='__main__':
    print("hello world")