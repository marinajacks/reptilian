#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 13:55:14 2018

@author: macbook
这个是居理新房的房价数据的爬虫的结果.选取的是杭州的数据.
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd

def test():
    url='http://hz.julive.com/project/s'
    
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    
    apartments=[]
    houses=soup.find_all(class_='house-item main_click_total')
    for i in range(len(houses)):
        house=[]
        title=houses[i].find(class_='title').getText().strip()
        position=houses[i].find(class_='position project-card-position project-card-item').getText().strip().split('...')[0]
        types=houses[i].find(class_='types')
        if (types is None):
            types=''
        else:
            types=types.getText().strip()
        area=houses[i].find(class_='area')
        if (area is None):
            area=''
        else:
            area=area.getText().strip()
        celling=houses[i].find(class_='celling').getText().strip()
        house_tag=houses[i].find(class_='house-tag').getText().strip()
        prices=houses[i].find(class_='total-price ').getText().strip()
        totals=houses[i].find(class_='developer').getText().strip()
        house.append(title.split(' ')[0])
        house.append(position)
        house.append(types)
        house.append(area)
        house.append(celling.split('\xa0')[0])
        house.append(prices)
        house.append(totals.split('\n')[1])
        apartments.append(house)
    return pd.DataFrame(apartments)
    print(title,position,types,area,celling,prices,totals)


def pagevalue(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    
    apartments=[]
    houses=soup.find_all(class_='house-item main_click_total')
    for i in range(len(houses)):
        house=[]
        title=houses[i].find(class_='title').getText().strip()
        position=houses[i].find(class_='position project-card-position project-card-item').getText().strip().split('...')[0]
        types=houses[i].find(class_='types')
        if (types is None):
            types=''
        else:
            types=types.getText().strip()
        area=houses[i].find(class_='area')
        if (area is None):
            area=''
        else:
            area=area.getText().strip()
        celling=houses[i].find(class_='celling')
        if (celling is None):
            celling=''
        else:
            celling=celling.getText().strip()
        #house_tag=houses[i].find(class_='house-tag').getText().strip()#这部分数据不一定是有用的
        prices=houses[i].find(class_='total-price ')
        if (prices is None):
            prices=''
        else:
            prices=prices.getText().strip()
        totals=houses[i].find(class_='developer')
        if (totals is None):
            totals=''
        else:
            totals=totals.getText().strip()
            
        house.append(title.split(' ')[0])
        house.append(position)
        house.append(types)
        house.append(area)
        if(celling==''):
            house.append([' '])
        else:
            house.append(celling.split('\xa0')[0])
        house.append(prices)
        if(totals==''):
            house.append([' '])
        else:
            house.append(totals.split('\n')[1])
        apartments.append(house)
    return pd.DataFrame(apartments)

def geturls():
    url0='http://hz.julive.com/project/s'
    urls=[]
    urls.append(url0)
    for i in range(1,96):
        urls.append(url0+'/z'+str(i+1))
    return urls



if __name__=='__main__':
    path='/Users/macbook/documents/project/reptilian/house/hznew7.xlsx'
    urls=geturls()
    s=pagevalue(urls[0])
    for i in range(1,len(urls)):
        s1=pagevalue(urls[i])
        print(s1)
        s=pd.concat([s,s1],ignore_index=True)
        print(i)
    
    print(s)
    s.to_excel(path,sheet_name='杭州新房')
    print(s)
        
        
