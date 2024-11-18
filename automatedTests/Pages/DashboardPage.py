from selenium.webdriver.common.by import By
import time

base_url = "http://127.0.0.1:8000/dashboard/"

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

        self.home = "//*[@id=\"navbarResponsive\"]/div/a[1]"


    def get_home(self):
        return self.driver.find_element(By.XPATH, self.home)


    def go_menu(self):
        self.get_home().click()





    @staticmethod
    def get_base_url():
        return base_url


