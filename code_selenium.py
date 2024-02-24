from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Chrome()
driver.get('https://www.smartprix.com/mobiles')
time.sleep(2)
link= driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
link.click()
time.sleep(2)
link2= driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
link2.click()
time.sleep(2)


old_height= driver.execute_script('return document.body.scrollHeight')
print(old_height)
while True:
    link3= driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[1]/div[2]/div[3]')
    link3.click()
    time.sleep(1.5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(new_height)
    if new_height==old_height:
        break
    old_height = new_height

html= driver.page_source
with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)

