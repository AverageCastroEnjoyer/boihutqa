from selenium.webdriver.common.by import By
import time

base_url = "http://127.0.0.1:8000/register"

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        self.first_name = "//*[@id=\"first_name\"]"
        self.last_name = "last_name"
        self.username = "username"
        self.submit_login = "/html/body/div/form/div/button"
        self.submit_successful = "/html/body/div/div[1]/div/span"


    def get_first_name(self):
        return self.driver.find_element(By.XPATH, self.first_name)

    def get_last_name(self):
        return self.driver.find_element(By.ID, self.last_name)

    def get_username(self):
        return self.driver.find_element(By.ID, self.username)

    def get_email(self):
        return self.driver.find_element(By.ID, 'email')

    def get_password(self):
        return self.driver.find_element(By.ID, "password")

    def get_confirm_password(self):
        return self.driver.find_element(By.ID, "confirm_password")

    def get_phone(self):
        return self.driver.find_element(By.ID, "phone")

    def get_submit_login(self):
        return self.driver.find_element(By.XPATH, self.submit_login)




    def register_fill(self, first_name, last_name, username, email, password, confirm_password, phone):
        #time.sleep(2)
        #self.get_navbar().click()
        self.get_first_name().send_keys(first_name)
        self.get_last_name().send_keys(last_name)
        self.get_username().send_keys(username)
        self.get_email().send_keys(email)
        self.get_password().send_keys(password)
        self.get_confirm_password().send_keys(confirm_password)
        self.get_phone().send_keys(phone)
        time.sleep(2)
        self.get_submit_login().click()
        time.sleep(2)

    def register_completed(self):
        element = self.driver.find_element(By.XPATH, self.submit_successful)
        return element.is_displayed()

    @staticmethod
    def get_base_url():
        return base_url


