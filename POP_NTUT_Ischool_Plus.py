# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:25:31 2020

@author: user
"""
import time
from selenium.webdriver.support.ui import Select 
from bs4 import BeautifulSoup
import POP_moving_file_once as mvo
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
import copy


def choose_class(ntut):
  time.sleep(3)
  ntut.wait()
  #output select
  strJs = """//print_class_name
function print_class_name(){
    var arrClass_Name = new Array() ;
    var window_top = window.top ;
    var moocSysbar = window_top.document.getElementById("moocSysbar").contentWindow ;
    var select = moocSysbar.document.getElementById("selcourse") ;
    for( i = 0 ; i < select.length ; i++ ){
        arrClass_Name.push(select[i].text) ;
    
        //debug
        //console.log(select[i].text) ; 
    }
    return arrClass_Name ;
}

return print_class_name() ;
"""
  lisOption = list()
  lisOption = ntut.driver.execute_script(strJs)
  
  #debug
  #print(lisOption)
  
  for strOp in lisOption :
    print(strOp)
  ntut.wait()
  
  #input class name
  print(f"{ntut.strName} 想要下載的文件是上述課程中的哪一個呢？\n貼心提醒：可以複製貼上即可省去打字時間喔！")
  strClass_Name = input()
  #strClass_Name = "1081_中級會計學_266828"
  time.sleep(3)
  strJs = """//choose class
var arrClass_Name = new Array() ;
var window_top = window.top ;
var moocSysbar = window_top.document.getElementById("moocSysbar").contentWindow ;
var select = moocSysbar.document.getElementById("selcourse") ;
select[""" +  str(lisOption.index(strClass_Name) )  + """].selected = true ;
select.onchange() ;
""" 
  
  ntut.driver.execute_script(strJs) 
  ntut.wait()
  time.sleep(3)
  print("即將轉入頁面" , strClass_Name) 
  return strClass_Name


def select_class_content(ntut , strClass_Name ):
  ntut.wait()
  strJs = """//choose select_class_content (SYS_04_01_002)
var window_top = window.top ;
var moocSysbar = window_top.document.getElementById("moocSysbar").contentWindow ;
moocSysbar.document.getElementById("SYS_04_01_002").click() ;  
  """
  ntut.driver.execute_script(strJs)
  
  #beta
  print("目前功能為下載北科 i 學園所有課程資料（不含影片），未來可能更新，謝謝！")
  
  
def show_document(ntut , strClass_Name):
  
  #important use time.sleep can be web loading css
  time.sleep(3)
  ntut.driver.switch_to.parent_frame()  
  wait(ntut.driver ,10).until(EC.frame_to_be_available_and_switch_to_it(ntut.driver.find_element_by_id("s_catalog")))  
  wait(ntut.driver ,10).until(EC.frame_to_be_available_and_switch_to_it(ntut.driver.find_element_by_id("pathtree")))
  elems = ntut.driver.find_elements_by_tag_name("a")
  strClass_Name = strClass_Name.split('_')[1]
  lis_elems = list()
  for i in range(0, len(elems)):
    lis_elems.append(strClass_Name + '-' + elems[i].text)
  
  #go go iframe("s_main")
  time.sleep(3)
  ntut.driver.switch_to.default_content()
  wait(ntut.driver ,10).until(EC.frame_to_be_available_and_switch_to_it(ntut.driver.find_element_by_id("s_main")))  
  time.sleep(3)

  print("""檔案下載中...
因每位使用者的網速不同 請稍待片刻
目前下載的文件課程名稱與網址將會呈現在下方
""")
  for i in range(0, len(lis_elems) ) :
    if("[錄]" in lis_elems[i] ) :
      continue 
    if( mvo.duplicate(ntut.strPath , lis_elems[i]) ):
      print( "已擁有" , lis_elems[i] )
      continue
    ntut.driver.execute_script("""
var window_top = window.top ;
var html_Pathtree = window_top.document.getElementById("s_catalog").contentWindow.document.getElementById("pathtree").contentWindow;
var launchActivity = html_Pathtree.document.getElementsByTagName('a');
launchActivity[ """ +  str(i)  + " ].onclick();")
    time.sleep(3)
    print( "下載中..." , lis_elems[i] )
    document_download(ntut , lis_elems[i])
  print(f"""下載完成！謝謝 {ntut.strName} 使用""")


def document_download(ntut , strFile_Name ):
  #js to downlaod
  strJs = r"""
//ischool plus download 
var window_top = window.top ;
var html_s_main = window_top.document.getElementById("s_main").contentWindow;
var s_main_title = html_s_main.document.getElementsByTagName('title')[0];

//debug
//s_main_title.text;

if (s_main_title.text == "臺北科技大學(NTUT) " ){
    html_s_main.document.getElementsByTagName("button")[0].onclick() ;
}
else{
    var s_main_script = html_s_main.document.getElementsByTagName('script');
    var arrScript = new Array() ;
        arrScript = s_main_script[0].text.split("var DEFAULT_URL   = '");
        strUrl_Pdf = arrScript[1].split("';")[0] ;
        strUrl_Pdf = "https://istudy.ntut.edu.tw/learn/path/" + strUrl_Pdf ;

        //download pdf 
        var downloadLink = document.createElement('a');
        downloadLink.href = strUrl_Pdf ;
        downloadLink.download = 'david';
        downloadLink.click();        
}
""" 
  
  ntut.driver.execute_script(strJs)
  ntut.wait()
  mvo.rename(ntut.strPath , strFile_Name)
  time.sleep(1)
  



def thanks():
  print("""感謝高鈺成、洪嘉偉在困難時給予幫助
感謝CDSN、stackoverflow、selenium-python中文文檔、
iT邦幫忙、程式前沿、itread01、灰藍.github
「透過網頁給予我技術幫助」""")  
