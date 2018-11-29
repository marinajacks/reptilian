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
    drugs=['浙贝母','三七','薏苡仁']
    modules=tcmsp.main(drugs)

    
    drugs1=['ZHE BEI MU','SAN QI','YI YI REN']
    modules1=tcmid.main(drugs1)
  
    herbs=['浙贝母','三七','薏苡仁']
    name='marina'
    password='han#1990@yan'
    drugsinfo=chem.wholedurgs(herbs,name,password)
    
    import pypinyin
 
# 不带声调的(style=pypinyin.NORMAL)
def hp(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s
 
# 带声调的(默认)
def hp2(word):
    s = ''
    for i in pypinyin.pinyin(word):
        s = s + ''.join(i) + " "
    return s
 
 
if __name__ == "__main__":
    print(hp("中国中央电视台春节联欢晚会"))
    print(hp2("中国中央电视台春节联欢晚会"))
