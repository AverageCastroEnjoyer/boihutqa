from selenium.webdriver.common.by import By
import time

base_url = "http://127.0.0.1:8000/"

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.navbar = ".navbar-toggler"
        self.user = "//*[@id=\"navbarResponsive\"]/div/li[2]/a"
        self.login = "//*[@id=\"navbarResponsive\"]/div/li[2]/ul/li[1]/a"
        self.register = "//*[@id=\"navbarResponsive\"]/div/li[2]/ul/li[2]/a"



    def get_navbar(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.navbar)

    def get_user(self):
        return self.driver.find_element(By.XPATH, self.user)

    def get_login(self):
        return self.driver.find_element(By.XPATH, self.login)

    def get_register(self):
        return self.driver.find_element(By.XPATH, self.register)



    def click_navbar(self):
        self.get_navbar().click()

    def click_user(self):
        self.get_user().click()

    def click_register(self):
        self.get_register().click()

    def open_register(self):
        self.get_user().click()
        self.get_register().click()
        time.sleep(1)

    def open_login(self):
        self.get_user().click()
        self.get_login().click()
        time.sleep(0.4)





    @staticmethod
    def get_base_url():
        return base_url


