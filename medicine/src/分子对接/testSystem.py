# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 22:15:30 2018

@author: hello
"""
from SystemDock import dock0
from SystemDock import dock1
from SystemDock import dock2
from SystemDock import dock3
from SystemDock import dock4
from SystemDock import clicks1
from SystemDock import file_name
import  time
import pandas as pd

def getc(a,b):
    for i in range(a,b):
        print('clicks1(driver,'+str(i)+')')

def getcs(a,b):
    for i in range(a,b):
        print('try:')
        print('    '+'clicks1(driver,'+str(i)+')')
        print('except ConnectionAbortedError:')
        print('    '+'clicks1(driver,'+str(i)+')')

def getres(a,b):
    print('dock2(driver,\''+str(a+1)+'-'+str(b)+'\')')
    
def getres1(a,b):
     print('try:')
     print('    '+'dock2(driver,\''+str(a+1)+'-'+str(b)+'\')')
     print('except ConnectionAbortedError:')
     print('    '+'dock2(driver,\''+str(a+1)+'-'+str(b)+'\')')

    
    
def test(a,b):
    getcs(a,b)
    getres1(a,b)

def tests():
    driver=dock0()
    time.sleep(60)

    try:
        driver=dock1(driver)
    except ConnectionAbortedError:
        driver=dock1(driver)

    dock4(driver,55,60)

def main(a,b):
    driver=dock0()
    time.sleep(60)
    
    try:
        driver=dock1(driver)
    except ConnectionAbortedError:
        driver=dock1(driver)
    time.sleep(5)
    dock4(driver,a,b)
    


    

#测试发现执行两次就会解决好
#ConnectionAbortedError: [WinError 10053] 你的主机中的软件中止了一个已建立的连接。
#这样的问题
#下面是循环实现这个操作，每次上传5个页面的操作
def test2(driver):
    for i in range(45,50):
        try:
            clicks1(driver,i)
        except ConnectionAbortedError:
            clicks1(driver,i)
        time.sleep(8)
    
    try:
        dock2(driver,'46-50')
    except ConnectionAbortedError:
        dock2(driver,'46-50')


    
def datas():
    path='D:\\MarinaJacks\\project\\reptilian\\medicine\\中药数据\\TCMID\\'
    names=['SAN QI','YI YI REN','ZHE BEI MU','龙血竭']

    paths=[]
    for name in names:
        paths.append(path+name+'\\'+name+'.xlsx')
        
    dfs=[]
    for i in range(len(paths)):
        df=pd.read_excel(paths[i])
        for j in range(len(df)):
            dfs.append(df['titles'].iloc[j])
        print(len(df))
    
    drugs=[]
    for i in dfs:
        if(i not in drugs):
            drugs.append(i)
    return drugs
        
if __name__=="__main__":
    path2='D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\TCMID_3D\\'
    file=file_name(path2)
    n=len(file)
    a=0
    while(a<n):
        print(a,a+5)
        main(a,a+5)
        print('The project is success!')
        time.sleep(20)
        a=a+5

