
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 19:54:36 2018

@author: macbook
这个程序主要是为了进行医药数据的分析得来的名称,参数等相关信息,
使用上海有机所的中药与化学成分数据库来进行的数据的爬取和准备,
该程序可以实现单个成分的获取，也可以实现批量的数据的获取。
"""
from selenium import webdriver
import pandas as pd
import re
import time

#这个函数仅为了获取到药草成分的名称信息
def getdurg(drugname,name,password):
#def getdurg(drugname,p,name,password):
    #url='http://www.chemcpd.csdb.cn/cmpref/Tcm_Multi/R_tcd_Comp.asp'
    #headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    #response=requests.get(url,headers=headers)
    #现在我们发现为什么在使用编码的时候出现原始的代码的问题,主要就是原始的代码出现父编码与本层的编码
    #格式出现不一致的问题.另外,从这里可以看到,实际上我们需要使用到动态的网页爬虫技术来进行网页的登陆
   # path='/Users/macbook/downloads/geckodriver'
    path='D:\project\selenium\geckodriver'
    driver = webdriver.Firefox(executable_path =path)
    url1='http://www.chemcpd.csdb.cn/cmpref/main/tcm_introduce.asp?n%20Count=6077992'
    driver.get(url1)
    time.sleep(1)
    #下面是模拟登陆的页面
    driver.find_element_by_name('Username').clear()   #清除用户名字
    driver.find_element_by_name('Username').send_keys(name)#输入用户名
    driver.find_element_by_name('Password').clear()   #清除用户密码
    driver.find_element_by_name('Password').send_keys(password)#输入用户密码
    driver.find_element_by_name('login').click()   #点击登陆
    #文本检索数据信息
    time.sleep(1)
    driver.find_element_by_link_text('中药药材检索').click()
    #driver.find_element_by_link_text('中药药材检索').get_attribute("href") 这部分的数据主要是为了
    #获取到中药药材检索对应的href数据,其实不一定是为了获取到这些数据,还可以直接click来跳转到对应的网页
    driver.find_element_by_name('Specname').clear()
    driver.find_element_by_name('Specname').send_keys(drugname)
    driver.find_element_by_id('submit1').click()
    time.sleep(1)
    #首先需要确定的是存在这样的一个结果,不存在的话就不进行相关的后续操作
    tbodys0=driver.find_elements_by_tag_name('tbody')
    #下面的主要目标是获得精确的药品名称,精确确定,因为一种药草名称对应着很多的药材
    if(len(tbodys0)>0):
        loc =None
        while(loc is None):
            tbodys=driver.find_element_by_tag_name('tbody')
            trs=tbodys.find_elements_by_tag_name('tr')
            drugs=[]
            for  tr in trs:
                tds=tr.find_elements_by_tag_name('td')
                drugs.append(tds[5].text)
                
            for i in range(len(drugs)):
                if(drugname==drugs[i]):
                    loc=i
                    break
                else:
                  loc=None
            if(loc is not None):
                break
            
            driver.find_element_by_name('next').click()
            
        driver.find_elements_by_name('FID')[loc-1].click()
        driver.find_element_by_name('Tcd_Comp_ID').click()
        n=int((driver.find_elements_by_tag_name('font')[-1]).find_element_by_tag_name('b').text)
     
         #下面是另外的一种写法,这种写法可以有效的把开头的数据清理掉，另外,这部分完全是为了下载页面数据
        drugs=[]
        names=[]
    
        table = driver.find_element_by_class_name('newform')
        table_rows = table.find_elements_by_tag_name('tr')
        tds=table_rows[0].find_elements_by_tag_name('td')
        for i in range(1,len(tds)):
               names.append(tds[i].text)
        drugs.append(names)
            
        for cl in range(1,n):
           table = driver.find_element_by_class_name('newform')
           table_rows = table.find_elements_by_tag_name('tr')
        
           for i in range(1,len(table_rows)):
               drug=[]
               tds=table_rows[i].find_elements_by_tag_name('td')
               for j in range(1,len(tds)):
                   drug.append(tds[j].text)
               drugs.append(drug)
                
           driver.find_element_by_name('next').click()
        #单独把最后一页面的数据存储起来
        table = driver.find_element_by_class_name('newform')
        table_rows = table.find_elements_by_tag_name('tr')
        
        for i in range(1,len(table_rows)):
               drug=[]
               tds=table_rows[i].find_elements_by_tag_name('td')
               for j in range(1,len(tds)):
                   drug.append(tds[j].text)
               drugs.append(drug)
               
        modules=[]
        for drug in drugs:
            modules.append(drug[0])
            
        mos=[]
        for i in modules:
            name=i.split('/')
            if(len(name)==2):
                mos.append(name[1].strip())
            else:
                zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
                for n in name:
                    match=zhPattern.search(n)
                    if(match is None):
                        mos.append(n.strip())
                        break
       # df=pd.DataFrame(mos)
        
       # df.to_excel(p)
        driver.quit()
        return mos
    else:
        print('不存在该药材')
        
#这个函数可以获取到较为全面的药品成分信息，包括中英文名称还有就是”化合物分子式“和”CAS号“信息
def getdurgs(drugname,p,name,password):
    #url='http://www.chemcpd.csdb.cn/cmpref/Tcm_Multi/R_tcd_Comp.asp'
    #headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    #response=requests.get(url,headers=headers)
    #现在我们发现为什么在使用编码的时候出现原始的代码的问题,主要就是原始的代码出现父编码与本层的编码
    #格式出现不一致的问题.另外,从这里可以看到,实际上我们需要使用到动态的网页爬虫技术来进行网页的登陆
   # path='/Users/macbook/downloads/geckodriver'
    path='D:\project\selenium\geckodriver'
    driver = webdriver.Firefox(executable_path =path)
    url1='http://www.chemcpd.csdb.cn/cmpref/main/tcm_introduce.asp?n%20Count=6077992'
    driver.get(url1)
    
    #下面是模拟登陆的页面
    driver.find_element_by_name('Username').clear()   #清除用户名字
    driver.find_element_by_name('Username').send_keys(name)#输入用户名
    driver.find_element_by_name('Password').clear()   #清除用户密码
    driver.find_element_by_name('Password').send_keys(password)#输入用户密码
    driver.find_element_by_name('login').click()   #点击登陆
    #文本检索数据信息
    time.sleep(1)
    driver.find_element_by_link_text('中药药材检索').click()
    #driver.find_element_by_link_text('中药药材检索').get_attribute("href") 这部分的数据主要是为了
    #获取到中药药材检索对应的href数据,其实不一定是为了获取到这些数据,还可以直接click来跳转到对应的网页
    driver.find_element_by_name('Specname').clear()
    driver.find_element_by_name('Specname').send_keys(drugname)
    driver.find_element_by_id('submit1').click()
    time.sleep(1)
    #首先需要确定的是存在这样的一个结果,不存在的话就不进行相关的后续操作
    tbodys0=driver.find_elements_by_tag_name('tbody')
    #下面的主要目标是获得精确的药品名称,精确确定,因为一种药草名称对应着很多的药材
    if(len(tbodys0)>0):
        loc =None
        while(loc is None):
            tbodys=driver.find_element_by_tag_name('tbody')
            trs=tbodys.find_elements_by_tag_name('tr')
            drugs=[]
            for  tr in trs:
                tds=tr.find_elements_by_tag_name('td')
                drugs.append(tds[5].text)
                
            for i in range(len(drugs)):
                if(drugname==drugs[i]):
                    loc=i
                    break
                else:
                  loc=None
            if(loc is not None):
                break
            
            driver.find_element_by_name('next').click()
            
        driver.find_elements_by_name('FID')[loc-1].click()
        driver.find_element_by_name('Tcd_Comp_ID').click()
        n=int((driver.find_elements_by_tag_name('font')[-1]).find_element_by_tag_name('b').text)
     
         #下面是另外的一种写法,这种写法可以有效的把开头的数据清理掉，另外,这部分完全是为了下载页面数据
        drugs=[]
        names=[]
    
        table = driver.find_element_by_class_name('newform')
        table_rows = table.find_elements_by_tag_name('tr')
        tds=table_rows[0].find_elements_by_tag_name('td')
        for i in range(1,len(tds)):
               names.append(tds[i].text)
        drugs.append(names)
            
        for cl in range(1,n):
           table = driver.find_element_by_class_name('newform')
           table_rows = table.find_elements_by_tag_name('tr')
        
           for i in range(1,len(table_rows)):
               drug=[]
               tds=table_rows[i].find_elements_by_tag_name('td')
               for j in range(1,len(tds)):
                   drug.append(tds[j].text)
                   print(tds[j].text)
               drugs.append(drug)
               print(table_rows[i].text)
                
           driver.find_element_by_name('next').click()
        #单独把最后一页面的数据存储起来
        table = driver.find_element_by_class_name('newform')
        table_rows = table.find_elements_by_tag_name('tr')
        
        for i in range(1,len(table_rows)):
               drug=[]
               tds=table_rows[i].find_elements_by_tag_name('td')
               for j in range(1,len(tds)):
                   drug.append(tds[j].text)
                   print(tds[j].text)
               drugs.append(drug)
               print(table_rows[i].text)
               
            
        df=pd.DataFrame(drugs)
        
        df.to_excel(p)
        driver.quit()
    else:
        print('不存在该药材')
    
def wholedurgs(drugs,name,password):
    drugsinfo=[]
    for drug in drugs:
        infos=getdurg(drug,name,password)
        for i in infos:
            drugsinfo.append(i)
    return drugsinfo



if __name__=="__main__":

    #herb=input('中药名称(中文)')
    #name=input("输入用户名:")
    #password=input("输入用户密码:")
    #这个是mac的地址
    #p='/Users/macbook/documents/project/reptilian/medicine/中药数据/上海有机/'
    '''
    p1=r'D:\project\reptilian\medicine\中药数据\上海有机所1'+'\\'+herb
    if os.path.exists(p1):
        pass
    else:
        os.makedirs(p1) 
    #p1=p+herb+'/'+herb+'.xlsx' win下的设计
    p=p1+'\\'+herb+'.xlsx'
    '''
    herbs=['半夏','黄连','黄芩','干姜','人参','大枣','甘草']
    name='marina'
    password='han#1990@yan'
    drugsinfo=wholedurgs(herbs,name,password)

