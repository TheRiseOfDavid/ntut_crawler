# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:47:11 2020

@author: user
"""

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import warnings
import logging
import copy


class browser():
  def __init__(self ):
    self.options = webdriver.ChromeOptions()
    self.capability = None
    self.strPath = ""
    self.prefs = {'profile.default_content_settings.popups': 0, "profile.default_content_setting_values.automatic_downloads":1 , 'download.default_directory': self.strPath}
    self.driver = None
  
  
  def setup(self , strPath):
    self.strPath = strPath
    self.prefs['download.default_directory'] = self.strPath
    self.options.add_experimental_option('prefs', self.prefs)
    self.driver = webdriver.Chrome( r".\element\chromedriver.exe" , chrome_options=self.options , desired_capabilities = self.capability)
  
  
  def headless(self):
    self.options.add_argument('--headless')
    self.options.add_argument('--disable-gpu')
  
  
  def wait(self):
    self.driver.implicitly_wait(30)
    
  
  def quit(self):
    self.driver.quit()
   

  def ignore_loggings(self):
    self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    
  def add_loggings(self):
    self.capability = DesiredCapabilities.CHROME
    self.capability["loggingPrefs"] =  { 'browser':'ALL' }
    