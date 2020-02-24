# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 01:25:29 2020

@author: user
"""
import os
import time


def duplicate(strPath , dicAll_Data ):
  lisDir = os.listdir(strPath)
  for strFile in lisDir:
    strFile_Name = strFile.rsplit("." , 1)[0]
    if(strFile_Name in dicAll_Data.keys()):
        del dicAll_Data[strFile_Name]
  return dicAll_Data      
      

def rename(strPath , strFile_New_Name):
  #debug 
  #strPath = r"C:\Users\user\Downloads" 
  #strNew_Path = r"D:\program\tool program\Download_NTUT_Imfornation_Learning_Course_Files\download"
  strFile_Old_Name = ""
  isOk = 1
  while(isOk):
    isOk = 0
    time.sleep(1)
    lisDir = os.listdir(strPath)
    for strFile_Name in lisDir:
      if ".crdownload" in strFile_Name:
        isOk = 1
        break
      
    #debug
    #print(isOk)
    #print(strFile_Name)
  
  lisDir = os.listdir(strPath)
  lisFile = list()
  strFile_Old_Name = ""
  strFile_Type = ""
  for strFile_Name in lisDir:
    if(strFile_Name[0:14].isdigit()):
      lisFile = strFile_Name.rsplit('.',1)
      
      #debug
      #print(lisFile)
      
      strFile_Old_Name = lisFile[0]
      strFile_Type = lisFile[1]
      break
    
  time.sleep(2)
  if(not strFile_New_Name[0:14].isdigit()):
    isOk = 1 
    while(isOk):
      try:
        os.rename( rf"{strPath}\{strFile_Old_Name}.{strFile_Type}" , \
                  rf"{strPath}\{strFile_New_Name}.{strFile_Type}")
        isOk = 0
      except:
        return rename(strPath , strFile_New_Name)
  time.sleep(2)



