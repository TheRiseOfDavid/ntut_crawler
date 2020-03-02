# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 00:48:42 2020

@author: user
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select 
from bs4 import BeautifulSoup
import POP_download_NTUT_captcha_picture as captcha
from POP_OCR_NTUT_captcha import parsing_captcha
import time
import POP_moving_file_once as mvo
import POP_account_imformation as ai

def input_path():
  print("請輸入下載檔案的放入位置,如需更改帳密請輸入1")
  strPath = r"%s" % input()
  if(strPath == "1"):
    ai.open_file(1)
    print("修改完成！\n現在請你輸入輸入下載檔案的放入位置")
    strPath = r"%s" % input()
  return strPath

def wait(driver):
  driver.implicitly_wait(30)
 
def init_download_file_options(strPath):
  options = webdriver.ChromeOptions()
  prefs = {'profile.default_content_settings.popups': 0, "profile.default_content_setting_values.automatic_downloads":1 , 'download.default_directory': strPath}
  options.add_experimental_option('prefs', prefs)
  driver = webdriver.Chrome( r".\element\chromedriver.exe" , chrome_options=options)
  print("準備進入北科入口網站")
  strUrl = "https://nportal.ntut.edu.tw/index.do"
  driver.get(strUrl)
  return driver


def input_account_information(strUser ,driver , strPath , strAccount , strPassWord):
  wait(driver)
  
  #input Account
  elem = driver.find_element_by_id("muid")
  elem.send_keys(strAccount)
  
  #input PassWord
  elem = driver.find_element_by_id("mpassword")
  elem.send_keys(strPassWord)

  #input Captcha
  elem = driver.find_element_by_id('authcode')
  captcha.download_captcha(driver , strPath)
  elem.send_keys(parsing_captcha(strPath)) 
  captcha.Delete_captcha(strPath)
  print(f"""由於OCR圖像辨識目前不太準確，還請 {strUser} 幫忙確認謝謝！！
大衞之後會改進的，非常抱歉
如果驗證碼辨識正確請輸入1，辨識失敗請輸入0
警告：請不要操控網頁上的按鈕介面
""")
  
  isRight = int(input())
  if (isRight == 0):
    print("請查看網頁後並在程式端輸入驗證碼\n提醒：請不要操控網頁上的按鈕介面")
    driver.find_element_by_id('authcode').clear()
    elem.send_keys(input())
  
  #login
  elem = driver.find_element_by_class_name('l_icon01')
  elem.click()
  
  return driver


def modify_user_name(driver):
  wait(driver)
  strUser = driver.find_element_by_class_name("words").text
  strUser = strUser.strip()
  strUser = strUser.replace(" " , "")
  print(strUser)
  strUser = strUser.replace("歡迎您" , "")
  return strUser[1::]


def go_ischool(driver):
  #go_system_academic_affairs
  wait(driver)
  elem = driver.find_element_by_partial_link_text("教務系統")
  elem.click()
  
  #go_ischool
  elem = driver.find_element_by_partial_link_text("北科 i 學園")
  elem.click()
  
  return driver
  

def ischool_select(strUser , driver):
  #ischool select
  lisOption = list()
  lisWindows = driver.window_handles
  
  #debug
  #print(lisWindows)
  
  #selenium control ischool
  driver.switch_to.window(lisWindows[1])
  time.sleep(3)
  select = Select(driver.find_element_by_name("city"))  
  
  #output select
  for op in select.options:
    lisOption.append(op.text)
    print(op.text)
  wait(driver)
  
  #input class name
  print(f"{strUser} 想要下載的文件是上述課程中的哪一個呢？\n貼心提醒：可以複製貼上即可省去打字時間喔！")
  strClass_Name = input()
  select.select_by_visible_text(strClass_Name)
  print("即將轉入頁面" , strClass_Name)
  
  return driver


def class_select(strUser , driver):
  wait(driver)
  elem = driver.find_element_by_id('courseToolListBlock')
  print(elem.text)
  
  dicNTUT_Ischool_Class_Item = dict()
  dicNTUT_Ischool_Class_Item["Course homepage"] = "courseHomePage"
  dicNTUT_Ischool_Class_Item["Course description"] = "CLDSC"
  dicNTUT_Ischool_Class_Item["Agenda"] = "CLCAL"
  dicNTUT_Ischool_Class_Item["Announcement"] = "CLANN"
  dicNTUT_Ischool_Class_Item["Document"] = "CLDOC"
  dicNTUT_Ischool_Class_Item["Mediacenter"] = "INWICAST"
  dicNTUT_Ischool_Class_Item["Exercises"] = "CLQWZ"
  dicNTUT_Ischool_Class_Item["Learning Path"] = "CLLNP"
  dicNTUT_Ischool_Class_Item["Assignments"] = "CLWRK"
  dicNTUT_Ischool_Class_Item["Forums"] = "CLFRM"
  dicNTUT_Ischool_Class_Item["Groups"] = "CLGRP"
  dicNTUT_Ischool_Class_Item["Users"] = "CLUSR"  
  
  #gold
  #print("使用者您好，請問你要使用甚麼功能呢？")
  #strNTUT_Ischool_Class = input()
  
  #beta
  print(f"""由於開發功能目前只能夠下載\"document\"內的所有資料
將馬上為您轉入document，非常謝謝 {strUser} 使用
大衞也會加緊腳步加速開發其他功能""")
  strNTUT_Ischool_Class = "Document"
  
  wait(driver)
  elem = driver.find_element_by_id(dicNTUT_Ischool_Class_Item[strNTUT_Ischool_Class])
  elem.click()
  wait(driver)
  
  return driver


def download_document( strUser , strPath , driver  ):
  #catch all herf
  wait(driver)
  soup = BeautifulSoup(driver.page_source , "html.parser" )
  strText = ""
  dicAll_Data= dict()
  links_tr = soup.find_all("tr")
  for link_tr in links_tr:
    isI = True
    links_td = link_tr.find_all('td')
    
    for link_td in links_td :
      if(isI):
        isI = False
        strText = link_td.text
      else:
        links_a = link_td.find_all('a')
        
        for link_a in links_a:
          dicAll_Data[strText] = "https://ischool.ntut.edu.tw" + link_a['href']
  
  #output all download document name
  print("""檔案下載中...
因每位使用者的網速不同 請稍待片刻
目前下載的文件課程名稱與網址將會呈現在下方
""")
  
  mvo.duplicate(strPath , dicAll_Data)
  
  #js to downlaod
  for it in dicAll_Data.items():
    #debug
    #print(it[1] , it[0] , sep='\n')
    
    strJs = f"""
    var downloadLink = document.createElement('a');
    downloadLink.href = '{it[1]}';
    downloadLink.download = '{it[0]}';
    downloadLink.click();
    """ 
    driver.execute_script(strJs)
    wait(driver)
    print("下載中..." , it[0])
    mvo.rename(strPath , it[0])
    time.sleep(1)
  
  print(f"下載完成！謝謝 {strUser} 使用")
  return list(dicAll_Data.keys())

  
def quit(driver):
  driver.quit()
  
  
if __name__ == "__main__":
  pass
else:
  pass