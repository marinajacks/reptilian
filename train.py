#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:37:38 2018

@author: macbook
火车票数据爬取
"""


import requests
from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

url='https://kyfw.12306.cn/otn/leftTicket/init'

path='/Users/macbook/downloads/geckodriver'

urls = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
driver = webdriver.Firefox(executable_path =path)
    
s=driver.get(url)

driver.find_element_by_id('fromStationText').clear()

driver.find_element_by_id('fromStationText').send_keys("fuyang")

driver.find_element_by_id('fromStationText').send_keys(Keys.ENTER)

driver.find_element_by_id('toStationText').clear()

driver.find_element_by_id('toStationText').send_keys("shanghainan")

driver.find_element_by_id('toStationText').send_keys(Keys.ENTER)

driver.find_element_by_id('date_icon_1').click()

driver.find_element_by_id('date_icon_1').send_keys(Keys.ENTER)


driver.find_element_by_id('query_ticket').click()



def traininfo(froms,to):
    driver.find_element_by_id('fromStationText').clear()
    
    driver.find_element_by_id('fromStationText').send_keys(froms)
    
    driver.find_element_by_id('fromStationText').send_keys(Keys.ENTER)
    
    driver.find_element_by_id('toStationText').clear()
    
    driver.find_element_by_id('toStationText').send_keys(to)
    
    driver.find_element_by_id('toStationText').send_keys(Keys.ENTER)
    
    driver.find_element_by_id('train_date')
    
    
    driver.find_element_by_id('query_ticket').click()


def test():
    froms='fuyang'
    to='hangzhou'
    traininfo(froms,to)