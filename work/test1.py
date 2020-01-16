# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:08:13 2019

@author: hello
"""

impor 


a="   -42"

b=a.strip()
print(int(b))


b="d7373 shuhweus"

c=list(b)
d=""
for j=0;j<len(c);j++:
    if(c[j].isdist()):
        d=d+c[j]
    else:
        break

print(d)
    
if(c[0].isdigit() or c[0]=='+' or c[0]=='='):
    print(c)
else:
    print(0)
    
    
    
import  pandas as pd
import os

def file_name(path):
    file=[]
    #根目录下面有三个数据，分别是根目录、子目录和文件的名字
    for root, dirs, files in os.walk(path):
        for i in files:
              file.append(path+i)
    return file

path="D:\\MarinaJacks\\project\\reptilian\\medicine\\molecule\\缺失数据\\对接数据\\"

file=file_name(path)

print(file)

a=pd.read_csv(file[0])
b=pd.read_csv(file[1])
