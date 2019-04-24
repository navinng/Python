import os,shutil
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#url = 'https://www.thenomadhotel.com/'
url = 'https://www.adda52.com/'
driver = webdriver.Chrome('D:\chromedriver')
iterations = 0
driver.get(url)
while iterations < 10 :
    html = driver.execute_script("return document.documentElement.outerHTML")
    selsoup = BeautifulSoup(html,'html.parser')
    images = (selsoup.findAll('img', { 'class' : 'img-responsive'}))
    imagelist = []
    for image in images :
        image_url = image['src']
        imagelist.append(image_url)
    
    for image in imagelist :
        try :
            file = os.path.basename(image)
            path = os.path.join(os.getcwd(), 'images', file)
            print(path)
            img_r = requests.get(image, stream = True)
            with open(path,'wb') as currentimage:
                shutil.copyfileobj(img_r.raw, currentimage)
                del img_r
        except:
            pass
  
    iterations += 1
    time.sleep(5)
   
driver.close()

