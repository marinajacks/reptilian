# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:14:08 2018

@author: hello
这个是用来进行药品靶点的求解
"""

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys  
import urllib.request
import time

#这个函数主要是用来进行某个特定网页的打开,打开网页后,找到对应的地址数据.给后
#续进行相关的
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
    time.sleep(2)
    
    #定位查找药品信息
    #driver.find_element_by_link_text('Related Targets').click()
    s=driver.find_elements_by_class_name('k-grid-content')
    trs = s[0].find_elements_by_tag_name('tr')
    tds=trs[0].find_elements_by_tag_name('td')
    #定位到对应的药品的链接信息
    time.sleep(2)
    url1=tds[2].find_element_by_tag_name("a").get_attribute('href')
    driver.get(url1)
    
    driver.find_element_by_link_text('Related Targets').click()
    time.sleep(1)
    n=int(driver.find_element_by_link_text("Go to the last page").get_attribute('data-page')) #获取到点击的次数信息    
    
    #链接的信息数据首次获取到
    hrefs=[]
    hrefs.append(['modid','molname','targetname','targeturl','targetid'])
    s1=driver.find_elements_by_class_name('k-grid-content')
    tbodys=s1[1].find_elements_by_tag_name("tbody")
    trs=tbodys[0].find_elements_by_tag_name("tr")
    for tr in trs:
        td=tr.find_elements_by_tag_name("td")
        modid=td[0].text
        molname=td[1].find_element_by_tag_name("a").get_attribute("text")
        targetname=td[2].find_element_by_tag_name("a").get_attribute("text")
        targeturl=td[2].find_element_by_tag_name("a").get_attribute("href")
        hrefs.append([modid,molname,targetname,targeturl])
    
    #动态的点击获取到对应的数据,首次获取到的情况在后边是不需要在点击的.
    for i in range(n-1):
        driver.find_element_by_link_text("Go to the next page").click()
        time.sleep(0.1)
        s1=driver.find_elements_by_class_name('k-grid-content')
        tbodys=s1[1].find_elements_by_tag_name("tbody")
        trs=tbodys[0].find_elements_by_tag_name("tr")
        for tr in trs:
            td=tr.find_elements_by_tag_name("td")
            modid=td[0].text
            molname=td[1].find_element_by_tag_name("a").get_attribute("text")
            targetname=td[2].find_element_by_tag_name("a").get_attribute("text")
            targeturl=td[2].find_element_by_tag_name("a").get_attribute("href")
            hrefs.append([modid,molname,targetname,targeturl])
   # driver.quit()
   #这部分获取到对应的药品靶点数据targetid,并将数据添加到对应的地址上
    for i in range(1,len(hrefs)):
        time.sleep(0.1)
        url0=hrefs[i][3]
        driver.get(url0)
        s10=driver.find_element_by_class_name("tableRst2")
        tbodys=s10.find_element_by_tag_name('thead')
        trs0=tbodys.find_elements_by_tag_name("tr")
        targetid=trs0[0].find_elements_by_tag_name("td")[0].text
        #print(targetid)
        hrefs[i].append(targetid)
    return hrefs
       
def writelocal0(path,hrefs):
    df=pd.DataFrame(hrefs)
    df.to_excel(path)



if __name__=="__main__":
    herb="浙贝母"
    herb=input('输入药品名称(中文):')
    hrefs=getdrugurl(herb)
    path=input('输入文件路径:')
    
    writelocal0(path,hrefs)
    
    
 
        
    

    