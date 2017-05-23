from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome('C:/Users/vaibh/Desktop/vaibhavahuja/projects/chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
target = "the name of contact or group "

string = "add your message here"
y_arg = '//*[@id="side"]/div[2]/div/label/input'
input_y = wait.until(EC.presence_of_element_located((
    By.XPATH, y_arg)))
input_y.send_keys(target + Keys.ENTER)

inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(70):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(0.04)