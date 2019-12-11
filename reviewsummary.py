import time
import os
import re
from random import randint
from selenium import webdriver
# available since 2.4.0
from selenium.webdriver.support.ui import WebDriverWait
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#Wait
def findrestaurant(chrome,element,method):
    try:
        element = WebDriverWait(chrome, 8).until(
            EC.presence_of_element_located((method, element))
        )

        return element
    except:
        return False

def findrestaurant2(chrome,element,method):
    try:
        element = WebDriverWait(chrome, 8).until(
            EC.presence_of_all_elements_located((method, element))
        )

        return element
    except:
        return False



# 建立 driver
driver = webdriver.Chrome()

# 去 google 首頁

driver.get("https://www.google.com.tw/maps/place/%E4%BA%95%E7%94%BA%E8%94%AC%E9%A3%9F%E6%96%99%E7%90%86/@24.165912,120.6851393,17z/data=!4m15!1m9!2m8!1z6aSQ5buz!3m6!1z6aSQ5buz!2zNDA05Y-w5Lit5biC5YyX5Y2A5bSH5b636Lev5LiA5q61NjMx6Jmf!3s0x346917de9efffd69:0x98ca9ba87b45b8f2!4m2!1d120.684873!2d24.1674817!3m4!1s0x346917dc076a996f:0x33fcc55bdfbe5c41!8m2!3d24.1683258!4d120.6833872")
time.sleep(3)

#往下滾動視窗
js="var q=document.getElementsByClassName('widget-pane-content scrollable-y')[0].scrollTop=900"
driver.execute_script(js)
time.sleep(3)

#平均星級
avestar=findrestaurant(driver,"//div[@class='jqnFjrOWMVU__right']/div",By.XPATH)
print(avestar.text)

#總評論數
allcomamount=findrestaurant(driver,"//div[@class='jqnFjrOWMVU__right']/button",By.XPATH)
print(allcomamount.text)

# 各星級評論
allbars=findrestaurant2(driver,"//*[@class='jqnFjrOWMVU__bucket-background']/div[@aria-label]",By.XPATH)
for b in range(len(allbars)):
     print("{}星級:{}".format(5-b,allbars[b].get_attribute("aria-label")))

#評論摘要(Review summary)
allrs=""
rs=findrestaurant2(driver,"//div[@class='section-review-snippet-line']/span",By.XPATH)
for r in rs:
    rtext=r.text
    allrs+=rtext

rsplit=allrs.split('"')
for r in rsplit:
    print(r)
