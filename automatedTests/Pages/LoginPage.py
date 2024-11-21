from selenium.webdriver.common.by import By
import time

base_url = "http://127.0.0.1:8000/login"

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = "id_email"
        self.password = "id_password"
        self.submit_login = "/html/body/div/div[2]/form/div/button"
        self.message = "/html/body/div/div[1]/div/span"

    def get_email(self):
        return self.driver.find_element(By.ID, self.email)

    def get_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_submit_login(self):
        return self.driver.find_element(By.XPATH, self.submit_login)

    def get_message(self):
        return self.driver.find_element(By.XPATH, self.message)
    
    def get_message_text(self):
        return self.get_message().text

    def login_fill(self, email, password):
        #self.get_navbar().click()
        self.get_email().send_keys(email)
        self.get_password().send_keys(password)
        time.sleep(1)
        self.get_submit_login().click()
        time.sleep(1.5)

    @staticmethod
    def get_base_url():
        return base_url


