from selenium.webdriver.common.by import By
import time

base_url = "http://127.0.0.1:8000/checkout/"


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        self.first_name = "first_name"
        self.last_name = "last_name"
        self.address = "address"
        self.city = "city"
        self.division = "division"
        self.zip = "zip"
        self.country = "country"
        self.transaction = "transaction_id"
        self.note = "order_note"
        self.submit = "/html/body/div/form/div[8]/button"
        self.processing = "/html/body/div/div[2]/table/tbody/tr/td[1]"
        self.division_warning = "/html/body/div/div/div/span"
        self.city_warning = "/html/body/div/div/div/span"
        self.transaction_warning = "/html/body/div/div/div"

    def get_first_name(self):
        return self.driver.find_element(By.ID, self.first_name)

    def get_last_name(self):
        return self.driver.find_element(By.ID, self.last_name)

    def get_address(self):
        return self.driver.find_element(By.ID, self.address)

    def get_city(self):
        return self.driver.find_element(By.ID, self.city)

    def get_division(self):
        return self.driver.find_element(By.ID, self.division)

    def get_zip(self):
        return self.driver.find_element(By.ID, self.zip)

    def get_country(self):
        return self.driver.find_element(By.ID, self.country)

    def get_transaction(self):
        return self.driver.find_element(By.ID, self.transaction)

    def get_note(self):
        return self.driver.find_element(By.ID, self.note)

    def get_submit(self):
        return self.driver.find_element(By.XPATH, self.submit)

    def get_processing(self):
        return self.driver.find_element(By.XPATH, self.processing)

    def get_division_warning(self):
        return self.driver.find_element(By.XPATH, self.division_warning)

    def get_city_warning(self):
        return self.driver.find_element(By.XPATH, self.city_warning)

    def get_transaction_warning(self):
        return self.driver.find_element(By.XPATH, self.transaction_warning)

    def fill_checkout(self, first_name, last_name, address, city, division, zip, country, transaction, note):
        # time.sleep(2)
        # self.get_navbar().click()
        self.get_first_name().send_keys(first_name)
        self.get_last_name().send_keys(last_name)
        self.get_address().send_keys(address)
        self.get_city().send_keys(city)
        self.get_division().send_keys(division)
        self.get_zip().send_keys(zip)
        self.get_country().send_keys(country)
        self.get_transaction().send_keys(transaction)
        self.get_note().send_keys(note)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.get_submit().click()

    def order_successful(self):
        return self.get_processing().is_displayed()

    def check_division_warning(self):
        time.sleep(1)
        actual_message = self.get_division_warning().text
        return actual_message == "Sorry, Division can't contain a number"


    def check_city_warning(self):
        time.sleep(1)
        actual_message = self.get_city_warning().text
        return actual_message == "Sorry, City can't contain number"

    def check_transaction_warning(self):
        time.sleep(1)
        actual_message = self.get_transaction_warning().text
        return actual_message == "Sorry, transaction Id already exits."



    @staticmethod
    def get_base_url():
        return base_url


