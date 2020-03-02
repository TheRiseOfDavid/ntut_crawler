# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:51:36 2020

@author: user
"""
import os


def open_file(isEdit):
  strPath = r".\element\\"
  strFile = r"account.txt"
  strFile_Data = ""
  with open(strPath + strFile , "r" , encoding = "utf-8") as f:
    strFile_Data = f.read()
  if(strFile_Data != "" and isEdit == 0 ):
    print("檔案存在")
    
    #test
    #tup = read_data(strPath , strFile)  
    #print(tup)
    #return tup
  
    return read_data(strPath , strFile)  
  else:
    strAccount = ""
    strPassWord = ""
    print("""檔案不存在...正在建立中
    
請輸入你的北科入口網站帳戶
    
    """)
    strAccount = input()
    print("請輸入你的北科入口帳戶密碼\n")
    strPassWord = input()
    print("資料處理中...\n")
    
    #create strPath
    if not os.path.isdir(strPath):
      os.mkdir(strPath)
      
    with open(strPath + strFile , "w" , encoding = "utf-8") as f:
      f.write("使用者\n")
      f.write(strAccount + '\n')
      f.write(strPassWord)
      
    print("創建成功！ \n重新導向至輸入畫面")
    return open_file(0)
  
  
def read_data(strPath , strFile):
  strAccount = ""
  strPassWord = ""
  strUser = ""
  with open(strPath + strFile , "r" , encoding = "utf-8") as f:
    #remove \n  
    strUser = f.readline().replace("\n" , "")
    strAccount = f.readline().replace("\n" , "")
    strPassWord = f.readline().replace("\n" , "")
  print( strUser , "歡迎使用\n帳戶為" , strAccount)
  print("帳戶：" , strAccount)
  print("密碼：" , strPassWord)
  
  return ( strUser , strAccount , strPassWord)


def modify_user_name(strUser):
  strPath = r".\element\\"
  strFile = r"account.txt"
  with open(strPath + strFile , "r+" , encoding = "utf-8") as f:
      f.write(strUser)
        

def main():
  pass
  
  
if __name__ == "__main__":
  pass