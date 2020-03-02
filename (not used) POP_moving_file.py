# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:41:39 2020

@author: user
"""

import os
import os.path
import shutil
import sys
import time

def wait(strPath):
  while(1):
    isOK = 1
    lisDir = os.listdir(strPath)
    for strFile_Name in lisDir:      
      if ".crdownload" in strFile_Name:
        time.sleep(1)
        isOK = 0
        break 
    if(isOK):
      break
  print("檔案下載成功！")
  
def rename(strPath , lisFile_New_Name):
  #debug 
  #strPath = r"C:\Users\user\Downloads" 
  #strNew_Path = r"D:\program\tool program\Download_NTUT_Imfornation_Learning_Course_Files\download"

  
  lisDir = os.listdir(strPath)
  for strFile in lisDir :
    strFile_New_Name = lisFile_New_Name[0]
    del lisFile_New_Name[0]
    if(strFile[0:14:].isdigit()):
      print(strFile)
        #os.rename( rf"{strPath}\{strFile}" , \
        #            rf"{strPath}\{strFile_New_Name}.{strFile.rsplit('.')[1]}")



if __name__ == "__main__":
  rename(r"D:\program\tool program\Download_NTUT_Imfornation_Learning_Course_Files\download", \
         ["201909180846311225儼馬產業裴技軟.pdf" , "201909180828320918台鑿民卡國.pdf" ], \
         ["1225鐵馬產業與社會" , "0918台灣民主國"])
  
  
  pass
