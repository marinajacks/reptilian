#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:27:58 2018

@author: macbook
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:08:43 2018

@author: macbookz
这个数据主要来自于京东销售平台的数据,为了获取手机数据得到的销售数据而进行分析得到的。

"""


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime

#
def login(uname, pwd):
    path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path =path)
    driver.get("http://www.jd.com")
    driver.find_element_by_link_text("你好，请登录").click()
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    time.sleep(1)
    driver.find_element_by_name("loginname").send_keys(uname)
    time.sleep(1)
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    time.sleep(1)
    driver.find_element_by_id("loginsubmit").click()
    '''
    time.sleep(3)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(3)
    driver.find_element_by_link_text("去结算").click()
    '''
    now = datetime.datetime.now()
    print (now.strftime('%Y-%m-%d %H:%M:%S'))
    print ('login success')   
       

uname='chenbiaozainan@126.com'
pwd='han#1990@yan'
login(uname,pwd)  
#这里实现登陆的时候需要手动和机动相结合才可以,这是以为在这里,存在着
#验证码信息是无法获取到的.
driver.find_element_by_id('key').clear()
driver.find_element_by_id('key').send_keys('手机')
driver.find_element_by_class_name('button').click()

    
def test():
    url0='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E%2B%E4%B8%8A%E6%B5%B7&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&p=1&isadv='
    urls=[]
    for i in range(13):
        urls.append(url0+str(i+1))
    #注意到这里的数据分析师,只有1-13,所以获取到这个数据的时候,实际上只需要从1到13
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    res.encoding='utf8'
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


url=driver.current_url

def product(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    
    infos=soup.find_all(class_='gl-item')
    saleinfo=[]
    for info in infos:
        price=info.find(class_='p-price').get_text().strip()
        brand=info.find(class_='p-name p-name-type-2').get_text().strip()
        store=info.find(class_='p-shop').get_text().strip()
        
        mains=info.find(class_='ps-main').get_text().strip()

        num=info.find(class_='p-commit')
        if num is None:
            nums=0
        else:
            nums=num.get_text().strip()
        saleinfo.append([price,brand,mains,store,nums])
    return saleinfo
  

#这一步实现点击操操作
urls=[]
for i in range(100):
    d=driver.find_element_by_class_name('pn-next')
    d.click()
    time.sleep(1)
    url=driver.current_url
    urls.append(url)


phone=[]
for url in urls:
    phone.append(product(url))

phones=[]
for ph in phone:
    for p in ph:
        phones.append(p)
paths='/Users/macbook/documents/project/reptilian/phone/phone.txt'

infos=''
for p in phones:
    for i in p:
        infos+=i.strip().replace('\n','')
        infos+='|'
    infos+='\n'

f=open(paths,'w',encoding='utf-8')
f.write(infos)
f.close()

f=open(')
