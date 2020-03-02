# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 20:52:41 2020

@author: user
"""
import os
from selenium import webdriver
import copy
import threading

thrLocal = getattr( threading.local() , "drvier" , None )
driver = webdriver.Chrome( r".\element\chromedriver.exe" )
driver.get("https://onlinejudge.org/")
copy_driver = copy.deepcopy(driver)
copy_driver.get("https://www.op.gg/champion/swain/statistics/support")
print(copy_driver.find_element_by_class_name("champion-stats__single__item").text)
print(driver.find_element_by_class_name("contentheading").text)


    
   