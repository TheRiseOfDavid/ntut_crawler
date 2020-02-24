# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:48:53 2020

@author: user
"""

class account():
  def __init__(self):
    self.strName = "使用者"
    self.strAccount = ""
    self.strPassWord = ""
    self.strPath = r".\element\\"
    self.strFile = r"account.txt"
    self.lisLines = list()
    
    
  def search_file(self , strEdit_Mode):
    with open(self.strPath + self.strFile , "r" , encoding = "utf-8") as f:
      self.lisLines = f.readlines()
    if(len(self.lisLines) and strEdit_Mode == "0"):
      self.__read_data()
    else:
      self.__key_in()
    return ""
  
  
  def __read_data(self):
    print("檔案存在")
    self.strName = self.lisLines[0].strip()
    self.strAccount = self.lisLines[1].strip()
    self.strPassWord = self.lisLines[2].strip()
    print( self.strName , "歡迎使用\n帳戶為" , self.strAccount)
    print("帳戶：" , self.strAccount)
    print("密碼：" , self.strPassWord)
  
  
  def __key_in(self):
    print("""檔案不存在...正在建立中
    
請輸入你的北科入口網站帳戶
    
    """)
    self.strAccount = input()
    print("請輸入你的北科入口帳戶密碼\n")
    self.strPassWord = input()
    print("資料處理中...\n")
    
    with open(self.strPath + self.strFile , "w" , encoding = "utf-8") as f:
      f.write("使用者\n")
      f.write(self.strAccount + '\n')
      f.write(self.strPassWord)
    print("創建成功！ \n重新導向至輸入畫面")
    self.search_file("0")
  
  
  def modify_user_name(self):
    with open(self.strPath + self.strFile , "w" , encoding = "utf-8") as f:
        f.writelines([self.strName + '\n' , self.strAccount + '\n' , self.strPassWord + '\n'])
    