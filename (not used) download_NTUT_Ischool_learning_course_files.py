# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:32:20 2020

@author: user
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select 
from bs4 import BeautifulSoup

def download_file(strAccount , strPassWord):  
  print("請輸入下載檔案的放入位置")
  strPath = r"%s" % input()
  options = webdriver.ChromeOptions()
  prefs = {'profile.default_content_settings.popups': 0, "profile.default_content_setting_values.automatic_downloads":1 , 'download.default_directory': strPath}
  options.add_experimental_option('prefs', prefs)
  driver = webdriver.Chrome(chrome_options=options)
  strUrl = "https://nportal.ntut.edu.tw/index.do"
  driver.get(strUrl)

  #input Account
  elem = driver.find_element_by_id("muid")
  elem.send_keys(strAccount)
  
  #input PassWord
  elem = driver.find_element_by_id("mpassword")
  elem.send_keys(strPassWord)

  #input Captcha
  elem = driver.find_element_by_id('authcode')
  elem.send_keys(input())

  #login
  elem = driver.find_element_by_class_name('l_icon01')
  elem.click()

  #auto captcha input
  '''
  #Captcha Processing

  soup = BeautifulSoup(driver.page_source,'html.parser')
  page = driver.page_source
  lisPage = page.split('\n')
  print(lisPage[215])
  
  for items in soup.find_all('img'):
    if 'src' in items.attrs:
      
      image = requests.get("https://nportal.ntut.edu.tw/" + items['src']) 
      with open('./element/' + str(index) + ".jpg","wb") as f:
        f.write(image.content)
        index +=1

  #input Captcha
  pytesseract.pytesseract.tesseract_cmd = r'D:\program\tool program\Download_NTUT_Imfornation_Learning_Course_Files\element\Tesseract-OCR\tesseract.exe'
  image = Image.open('./element/7.jpg')
  image_String = pytesseract.image_to_string(image)
  print(image_String)
  '''
  
  #go System of Academic Affairs
  elem = driver.find_element_by_partial_link_text("教務系統")
  elem.click()

  #go ischool
  
  #debug
  '''
  #elem = driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div[1]/div[0]/div[1]/div[0]/div[0]/div[0]/ul/li[3]/a/herf") 
  #                                               主內容開始      功能框開始
  
  #elem = driver.find_element_by_xpath("//div[@class='eip3_box']/div[@class='dijitContentPane boxContent']/div[@class='aptreeBgColor']/div[@class='aptree']/ul[0]/li[1]/div/ul/li[4]/span/a")
  
  #elem = driver.find_element_by_id("ap-aa")
  '''
  
  driver.implicitly_wait(30)
  elem = driver.find_element_by_partial_link_text("北科 i 學園")
  #elem = driver.find_element_by_xpathch("/html/body/div[@id='mainContainer']/div[@id='floatingBoxParentContainer']/div[@id='Column2']/div[@id='box_aptree']/div/div/div[@id='div_aptreeContent']/table/tbody/tr/td/div[@class='aptreeBgColor']/div[@id='divStandaptree']/ul/li[2]/div/ul/li[4]/span/a")
  elem.click()

  # ischool select
  lisOption = list()
  lisWindows = driver.window_handles
  
  #selenium control ischool
  driver.switch_to.window(lisWindows[1])
  select = Select(driver.find_element_by_name("city"))  
  #debug
  #print(driver.current_url)
  
  for op in select.options:
    lisOption.append(op.text)
    print(op.text)
  
  #strInput = input()
  
  driver.implicitly_wait(30)
  #strClass = u"%s" % strInput
  
  #test 
  strClass = u"%s" % "1081_程式設計(ㄧ)_263166"
  
  select.select_by_visible_text(strClass)
  
  # go ischool class
  
  driver.implicitly_wait(30)
  elem = driver.find_element_by_id('courseToolListBlock')
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
  
  #test
  strNTUT_Ischool_Class = "Document"
  
  #strNTUT_Ischool_Class = input()
  driver.implicitly_wait(30)
  elem = driver.find_element_by_id(dicNTUT_Ischool_Class_Item[strNTUT_Ischool_Class])
  elem.click()
  driver.implicitly_wait(30)
  document_download(driver)
  

