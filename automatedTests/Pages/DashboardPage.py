from selenium.webdriver.common.by import By
import time

base_url = "http://127.0.0.1:8000/dashboard/"

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.home = "//*[@id=\"navbarResponsive\"]/div/a[1]"
        self.message = "/html/body/div/div[2]/div[1]/div/span"

    def get_home(self):
        return self.driver.find_element(By.XPATH, self.home)

    def get_message(self):
        return self.driver.find_element(By.XPATH, self.message)
    
    def get_message_text(self):
        return self.get_message().text
    
    def go_menu(self):
        self.get_home().click()





    @staticmethod
    def get_base_url():
        return base_url


