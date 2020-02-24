# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:47:11 2020

@author: user
"""

from selenium import webdriver
import warnings
import logging


class browser():
  def __init__(self ):
    self.options = webdriver.ChromeOptions()
    self.strPath = ""
    self.prefs = {'profile.default_content_settings.popups': 0, "profile.default_content_setting_values.automatic_downloads":1 , 'download.default_directory': self.strPath}
    self.driver = None
  
  
  def setup(self , strPath):
    self.strPath = strPath
    self.prefs['download.default_directory'] = self.strPath
    self.options.add_experimental_option('prefs', self.prefs)
    self.driver = webdriver.Chrome( r".\element\chromedriver.exe" , chrome_options=self.options)
  
  
  def headless(self):
    self.options.add_argument('--headless')
    self.options.add_argument('--disable-gpu')
  
  
  def wait(self):
    self.driver.implicitly_wait(30)
    
  
  def quit(self):
    self.driver.quit()
    

  def ignore_loggings(self):
    self.options.add_experimental_option('excludeSwitches', ['enable-logging'])