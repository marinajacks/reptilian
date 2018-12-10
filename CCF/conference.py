# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:56:05 2018

@author: hello
"""

from selenium import webdriver
import pandas as pd
import time
from sqlalchemy import create_engine


def test(email,pwd):
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='https://www.myhuiban.com/conferences/'
    driver.get(url)
    driver.find_element_by_id('LoginForm_email').clear()
    driver.find_element_by_id('LoginForm_email').send_keys(email)
    driver.find_element_by_id('LoginForm_password').clear()
    driver.find_element_by_id('LoginForm_password').send_keys(pwd)
    driver.find_element_by_name('yt0').click()
    time.sleep(1)
    heads=driver.find_element_by_tag_name('thead').find_elements_by_tag_name('th')
    head=[]
    for th in heads:
        print(th.text)
        head.append(th.text)
    bodys=[]
    bodys.append(head)
    tag=20
    j=0
    while(1):
        trs=driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        td0=[]
        for tr in trs:
            tds=tr.find_elements_by_tag_name('td')
            td0=[]
            for td in tds:
                print(td.text,end='\t')
                td0.append(td.text)
            print()
            bodys.append(td0)
        test=driver.find_elements_by_partial_link_text('后页')
        time.sleep(1)
        if(len(test)==0 or j>tag):
            break
        else:
            driver.find_element_by_partial_link_text('后页').click()
            time.sleep(1)
        j=j+1
    driver.quit()
    return bodys
        
        

    
if __name__=="__main__":
    bodys=test('a','123')
    '''
    huiban=[]
    huiban.append(head)
    huiban.extend(bodys)
    df=pd.DataFrame(bodys)
    df.to_excel('D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\会伴.xlsx')
    
    writebase('confercence',bodys)
    
    for i in bodys:
        if(len(i)!=12):
            print((i))
    '''
        
    