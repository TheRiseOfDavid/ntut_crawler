# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:57:42 2020

@author: user
"""

import POP_account_imformation as ai
import POP_download_NTUT_Ischool_learning_course_files as ntut
import time

def main():
  #account imformation
  tupAccount = ai.open_file(0)
  strUser = tupAccount[0]
  strAccount = tupAccount[1]
  strPassWord = tupAccount[2]
    
  #download ntut file
  strPath = ntut.input_path()
  driver = ntut.init_download_file_options(strPath)
  ntut.input_account_information( strUser , driver , strPath , strAccount , strPassWord)
  strUser = ntut.modify_user_name(driver)
  ai.modify_user_name(strUser)
  ntut.go_ischool(driver)
  ntut.ischool_select( strUser , driver)
  ntut.class_select(strUser , driver)
  ntut.download_document( strUser , strPath , driver)
  
  print("""
謝謝高鈺成提供js支援
謝謝洪嘉偉給予py教學
謝謝cdsn、stackoverflow、selenium-python中文文档、
iT邦幫忙、程式前沿、🐴 的學習筆記、itread01、
灰蓝.github
「透過網頁給予我提供技術幫助」""")
  time.sleep(3)
  ntut.quit(driver)
  print("系統將在5秒後自行關閉")
  time.sleep(5)
  
if __name__ == "__main__":
  main()
else:
  pass