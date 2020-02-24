# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:25:31 2020

@author: user
"""
import time
from selenium.webdriver.support.ui import Select 
from bs4 import BeautifulSoup
import POP_moving_file_once as mvo


def choose_class(ntut):
  time.sleep(3)
  ntut.driver.switch_to.frame("mooc_sysbar")
  select = Select(ntut.driver.find_element_by_id("selcourse"))
  
  #output select
  lisOption = list()
  for op in select.options:
    lisOption.append(op.text)
    print(op.text)
  ntut.wait()
  
  #input class name
  print(f"{ntut.strName} 想要下載的文件是上述課程中的哪一個呢？\n貼心提醒：可以複製貼上即可省去打字時間喔！")
  strClass_Name = input()
  select.select_by_visible_text(strClass_Name)
  print("即將轉入頁面" , strClass_Name) 
  return strClass_Name


def select_class_content(ntut , strClass_Name ):
  ntut.wait()
  elem = ntut.driver.find_element_by_id('SYS_04_01_002')
  
  #beta
  print("目前功能為下載北科 i 學園所有課程資料（不含影片），未來可能更新，謝謝！")
  
  elem.click()
  ntut.wait()

  
def document_download(ntut , strClass_Name):
  ntut.driver.back()
  ntut.wait()
  ntut.driver.switch_to.default_content()
  ntut.driver.switch_to.frame("s_catalog")
  #debug
  elem = ntut.driver.find_element_by_id("pathtree")
  elem = elem.get_attribute("src")
  
  #ntut.driver.switch_to.frame("pathtree")
  
  #strClass_Name fetch chinese word
  strClass_Name = strClass_Name.split('_')[1] + '-'
  lisWindows = ntut.driver.window_handles
  ntut.driver.switch_to.window(lisWindows[2])  
  soup = BeautifulSoup(ntut.driver.page_source , "html.parser" )
  
  #debug
  print(soup.text + '\n' )
  
  strText = ""
  dicAll_Data= dict()
  links_li = soup.find_all("li")
  for it in links_li :
    print(it.text + '\n') 
 
  

'''  
  #output all download document name
  print("""檔案下載中...
因每位使用者的網速不同 請稍待片刻
目前下載的文件課程名稱與網址將會呈現在下方
""")
    
  mvo.duplicate(ntut.strPath , dicAll_Data)
  
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
    ntut.driver.execute_script(strJs)
    ntut.wait()
    print("下載中..." , it[0])
    mvo.rename(ntut.strPath , it[0])
    time.sleep(1)
  
  print(f"""下載完成！謝謝 {ntut.strName} 使用
""")
  return list(dicAll_Data.keys())
'''

def thanks():
  print("""感謝高鈺成、洪嘉偉在困難時給予幫助
感謝CDSN、stackoverflow、selenium-python中文文檔、
iT邦幫忙、程式前沿、itread01、灰藍.github
「透過網頁給予我技術幫助」""")  
