# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 00:55:41 2020

@author: user
"""

#from selenium import webdriver 
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import base64
import os

def download_captcha(driver , strPath):
  strJs = """var codeImage = document.querySelector("#authImage");

async function getCodeImageDataURL(codeImage) {
    var canvasForCloneCodeImage = document.createElement("canvas");
    var canvasContextForCloneCodeImage = canvasForCloneCodeImage.getContext("2d");
    
    await new Promise(returnCodeImageLoaded => {
        var codeImageLoaded = codeImage.complete;
        if (codeImageLoaded) returnCodeImageLoaded();
        else codeImage.addEventListener("load", returnCodeImageLoaded);
    });

    canvasContextForCloneCodeImage.drawImage(codeImage, 0, 0);
    return canvasForCloneCodeImage.toDataURL();
}
return getCodeImageDataURL(codeImage);
"""
  strImg_data = driver.execute_script(strJs)
  strHead, strData = strImg_data.split(',', 1)
  file_ext = strHead.split(';')[0].split('/')[1]
  base64_data = base64.b64decode(strData)

  with open( strPath + r"/image." + file_ext ,"wb") as f:
    f.write(base64_data)
  

def Delete_captcha(strPath):
  os.remove(strPath + r'\image.png')

  
if __name__ == "__main__":
  pass
else:
  pass
  