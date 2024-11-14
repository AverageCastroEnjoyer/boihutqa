from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
menu = driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/p[2]/a[2]")
time.sleep(2)
menu.click()

time.sleep(10)





#driver.quit()