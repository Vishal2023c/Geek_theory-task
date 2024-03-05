from selenium import webdriver
from selenium.webdriver.common.by import By  
import time

# username="9589335699"
# password="H4523v95"

driver=webdriver.Chrome()

driver.get("https://91club.co.in/")

driver.find_element(By.CSS_SELECTOR,"input[type=\"submit\"]").click()
driver.find_element(By.CSS_SELECTOR," input[type\"div.loginin\"]").click()
# driver.find_element(By.CLASS_NAME,"userNumber").send_keys("9589335699")
# driver.find_element(By.CLASS_NAME,"password").send_keys("H4523v95")
# driver.find_element(By.CSS_SELECTOR,"button .active[data-v-ba1985c0]").click()

print("logging succesfully !")
time.sleep(120)