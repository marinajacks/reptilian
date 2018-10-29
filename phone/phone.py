#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:08:43 2018

@author: macbookz
这个数据主要来自于天猫销售平台的数据,为了获取手机数据得到的
"""


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.action_chains import ActionChains


def login(name,password):
   # url0='https://login.tmall.com/?spm=875.7931836/B.a2226mz.1.66144265j4tft7&redirectURL=https%3A%2F%2Fwww.tmall.com%2F'
    #url0='https://login.tmall.com/?spm=875.7931836/B.a2226mz.1.661442657Z6VPZ&redirectURL=https%3A%2F%2Fwww.tmall.com%2F'
    url0='https://login.taobao.com/member/login.jhtml?'
    url0='https://login.tmall.com/'
   # url0='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=1d2ac728745a483c9a12915a3f489b23'
    path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path =path)
    driver.get(url0)
    #driver.maximize_window()
    #driver.find_element_by_class_name('login-links')#.click()
    time.sleep(3)
    sb=driver.find_element_by_class_name("login-switch")
    sb.click()
    
    userbox=driver.find_element_by_id("TPL_username_1")
    pwdbox=driver.find_element_by_id("TPL_password_1")
    
    userbox.send_keys(name)
    pwdbox.send_keys(password)
    
    source=driver.find_element_by_xpath("//*[@id='nc_1_n1z']")  
    #定义鼠标拖放动作
    ActionChains(driver).drag_and_drop_by_offset(source,1135,0).perform()
    #等待JS认证运行,如果不等待容易报错
    time.sleep(2)
    #查看是否认证成功，获取text值
    text=driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
     #目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
    if text.text.startswith(u'请在下方'):
        print('成功滑动')
    if text.text.startswith(u'请点击'):
        print('成功滑动')
    if text.text.startswith(u'请按住'):
        pass
    
    dragger=driver.find_element_by_id('nc_1_n1z')#.滑块定位
    
    action=ActionChains(driver)
    action.click_and_hold(dragger).perform()
    
    
    try:    
        action.drag_and_drop_by_offset(dragger,800, 0).perform()     

    except UnexpectedAlertPresentException:

        print("faild")
  
    for index in range(500):

        try:
    
            action.drag_and_drop_by_offset(dragger, 500, 0).perform()#平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
    
        except UnexpectedAlertPresentException:
    
            break
    driver.find_element_by_id('J_SubmitStatic').click()

    time.sleep(11)  #等待停顿时间

 
                                     
    hua=driver.find_element_by_id('nc_1__scale_text')
    hua.click()
  
    

    
    
    
    loadmore=driver.find_element_by_id("J_SubmitStatic")
    loadmore.click()
    
    
    
    url=driver.current_url
    driver.get(url)
    
    driver.find_element_by_class_name("qrcode-login")
    url='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=1.def.0.V01&wq=shouji&pvid=16319cb6e0f74a41b2b3fe5222fd77ee'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    
    product=soup.find_all(class_='gl-item')
   
    
    
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
    path='/Users/macbook/downloads/geckodriver'
    driver = webdriver.Firefox(executable_path =path)
    url0='https://www.tmall.com/'
    driver.get(url0)
    #模拟点击操作
    time.sleep(5)
    urls=[]
    driver.find_element_by_class_name('sn-login')
    driver.find_element_by_id('mq').send_keys('手机')
    time.sleep(5)
    driver.find_element_by_id("mq").submit()
    time.sleep(2)
    url=driver.current_url
    urls.append(url)
    for i in range(100):
        driver.find_element_by_class_name("ui-page-next").click()
        time.sleep(5)
        urls.append(driver.current_url)
    product=product(url)

    '''
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    
    infos=soup.find_all(class_='product item-1111 ')
    saleinfo=[]
    for info in infos:
        price=info.find(class_='productPrice').get_text().strip()
        brand=info.find(class_='productTitle productTitle-spu').get_text().strip()
        store=info.find(class_='productShop').get_text().strip()
        num=info.find(class_='productStatus')
        if num is None:
            nums=0
        else:
            nums=num.get_text().strip()
        saleinfo.append([price,brand,store,nums])
    driver.find_element_by_class_name("ui-page-next").click()
    uels=driver.current_url
    
    jobinfo=[]
    info=soup.find(class_='terminal-ul clearfix').get_text().split('\n')
    for i in info:
        if(i==''):
            pass
        else:
            jobinfo.append(i.strip())
    '''
    #这部分主要是为了写入到文本
    '''
    for i in jobinfo:
        print(i,end=' ')
    '''
            
    #下面的数据是很难获取到的.这部分的数据处理起来问题很多，
    #另外,实际上我们需要注意的就是这里是真正的文本处理
    #soup.find(class_='tab-inner-cont').get_text()
    
    return jobinfo
def product(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    
    infos=soup.find_all(class_='product item-1111 ')
    saleinfo=[]
    for info in infos:
        price=info.find(class_='productPrice').get_text().strip()
        brand=info.find(class_='productTitle productTitle-spu').get_text().strip()
        store=info.find(class_='productShop').get_text().strip()
        num=info.find(class_='productStatus')
        if num is None:
            nums=0
        else:
            nums=num.get_text().strip()
        saleinfo.append([price,brand,store,nums])
    return saleinfo
  

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

def writebase(infos):
    conn = pymysql.Connect(
         host='localhost',
         port=3306,
         user='root',
         passwd='123456',
         db='ecnu',
         charset='utf8'
     )
    cursor = conn.cursor()
    
    a=infos
    if(len(infos)==7):
        cursor.executemany("insert into kami(notes,area,rooms,unitprice,floor,year,totalprice) values(%s,%s,%s,%s,%s,%s,%s)"
                           ,[(a[0],a[1],a[2],a[3],a[4],a[5],a[6])])
        conn.commit()
    else:
        pass
    cursor.close()
    conn.close()
    
    

if __name__ == "__main__":
    #url0='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E%2B%E4%B8%8A%E6%B5%B7&kw=%E6%9C%8D%E8%A3%85%E5%88%B6%E7%89%88%E5%B8%88&p=1&isadv='
    url0='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E%2B%E4%B8%8A%E6%B5%B7&kw=%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&p=1&isadv='
    urls=geturl(url0,90)
    path='/Users/macbook/documents/project/reptilian/work/job3.txt'
    for url in urls:
        getvalue(url,path)