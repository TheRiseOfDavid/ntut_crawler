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

def wait_and_collect_file(strPath):
  lisFile_Name = list()
  while(1):
    isOK = 1
    lisDir = os.listdir(strPath)
    for strFile_Name in lisDir:
      #while(isOK == 0):  
      #debug
      print(strFile_Name)
      
      if ".crdownload" in strFile_Name:
        time.sleep(1)
        isOK = 0
        if(not strFile_Name in lisFile_Name):
          strFile_Name = strFile_Name.rsplit('.')[0]
          
          #debug 
          print(strFile_Name)
          
          lisFile_Name.append(strFile_Name)
        
        break
      
    if(isOK):
      break
    
  print("檔案下載成功！")
  return lisFile_Name

def rename(strPath , lisFile_Old_Name , lisFile_New_Name):
  #debug 
  #strPath = r"C:\Users\user\Downloads" 
  #strNew_Path = r"D:\program\tool program\Download_NTUT_Imfornation_Learning_Course_Files\download"

  
  lisDir = os.listdir(strPath)
  for strFile in lisDir :
    
    if (strFile in lisFile_Old_Name):
      os.rename()  
    

    #for each move lisFile
    for strFile in lisFile:
      if(strFile in strFp):
        
        #test
        #print(strOld_Name)
        
        strNew_Name = strFile + strOld_Name[strOld_Name.rfind(".")::]
        
        #test
        #print(strNew_Name)
        
        os.rename(strPath + strOld_Name , strPath + strNew_Name)
        strFp = os.path.join(strPath , strNew_Name)
        #test 
        print("正在移動檔案" , strFp)
        
        strNew_Fp = os.path.join(strNew_Path , os.path.basename(strFp))
        shutil.move(strFp , strNew_Fp)

  print("移動完成")


if __name__ == "__main__":
  print("請輸入你要移動的檔案檔名")
  lisFile = list()
  lisFile.append(input())
  search(lisFile)
