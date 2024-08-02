from selenium import webdriver
from amazoncaptcha import AmazonCaptcha
from selenium.webdriver.common.by import By  
import time

username="9589335699"
password="Vishal@95"

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")

driver.find_element(By.XPATH,"//*[@id='nav-link-accountList-nav-line-1']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='ap_email']").send_keys(username)
driver.find_element(By.XPATH,"//*[@id='continue']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='ap_password']").send_keys(password)
driver.find_element(By.XPATH,"//*[@id='signInSubmit']").click()
print("logging succesfully !")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("laptop 2024")
driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()
time.sleep(20)
