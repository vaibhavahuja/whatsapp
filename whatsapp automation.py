from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/vaibh/Desktop/vaibhavahuja/projects/chromedriver.exe')
driver.get("http://web.whatsapp.com")
try:
    element = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.CLASS_NAME,"input"))
    )
finally:
    name = driver.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input')
    name.send_keys("Personal"+Keys.ENTER)

try:
    element = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH,'//div[@class="input"][@dir="auto"][@data-tab="1"]'))
    )
finally:
    message = driver.find_element_by_xpath('//div[@class="input"][@dir="auto"][@data-tab="1"]')
    for i in range(10):
        message.send_keys("hello" + Keys.ENTER)

