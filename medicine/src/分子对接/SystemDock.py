# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 10:43:27 2018
@author: hello
这个是做分子对接的自动化程序
"""

from selenium import webdriver
import pandas as pd
import time
import os
from selenium.common.exceptions import NoSuchElementException 


def getdata():
    path='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\genes.txt'
    f=open(path,'r')
    lines=f.readlines()
    gene=''
    for line in lines:
        gene+=line.strip('\n')
    return gene



#path='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\3D'
#这个函数可以获取指定文件下面的所有文件的子目录
def file_name(path):
    file=[]
    #根目录下面有三个数据，分别是根目录、子目录和文件的名字
    for root, dirs, files in os.walk(path):
        for i in files:
              file.append(path+i)
    return file
     
#这个函数是为了实现靶点获取的操作,得到的是一个串  
def gettarget(path):
    df=pd.read_excel(path,sheet_name="靶点交集")
    targets=[]
    for i in range(len(df['靶点'])):
        targets.append(df['靶点'].iloc[i])
    target=''
    for i in range(len(targets)-1):
        target+=targets[i]+','
    target=target+targets[-1]
    return target
        
    
    
def clicks(driver,file):
        driver.find_element_by_link_text('Upload File').click()
        #定位上传文件操作
        driver.find_element_by_name('uploader_form').click()
        driver.find_element_by_name('file').send_keys(file)
        #下面的部分实现上传操作
        test1=driver.find_element_by_id('addLigandsByFileDialog').find_elements_by_class_name('dijitDialogPaneActionBar')
        test1[0].find_elements_by_tag_name('button')[1].click()  #定位到对应的页面点击上传操作
        time.sleep(4)
        
        
def clicks1(driver,i):
        path2='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\TCMID_2D\\'
        file=file_name(path2)
        driver.find_element_by_link_text('Upload File').click()
        #定位上传文件操作
        driver.find_element_by_name('uploader_form').click()
        driver.find_element_by_name('file').send_keys(file[i])
        #下面的部分实现上传操作
        test1=driver.find_element_by_id('addLigandsByFileDialog').find_elements_by_class_name('dijitDialogPaneActionBar')
        test1[0].find_elements_by_tag_name('button')[1].click()  #定位到对应的页面点击上传操作
        time.sleep(10)
    
    
    
    
#将整个过程拆分成几个部分
def dock0():
    #path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\merge_pdbs.xlsx'
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    #driver = webdriver.Firefox(executable_path=path)
    path='D:\\project\\selenium\\v40\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)

   # path='D:\\project\\selenium\\chromedriver.exe'
   # driver = webdriver.Chrome(executable_path=path)#, chrome_options=options)
    url='http://systemsdock.unit.oist.jp/iddp/home/index'
    driver.get(url)
    driver.set_script_timeout(10)
    time.sleep(1)
    driver.find_element_by_id('generalMessageDialog')
    try:
        driver.find_element_by_link_text('Click here').click()
    except NoSuchElementException:
        driver.find_element_by_link_text('Click here').click()
        
    name=gettarget(path1)
    driver.find_element_by_link_text('STEP 1').click()
    time.sleep(1)
    #这部分是把页面中的数据放入到对应的空格中去
    driver.find_element_by_link_text('Protein PDB ID').click()
    driver.switch_to_frame('specifyProteinIdsEditor_iframe')
    driver.find_element_by_id('dijitEditorBody').send_keys(name)  #这一步很耗时
    
    #下面的操作实际上是要恢复到默认的页面上
    driver.switch_to_default_content() #回到默认的页面
    #下面的定位方式可以确保定位得到的框是唯一的
    test0=driver.find_element_by_id('addProteinNamesByIdsDialog').find_element_by_class_name('dijitDialogPaneActionBar')
    test0.find_elements_by_tag_name('button')[1].click()
    return driver




#实现第二部 STEP 2的操作
def dock1(driver):
    driver.switch_to_default_content()
    driver.find_element_by_partial_link_text('STEP 2').click()
    return driver

#实现最后一步step3的操作
def dock2(driver,nums):
    driver.find_element_by_partial_link_text('STEP 3').click()
    time.sleep(1)
    driver.find_element_by_id('run-docking').click()
    email='chenbiaozainan@126.com'
    note='TCMID的2D正式数据第'+nums+'个成分'
    driver.find_element_by_id('mailTextBox').send_keys(email)
    driver.find_element_by_id('noteTextBox').send_keys(note)
    s1=driver.find_element_by_id('executeConfirmDialog').find_element_by_class_name('dijitDialogPaneActionBar')
    s1.find_elements_by_tag_name('button')[1].click()
    
#实现上传成分的操作
    
def dock3(driver,a,b):
    for i in range(a,b):
        try:
            clicks1(driver,i)
        except ConnectionAbortedError:
            clicks1(driver,i)
        time.sleep(8)
    return driver

#上传和最后一部分操作都放在一起
def dock4(driver,a,b):
    for i in range(a,b):
        try:
            clicks1(driver,i)
            time.sleep(15) #尝试进行8s的停顿
        except ConnectionAbortedError: #假如出现异常，那么就延长再一次执行的时间
            clicks1(driver,i)
            time.sleep(40)
    try:
        dock2(driver,'\''+str(a+1)+'-'+str(b)+'\'')
    except ConnectionAbortedError:
        dock2(driver,'\''+str(a+1)+'-'+str(b)+'\'')
    time.sleep(5)
    driver.quit()
    
#上传和最后一部分操作都放在一起
def dock4s(driver,a,b):
    
    for i in range(a,b):
        try:
            clicks1(driver,i)
        except ConnectionAbortedError:
            clicks1(driver,i)
        time.sleep(20)
    try:
        dock2(driver,'\''+str(a+1)+'-'+str(b)+'\'')
    except ConnectionAbortedError:
        dock2(driver,'\''+str(a+1)+'-'+str(b)+'\'')
    time.sleep(5)
    driver.quit()

#下面的是测试函数，用来测试对接的某一个案例
def docks():
    path='D:\project\selenium\geckodriver'      #win环境下驱动地址
    path1='D:\\MarinaJacks\\project\\reptilian\\medicine\\Data\\merge.xlsx'
    #path='/Users/macbook/downloads/geckodriver'  #mac环境下驱动地址
    driver = webdriver.Firefox(executable_path=path)
    url='http://systemsdock.unit.oist.jp/iddp/home/index'
    driver.get(url)
    driver.set_script_timeout(10)
    time.sleep(1)
    driver.find_element_by_id('generalMessageDialog')
    driver.find_element_by_link_text('Click here').click()
    
    name=gettarget(path1)
    driver.find_element_by_link_text('STEP 1').click()
    time.sleep(1)
    #这部分是把页面中的数据放入到对应的空格中去
    driver.find_element_by_link_text('Protein PDB ID').click()
    driver.switch_to_frame('specifyProteinIdsEditor_iframe')
    driver.find_element_by_id('dijitEditorBody').send_keys(name)  #这一步很耗时
    
    #下面的操作实际上是要恢复到默认的页面上
    driver.switch_to_default_content() #回到默认的页面
    #下面的定位方式可以确保定位得到的框是唯一的
    test0=driver.find_element_by_id('addProteinNamesByIdsDialog').find_element_by_class_name('dijitDialogPaneActionBar')
    test0.find_elements_by_tag_name('button')[1].click()
    #这部分实际上少了对应的点击提交操作
    time.sleep(8)
    #下面是
    driver.switch_to_default_content()
    driver.find_element_by_partial_link_text('STEP 2').click()
    
    #下面的操作实现文件上传的操作
    '''
    driver.find_element_by_link_text('Upload File').click()
    #定位上传文件操作
    driver.find_element_by_name('uploader_form').click()
    
    path2='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\3D\\'
    file=file_name(path2)
    '''
    
    #实现目录上传
    for i in range(5):
            clicks1(driver,i)

    '''
    for i in range(5):
        driver.find_element_by_link_text('Upload File').click()
        #定位上传文件操作
        driver.find_element_by_name('uploader_form').click()
        driver.find_element_by_name('file').send_keys(file[i+1])
        #下面的部分实现上传操作
        test1=driver.find_element_by_id('addLigandsByFileDialog').find_elements_by_class_name('dijitDialogPaneActionBar')
        test1[0].find_elements_by_tag_name('button')[1].click()  #定位到对应的页面点击上传操作
        time.sleep(5)
    '''
    
    driver.find_element_by_partial_link_text('STEP 3').click()
    driver.find_element_by_id('run-docking').click()
    email='chenbiaozainan@126.com'
    note='正式数据第1-5个成分'
    driver.find_element_by_id('mailTextBox').send_keys(email)
    driver.find_element_by_id('noteTextBox').send_keys(note)

    
    s1=driver.find_element_by_id('executeConfirmDialog').find_element_by_class_name('dijitDialogPaneActionBar')
    s1.find_elements_by_tag_name('button')[1].click()

def main(a,b):
    driver=dock0()
    time.sleep(60)
    #这个可以直接获取到对应的session信息,实际上就是后边的结果信息
    try:
        session=driver.find_elements_by_class_name('header')[1].find_element_by_class_name('right-align').find_elements_by_tag_name('span')[1].text
    except ConnectionAbortedError:
        session=driver.find_elements_by_class_name('header')[1].find_element_by_class_name('right-align').find_elements_by_tag_name('span')[1].text
   
    session='http://systemsdock.unit.oist.jp/iddp/preProcess/load/'+session
    time.sleep(1)
    
    try:
        driver=dock1(driver)
    except ConnectionAbortedError:
        driver=dock1(driver)
        
    time.sleep(5)
    dock4(driver,a,b)
    return session




if __name__=="__main__":
    path2='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\TCMID_2D\\'
    file=file_name(path2)
    n=len(file)
    sessions=[]
    a=5
    while(a<240):
        print(a,a+5)
        session=main(a,a+5)
        sessions.append(session)
        print('The project is success!')
        time.sleep(20)
        a=a+5
    
    
    
    
    
    