import pytesseract
from PIL import Image


def parsing_captcha(strPath):
  pytesseract.pytesseract.tesseract_cmd = r'.\element\Tesseract-OCR\tesseract.exe'
  image = Image.open( strPath + r'\image.png').convert("L")
  img2 = image.crop((0, 0, 120, 40))
  
  #test
  #img2.show()
  
  tessdata_dir_config = r'--tessdata-dir ".\element\Tesseract-OCR\tessdata"'
  strCode= pytesseract.image_to_string(img2 , lang="eng")
  strCode = strCode.replace(" " , "")
  #os.remove(r'.\element\image.png')
  return strCode





if __name__ == "__main__":
  parsing_captcha()
else:
  pass