#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:21:39 2018
这个数据主要是从智联招聘中获取到的数据,获取到数据后边还可以进行数据
的可视化。
@author: macbook
"""

import requests
from bs4 import BeautifulSoup
import re 



def test():
    url0='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E%2B%E4%B8%8A%E6%B5%B7&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&p=1&isadv='
    urls=[]
    for i in range(13):
        urls.append(url0+str(i+1))
    #注意到这里的数据分析师,只有1-13,所以获取到这个数据的时候,实际上只需要从1到13
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(urls[0],headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    jobs=soup.find_all(class_='zwmc')
    hrefs=[]
    for job in jobs:
        tags=job.find(href=re.compile("^http:"))
        if(tags is None):
            pass
        else:
            print(tags.get('href'))
            hrefs.append(tags.get('href'))
    
    return 0



def test1():
    url1='http://jobs.zhaopin.com/516616229250085.htm'
    url='http://jobs.zhaopin.com/490285325251385.htm?ssidkey=y&ss=201&ff=03&sg=ec1e7ec892084114a8c91a27e1d39487&so=3&uid=666930424'

    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    jobinfo=[]
    info=soup.find(class_='terminal-ul clearfix').get_text().split('\n')
    for i in info:
        if(i==''):
            pass
        else:
            jobinfo.append(i.strip())
    #这部分主要是为了写入到文本
    '''
    for i in jobinfo:
        print(i,end=' ')
    '''
            
    #下面的数据是很难获取到的.这部分的数据处理起来问题很多，
    #另外,实际上我们需要注意的就是这里是真正的文本处理
    #soup.find(class_='tab-inner-cont').get_text()
    
    return jobinfo


#这个函数获取到工作的url信息
def geturl(url0,n):
    #url0='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E%2B%E4%B8%8A%E6%B5%B7&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&p=1&isadv='
    urls=[]
    for i in range(n):
        urls.append(url0+str(i+1))
    #注意到这里的数据分析师,只有1-13,所以获取到这个数据的时候,实际上只需要从1到13
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=[]
    soups=[]
    jobss=[]
    for i in range(n):
        res.append(requests.get(urls[i],headers=headers))
        soups.append(BeautifulSoup(res[i].text,'html.parser'))
        jobss.append(soups[i].find_all(class_='zwmc'))
   
    hrefs=[]
    for jobs in jobss:
        for job in jobs:
            tags=job.find(href=re.compile("^http:"))
            if(tags is None):
                pass
            else:
                hrefs.append(tags.get('href'))
    return hrefs
    
def getvalue(url,path):
    #url1='http://jobs.zhaopin.com/516616229250085.htm'
    #url='http://jobs.zhaopin.com/490285325251385.htm?ssidkey=y&ss=201&ff=03&sg=ec1e7ec892084114a8c91a27e1d39487&so=3&uid=666930424'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    jobinfo=[]
    info=soup.find(class_='terminal-ul clearfix').get_text().split('\n')
    for i in info:
        if(i==''):
            pass
        else:
            jobinfo.append(i.strip())
    #这部分主要是为了写入到文本
    values=''
    for i in jobinfo:
        values+=i
        values+=' '
    values+='\n'
    f=open(path,'a',encoding='utf-8')
    f.write(values)
    f.close()
    print('hello')
    #下面的数据是很难获取到的.这部分的数据处理起来问题很多，
    #另外,实际上我们需要注意的就是这里是真正的文本处理
    #soup.find(class_='tab-inner-cont').get_text()
    
    #return jobinfo



if __name__ == "__main__":
    #url0='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E%2B%E4%B8%8A%E6%B5%B7&kw=%E6%9C%8D%E8%A3%85%E5%88%B6%E7%89%88%E5%B8%88&p=1&isadv='
    url0='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E%2B%E4%B8%8A%E6%B5%B7&kw=%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&p=1&isadv='
    urls=geturl(url0,90)
    path='/Users/macbook/documents/project/reptilian/work/job3.txt'
    for url in urls:
        getvalue(url,path)