def document_download(driver):
  
  #elem = driver.find_elements_by_class_name(' item')
  
  strClick_Path = r"/html/body/div[@id='claroPage']/div[@id='claroBody']/div[@class='tabbedCourse']/div[@class='courseContent']/div[@id='courseRightContent']/table[@class='claroTable emphaseLine']/tbody"
  elem = driver.find_element_by_xpath(strClick_Path)
  driver.implicitly_wait(30)
  
  #elem = driver.find_element_by_xpath(strClick_Path + "/tr[" + str(i) + "]/td[2]/a/small/img" )
  #elem.click()
  soup = BeautifulSoup(driver.page_source , "html.parser" )
  
  #debug
  #print(driver.page_source)
  
  #links = soup.select(strClick_Path + r"/tr[" + str(i) + r"]/td[2]/a/herf")
  
  #test
  #links = soup.select("html body div#claroPage div#claroBody div[@class='tabbedCourse'] div[@class='courseContent'] div[@id='courseRightContent'] table[@class='claroTable emphaseLine'] tbody tr[" + str(i) + "]")
  #lisLinks_a = soup.find_all("a" , class_="item")
  
  strText = ""
  lisAll_Data= list()
  links_tr = soup.find_all("tr")
  for link_tr in links_tr:
    isI = True
    links_td = link_tr.find_all('td')
    
    #test
    #print(links_td)
    
    for link_td in links_td :
      if(isI):
        isI = False
        strText = link_td.text
      else:
        links_a = link_td.find_all('a')
        
        #test
        #print(links_a)
        
        for link_a in links_a:
          lisAll_Data.append([strText, "https://ischool.ntut.edu.tw" + link_a['href']])
   
  #test     
  print(lisAll_Data)
         
  #debug      
  #print(link.get("href"))
  #href = link.get("href")

  lisFile = list()
  for it in lisAll_Data:
    
    strJs_Code_To_Download = f"""
    var downloadLink = document.createElement('a');
    downloadLink.href = '{it[1]}';
    downloadLink.download = "";\
    downloadLink.click();
    """
    
    
    #test
    '''
    #it[1] == file URL it[0] == file name
    strJs_Code_To_Download = 'var downloadLink = document.createElement("a");\
downloadLink.href = "'+ it[1] + '";\
downloadLink.download = "1.pptx";\
downloadLink.click();'
    '''
    
    driver.execute_script(strJs_Code_To_Download)
    lisFile.append(it[0])
    driver.implicitly_wait(30)
    
    #test
    '''
    strJs_Code_To_Download = 'var downloadLink = document.createElement("a");\
downloadLink.href = "https://ischool.ntut.edu.tw/learning/backends/download.php?url=LzIwMTkwOTEwMTk0NzMwY2gwNl93ZWIucGRm&cidReset=true&cidReq=266828";\
downloadLink.download = "' + str(index) + '.pdf";\
downloadLink.click();' 
  '''  
    
  #url 
  #"https://ischool.ntut.edu.tw/learning/backends/download.php?url=LzIwMTkwOTEwMTk0NzMwY2gwNl93ZWIucGRm&cidReset=true&cidReq=266828"
  
  #test
  #print(lisFile)

  #move_file not use because the file name on the internet is different from \
  # file name on the download 
  #move_file(lisFile)
  
  
  #test
  '''
  strJs_Code_To_Download = f"""
    var downloadLink = document.createElement('a');
    downloadLink.href = 'https://ischool.ntut.edu.tw//learning/backends/download.php?url=LzIwMTkxMjE5MTcyNzAzw%2F6nT71tst%2FDRC5kb2N4&cidReset=true&cidReq=263166';
    downloadLink.click();
    """
  driver.execute_script(strJs_Code_To_Download)
  ''' 

def main():
  download_file("108AB0008" , "a63126312")


if(__name__ == "__main__"):
  main()