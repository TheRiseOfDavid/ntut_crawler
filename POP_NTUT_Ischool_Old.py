# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:43:48 2020

@author: user
"""
import time
from selenium.webdriver.support.ui import Select 
from bs4 import BeautifulSoup
import POP_moving_file_once as mvo
  

def choose_class(ntut):
  time.sleep(3)
  select = Select(ntut.driver.find_element_by_name("city"))
  
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
  elem = ntut.driver.find_element_by_id('courseToolListBlock')
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
  
  #beta
  print(f"""由於開發功能目前只能夠下載\"document\"內的所有資料
將馬上為您轉入document，非常謝謝 {ntut.strName} 使用
大衞也會加緊腳步加速開發其他功能""")
  strNTUT_Ischool_Class = "Document"
  ntut.wait()
  elem = ntut.driver.find_element_by_id(dicNTUT_Ischool_Class_Item[strNTUT_Ischool_Class])
  elem.click()
  ntut.wait()
    
    
def document_download(ntut , strClass_Name):
  ntut.wait()
  
  #strClass_Name fetch chinese word
  strClass_Name = strClass_Name.split('_')[1] + '-'
  soup = BeautifulSoup(ntut.driver.page_source , "html.parser" )
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
          dicAll_Data[strClass_Name + strText] = "https://ischool.ntut.edu.tw" + link_a['href']
  
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


def thanks():
  print("""感謝高鈺成、洪嘉偉在困難時給予幫助
感謝CDSN、stackoverflow、selenium-python中文文檔、
iT邦幫忙、程式前沿、itread01、灰藍.github
「透過網頁給予我技術幫助」""")
    