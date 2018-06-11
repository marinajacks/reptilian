#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:44:09 2018

@author: macbook
高考信息数据库,主要是从高考帮这样一个网站获取到的数据:
    网址:http://college.gaokao.com/spepoint/a9/p1/
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

#url="http://college.gaokao.com/spepoint/a9/p1/"

def getvalue(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    
    data_list = [] 
    for idx, tr in enumerate(soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            data_list.append({
                '专业名称': tds[0].string,
                '高校名称': tds[1].string,
                '平均分': tds[2].string,
                '最高分': tds[3].string,
                '考生地区': tds[4].string,
                '科别': tds[5].string,
                '年份': tds[6].string,
                '批次': tds[7].string
            })
    print(url) #主要是为了查看进程,不至于看不到数据的处理进程
    df=pd.DataFrame(data_list)
    return df

def geturls():
    urls=[]
    for i in range(3424):
        urls.append('http://college.gaokao.com/spepoint/a9/p'+str(i+1))
    return urls

def mergedata(urls):
    df1=getvalue(urls[0])
    for i in range(1,len(urls)):
        df=getvalue(urls[i])
        df1=pd.concat([df1,df],ignore_index=True)
    return df1
        
        
def writeexcel(df,path):
    df.to_excel(path,sheet_name='Sheet1')


if __name__ == "__main__":
    urls=geturls()
    path='/Users/macbook/documents/project/reptilian/college/gaokao1.xlsx'
    df=mergedata(urls)
    writeexcel(df,path)
    
    
    
    
    
'''
#这部分数据主要是为了测试错误数据使用的.
    url="http://college.gaokao.com/spepoint/a9/p1151/"
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    
    data_list = [] 
    for idx, tr in enumerate(soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            print(tds[3].string)
            
    print(data_list)
    print(url)
    df=pd.DataFrame(data_list)
    return df
'''