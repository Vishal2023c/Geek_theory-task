from selenium import webdriver
from selenium.webdriver.common.by import By  
import time

username="chouhanvishal6609@gmail.com"
password="@sgsvchouhan"

driver=webdriver.Chrome()
driver.get("https://replit.com/")
driver.find_element(By.XPATH,"//a[@role='link']").click()

driver.find_element(By.XPATH,"//a[@role='button']").click()
driver.find_element(By.XPATH,"//input[@aria-label='Email']").send_keys(username)
driver.find_element(By.XPATH,"//input[@aria-label='Password']").send_keys(password)
driver.find_element(By.XPATH,"//button[@type='submit']").click()

print("logging succesfully !")
time.sleep(240)