# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:38:06 2020

@author: user
"""

from POP_OCR_NTUT_captcha import parsing_captcha
import POP_download_NTUT_captcha_picture as captcha
from OOP_browser import browser
import time
import sys


class NTUT(browser):
  def __init__(self, strPath , strName):
    super(NTUT , self).__init__()
    self.strUrl = "https://nportal.ntut.edu.tw/index.do"
    self.strName = strName
    self.strPath = strPath
    
    
  def login(self , user ):
    self.driver.get(self.strUrl)
    self.wait()
    #self.is_maintenance()
    
    #input Account
    elem = self.driver.find_element_by_id("muid")
    elem.send_keys(user.strAccount)
    
    #input PassWord
    elem = self.driver.find_element_by_id("mpassword")
    elem.send_keys(user.strPassWord)
    
    #input Captcha
    elem = self.driver.find_element_by_id('authcode')
    captcha.download_captcha(self.driver , self.strPath)
    strCaptcha = parsing_captcha(self.strPath)
    if(strCaptcha == ""):
      strCaptcha = "1"
    elem.send_keys(strCaptcha)
    captcha.Delete_captcha(self.strPath)
    

    
    '''
    print(f"""由於OCR圖像辨識目前不太準確，還請 {self.strName} 幫忙確認謝謝！！
大衞之後會改進的，非常抱歉
如果驗證碼辨識正確請輸入1，辨識失敗請輸入0
警告：請不要操控網頁上的按鈕介面
""")
    
    isRight = int(input())
    if (isRight == 0):
      print("請查看網頁後並在程式端輸入驗證碼\n提醒：請不要操控網頁上的按鈕介面")
      self.driver.find_element_by_id('authcode').clear()
      elem.send_keys(input())
    '''    
    
    #maintenance
    self.is_maintenance()
    
    #login
    elem = self.driver.find_element_by_class_name('l_icon01')
    elem.click()

    #islogin_right
    if(self.driver.current_url == "https://nportal.ntut.edu.tw/login.do"):
      elem = self.driver.find_element_by_tag_name('center').text
      if( "「驗證碼」輸入錯誤" in elem ):
        return 1 
      else:
        print("帳號密碼輸入錯誤，請重新開啟程式輸入正確帳密，謝謝 !")
        time.sleep(5)
        sys.exit() 
    return 0
 
    
  def edit_user_name(self):
    self.strName = self.driver.find_element_by_class_name("words").text
    self.strName = self.strName.strip()
    self.strName = self.strName.replace(" " , "")
    print(self.strName)
    self.strName = self.strName.replace("歡迎您" , "")
    return self.strName
  
  
  def system_choice(self , strSystem):
    self.wait()
    elem = self.driver.find_element_by_partial_link_text(strSystem)
    elem.click()
    
  
  def go_to_other_web(self):
    lisWindows = self.driver.window_handles
    self.driver.switch_to.window(lisWindows[1])
    
    
  def is_maintenance(self):
    time.sleep(1)
    if(self.driver.find_element_by_class_name('notice').text == "載入中..."):
      print("系統例行維護中，請過5分鐘再連線。")
      time.sleep(5)
      sys.exit()
    
  

    