# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:58:26 2020

@author: user
"""

from OOP_account_imformation import account 
from OOP_NTUT  import NTUT
from OOP_whispers_of_love import whispers
from OOP_browser import browser
#import POP_NTUT_Ischool_Old as Ischool
import POP_NTUT_Ischool_Plus as Ischool
import time
import os


def edit_account(user):
  strChoose = "0"
  while(strChoose.isdigit()):
    user.search_file(strChoose)
    print("請輸入下載檔案的放入位置,如需更改帳密請輸入1")
    strChoose = r"%s" % input()
    if( not os.path.isdir(strChoose) and strChoose != "1" ):
      print("路徑不存在，請重新輸入！")
      strChoose = "0"
  return strChoose  


def main():
  user = account()
  whisper = whispers()
  strPath = edit_account(user)
  ntut = NTUT( strPath , user.strName)
  #ntut.headless()
  ntut.ignore_loggings()
  ntut.setup(strPath)
  whisper.random_love()
  whispers.say_patient_to_user()
  while(ntut.login(user)): pass
  user.strUser = ntut.edit_user_name()
  ntut.system_choice("教務系統")
  #ntut.system_choice("北科i學園（舊版）")
  ntut.system_choice("北科i學園PLUS")
  ntut.go_to_other_web()
  whisper.random_love()
  whispers.say_patient_to_user()
  strClass_Name = Ischool.choose_class(ntut)
  Ischool.select_class_content(ntut , strClass_Name )
  Ischool.document_download(ntut , strClass_Name )
  #ntut.quit()
  Ischool.thanks()
  print("程式即將在 5 秒後自動關閉，謝謝您的使用")
  time.sleep(5)


if __name__ == "__main__":
  main()
else:
  pass