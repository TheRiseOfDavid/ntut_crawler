# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 01:25:29 2020

@author: user
"""
import os
import time


def duplicate(strPath , Data ):
  lisDir = os.listdir(strPath)
  dicAll_Data = dict()
  strData = ""
  if(type(Data) == dict):
    dicAll_Data = Data     
    for strFile in lisDir :
      strFile_Name = strFile.rsplit("." , 1)[0]
      if(strFile_Name in dicAll_Data.keys()):
          del dicAll_Data[strFile_Name]
    return dicAll_Data    
  elif (type(Data) == str):
    #debug
    #print(Data)
    
    strData = Data
    for strFile in lisDir:
      strFile_Name = strFile.rsplit("." , 1)[0]
      if(strData == strFile_Name):
        return 1
    return 0


def rename(strPath , strFile_New_Name):
  #debug 
  #strPath = r"C:\Users\user\Downloads" 
  #strNew_Path = r"D:\program\tool program\Download_NTUT_Imfornation_Learning_Course_Files\download"
  
  strFile_Old_Name = ""
  isOk = 1
  while(isOk):
    isOk = 0
    time.sleep(2)
    lisDir = os.listdir(strPath)
    for strFile_Name in lisDir:
      if ".crdownload" in strFile_Name:
        isOk = 1
        break
      
    #debug
    #print(isOk)
    #print(strFile_Name)
  
  lisDir = os.listdir(strPath)
  lisFile_Name = list()
  strFile_Old_Name = ""
  strFile_Type = ""
  for strFile_Name in lisDir:
    if(strFile_Name[0:14].isdigit() or strFile_Name == r"'ebook.pdf'"):
      lisFile_Name = strFile_Name.rsplit('.',1)
      #debug
      #print(lisFile)
      #print(4)
      
      strFile_Old_Name = lisFile_Name[0]
      strFile_Type = lisFile_Name[1].replace("'" , "")
      time.sleep(3)
      isOk = 1 
      while(isOk):
        try:
          #because 'ebook.pdf' , pdf' != strFile_Type
          os.rename( rf"{strPath}\{strFile_Old_Name}.{lisFile_Name[1]}" , \
                    rf"{strPath}\{strFile_New_Name}.{strFile_Type}")
          isOk = 0
        except:
          time.sleep(3)
          return rename(strPath , strFile_New_Name)
      time.sleep(3)
      break



