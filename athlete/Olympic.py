#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 20:25:20 2018
这个脚本主要是为了获得奥林匹克运动员的相关数据,从而得到相关的运动员的个人信息，
便于进行进一步的数据分析

@author: macbook
"""

import requests
from bs4 import BeautifulSoup
import re

#url='http://info.2012.163.com/athlete/584.html'
'''
res=requests.get(url)



soup=BeautifulSoup(res.text,'html.parser')

content=soup.find_all(class_='table')




print(content[0].find('h1').getText())

b=content[0].find_all('li')

#print(len(b))

for name in b:
    print(name.getText())
'''
'''
#这里的脚本可以访问静态的所有人员的信息
url='http://info.2012.163.com/athlete/list/'

res=requests.get(url)


soup=BeautifulSoup(res.text,'html.parser')
    
content1=soup.find_all(class_='clearfix switch-item')

#content=soup.find_all(class_='logo')

#u=content1[9].find_all('li')#.find('a').get('href')

for content in content1:
    u=content.find_all('li')
    for u0 in u:
        url0=(u0.find('a').get('href'))
        print(u0.find('a').get('title'),end=' ')
        urls=url.replace(url.split('/')[-2],url0.split('/')[-1])
        urls=urls[0:len(urls)-1]
        print(urls)


'''
'''
content2=soup.find_all(class_='clearfix switch-item')

u=content2[0].find_all('li')

u[0].find_all(class_='logo')
'''

#content2[19].find_all('li')



#print(content)


'''

#下面的函数用来处理运动员的相关信息,获取例如姓名、性别等相关数据
#这里其实还可以将这些数据存储在数据库中,脚本只需要做简单的修改就好,
#或者是将数据存储在txt文本中
def athlete(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content=soup.find_all(class_='table')
    b=content[0].find_all('li')
    info=[]
    print(content[0].find('h1').getText())
    info.append(content[0].find('h1').getText().split('\t'))
    for name in b:
        print(name.getText())
        info.append(name.getText())
    return info
    

info=athlete(url)
'''


'''
import urllib.request


url='http://info.2012.163.com/athlete/list/'


req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page.decode("utf8"))
'''
#下面的脚本用来动态的进行网页的访问

from selenium import webdriver

import time

path='/Users/macbook/downloads/geckodriver'

driver = webdriver.Firefox(executable_path =path)

'''
driver.get("http://info.2012.163.com/athlete/list/")

#driver.find_elements_by_class_name('yui_3_3_0_1_152637068449533')

time.sleep(5)

print (driver.title)

print ('Browser will close.')
driver.quit()

print ('Browser is close')
'''

url="http://info.2012.163.com/athlete/list/"

driver.get("http://info.2012.163.com/athlete/list/")


d=driver.find_elements_by_class_name('logo')

                  
                  

f=open('/Users/macbook/downloads/spy.txt','w')
#这一条指令长主要是用来进行判断左右移动的操作,每次移动一个
for i in range(49):
    m=driver.find_element_by_class_name("left_arrow").click()
    time.sleep(1)


def main(n):
    for i in range(n):
        m=driver.find_elements_by_class_name("left_arrow")
        m[1].click()
        time.sleep(2)
        s=driver.find_elements_by_class_name("MContent-list2")
        #time.sleep(2)
        a=s[1].text.split('\n')
        b=[]
        for i in a:
            if i=='':
                pass
            else:
                b.append(i)
        for i in b:
            print(i)

#这里需要注意的是,获取一个参数与获取所有的参数实际上是需要注意区分的,现在的情况就是
#加了s的就是全部的参数,不加上s的就是单独的
m=driver.find_elements_by_class_name("left_arrow")

m[0].click()

from selenium.webdriver.common.by import By

driver.find_element(By.partialLinkText("athlete"))


m[1].click()


driver.find_elements_by_link_text('athlete')


driver.find_element_by_id('yui_3_3_0_1_1526456221376161')

a=s.text.split('\n')
b=[]
for i in a:
    if i=='':
        pass
    else:
        b.append(i)

#这条指令确实可以获取到href这样的一个地址链接.
links=driver.find_elements_by_xpath("//*[@href]")


for link in links:
    #f.write(link.get_attribute('href'))
    #f.write('\n')
    print (link.get_attribute('href'))

f.close()
s1.get_attribute('href')


m1=driver.find_element_by_id("yui_3_3_0_1_152645622137633").click()



#driver.find_elements_by_xpath('[@class = \"logo\"]/text()')



driver.find_element_by_id("kw").send_keys("spark")

driver.find_element_by_id("su").submit()

time.sleep(2)
#通过 submit() 来操作 driver.find_element_by_id("su").submit()
time.sleep(3)
driver.quit()





'''
import numpy as np
import  matplotlib.pyplot   as plt
a=np.linspace(-10,10,100)
b=[]
for i in range(len(a)):
    b.append(np.exp(-a[i])/np.power(1+np.exp(-a[i]),2))
    
a=list(a)
plt.plot(a,b)

 url='http://su.julive.com/project/s/e1-z3'
 res=requests.get(url)
 res.status_code
 
 soup=BeautifulSoup(res.text,'html.parser')
 soup.find()
'''



from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import time

# Login 163 email
path='/Users/macbook/downloads/geckodriver'

driver = webdriver.Firefox(executable_path =path)
driver.get("http://mail.163.com/")

name=input("输入用户名:")
password=input("输入用户密码:")

elem_user = driver.find_element_by_name("username")
elem_user.clear
elem_user.send_keys(name)  
elem_pwd = driver.find_element_by_name("password")
elem_pwd.clear
elem_pwd.send_keys(password)  
elem_pwd.send_keys(Keys.RETURN)
#driver.find_element_by_id("loginBtn").click()
#driver.find_element_by_id("loginBtn").submit()
time.sleep(5)  
assert "baidu" in driver.title  
driver.close()  
driver.quit()  




data = driver.page_source

s1.id



#下面测试一些数据的使用情况

driver.current_url #获取当前的


if __name__ == "__main__": 
    test(3)
    