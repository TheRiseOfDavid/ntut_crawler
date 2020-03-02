#coding=utf-8  
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import base64
import pytesseract
from PIL import Image 

d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
browser = webdriver.Chrome(desired_capabilities=d)
browser.get('https://nportal.ntut.edu.tw/index.do')
js = """var codeImage = document.querySelector("#authImage");

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

#test
'''
js = 'var codeImage = document.querySelector("#authImage");async function getCodeImageDataURL(codeImage) {var canvasForCloneCodeImage = document.createElement("canvas");var canvasContextForCloneCodeImage = canvasForCloneCodeImage.getContext("2d");await new Promise(returnCodeImageLoaded => {var codeImageLoaded = codeImage.complete;if (codeImageLoaded) returnCodeImageLoaded();else codeImage.addEventListener("load", returnCodeImageLoaded);});canvasContextForCloneCodeImage.drawImage(codeImage, 0, 0);return canvasForCloneCodeImage.toDataURL();}await getCodeImageDataURL(codeImage);'


js ='var downloadLink = document.createElement("a");\
downloadLink.href = "https://nportal.ntut.edu.tw/authImage.do?datetime=1579534099865";\
downloadLink.download = "r.jpg";\
downloadLink.click();'

js = "return document.title"
'''


browser.implicitly_wait(30)
img_data = browser.execute_script(js)

#test
#print(img_data)

head, data = img_data.split(',', 1)
file_ext = head.split(';')[0].split('/')[1]
plain_data = base64.b64decode(data)

with open('./element/' + "image." + file_ext ,"wb") as f:
  f.write(plain_data)
  
if __name__ == "__main__":
  pass
else:
  pass


