# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:08:56 2018

@author: hello
"""

import requests as res 
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


url='http://www.room-reservation.lib.ecnu.edu.cn:8081/clientweb/m/ic2/default.aspx?version=3.00.20161208'
path='D:\project\selenium\geckodriver'
driver = webdriver.Firefox(executable_path =path)
driver.get(url)

driver.find_element_by_id("username").clear
driver.find_element_by_id("username").send_keys("51174500004")
driver.find_element_by_id("password").clear
driver.find_element_by_id("password").send_keys("han1990yan")
driver.find_element_by_link_text("登录").click()

time.sleep(1)

driver.find_element_by_link_text("预约空间").click()
values="中北校区单人间C"
rooms=["421","422","423","424","425","426","427","428","429","411","412"
       ,"413","414","415"]

name=values+rooms[0]

driver.find_element_by_link_text("中北校区单人间C421").click()