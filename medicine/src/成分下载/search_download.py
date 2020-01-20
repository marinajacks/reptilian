# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import os

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\Users\\mhzha\\Desktop\\data\\mol1'}
options.add_experimental_option('prefs', prefs)
options.add_argument('disable-infobars')
path='C:\\Users\\mhzha\\Desktop\\data\\chromedriver.exe'
dri = webdriver.Chrome(executable_path=path, chrome_options=options)

result0=[]
result = []



def mols1(driver,name):
    
    url='http://www.chemspider.com/'
    driver.get(url)
    
    driver.find_element_by_name("ctl00$ctl00$ContentSection$ContentPlaceHolder1$simpleSearch$simple_query").clear()
    driver.find_element_by_name("ctl00$ctl00$ContentSection$ContentPlaceHolder1$simpleSearch$simple_query").send_keys(name)
    driver.find_element_by_name('search_text_button').click()

    try:
        found = driver.find_element_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_ResultStatementControl1_plhCountMessage")
        result0.append("有")
        save_id = driver.find_elements_by_class_name("hide-below-desktop")[1].text
        result.append(save_id.lstrip("ChemSpider ID"))
        driver.find_element_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_RecordViewDetails_rptDetailsView_ctl00_ThumbnailControl1_save").click()
    except NoSuchElementException:
        found = driver.find_element_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_ResultViewControl1_ResultStatementControl1_plhCountMessage")
        li=[]
        found = found.text
        print("found=",found)
        li = found.split(" ")
        if li[1] == '0':
            result0.append("无")
            print("无")
        else:
            result0.append("2")
            driver.find_element_by_xpath("//td[@class='search-id-column expand footable-visible footable-first-column']/a").click()
            save_id = driver.find_elements_by_class_name("hide-below-desktop")[1].text
            result.append(save_id.lstrip("ChemSpider ID"))
            driver.find_element_by_id("ctl00_ctl00_ContentSection_ContentPlaceHolder1_RecordViewDetails_rptDetailsView_ctl00_ThumbnailControl1_save").click()


path="C:\\Users\\mhzha\\Desktop\\data\\1.xlsx"
df=pd.read_excel(path,sheet_name="Sheet1")

names=[]
for i in range(len(df)):
    names.append(df.ix[i][0])

    
for name in names:
    print(name)
    driver = mols1(dri,name)
    
print("-------------")
for re in result0:
    print(re)
    
for re in result:
    print(re)

def newFN(fileN):
    i=0
    for re in result:
        if re==fileN:
            return names[i]
        i = i+1
    return "NONONONONONONO"
    
    
path = "C:\\Users\\mhzha\\Desktop\\data\\mol1"

FileList = os.listdir(path)
for files in FileList:
    print("fileList============")
    #'原来的文件路径'
    oldDirPath = os.path.join(path, files)
    #'文件名'
    fileName = os.path.splitext(files)[0]
    newFileName = newFN(fileName)
    #'文件扩展名'
    fileType = os.path.splitext(files)[1]
    #'新的文件路径'
    newDirPath = os.path.join(path, newFileName + fileType)
    #'重命名'
    os.rename(oldDirPath, newDirPath)
