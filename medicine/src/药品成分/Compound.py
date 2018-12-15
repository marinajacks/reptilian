# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:00:27 2018

@author: hello
"""

import TCMID as tcmid
import TCMSP as tcmsp
import chemcpd as chem
import pandas as pd

import pypinyin

if __name__=="__main__":
    #现在发现的情况是，使用TCMSP数据库的话比较简单，现在只是用tcmsp进行简化操作
    drugs=['浙贝母','三七','薏苡仁']
    modules1=tcmsp.main(drugs)

    #把中文转成分开,然后在
    drugs1=['ZHE BEI MU','SAN QI','YI YI REN']
    modules2=tcmid.main(drugs1)
  
    herbs=['浙贝母','三七','薏苡仁']
    name='marina'
    password='han#1990@yan'
    modules3=chem.wholedurgs(herbs,name,password)

    
    modules=[]
    for i in modules1:
        modules.append(i)
    modules.extend(modules2)
    modules.extend(modules3)
    module=[]
    for i in modules:
        if(i not in module):
            module.append(i)
            
 
# 不带声调的(style=pypinyin.NORMAL)
def hp(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s
 
 
if __name__ == "__main__":
    print(hp("中 国 中 央电视台春节联欢晚会"))
