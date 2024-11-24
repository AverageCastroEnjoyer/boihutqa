from selenium.webdriver.common.by import By
import time

base_url = "http://127.0.0.1:8000/cart/"

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.continue_shopping = "/html/body/div[2]/div/div/a[1]/button"
        self.checkout = "/html/body/div[2]/div/div/a[2]"
        self.book = "/html/body/div[1]/div/div[1]/a/div"
        self.input = "/html/body/div[1]/div/form/div[1]/b/input"
        self.update = "/html/body/div[1]/div/form/div[3]/button"
        self.delete = "/html/body/div[1]/div/div[3]/a/button"
        self.empty = "/html/body/div[1]/p"
        self.warning = "/html/body/div/div/div/span"




    def get_continue_shopping(self):
        return self.driver.find_element(By.XPATH, self.continue_shopping)

    def get_checkout(self):
        return self.driver.find_element(By.XPATH, self.checkout)

    def get_book(self):
        return self.driver.find_element(By.XPATH, self.book)

    def get_input(self):
        return self.driver.find_element(By.XPATH, self.input)

    def get_update(self):
        return self.driver.find_element(By.XPATH, self.update)

    def get_delete(self):
        return self.driver.find_element(By.XPATH, self.delete)

    def get_empty(self):
        return self.driver.find_element(By.XPATH, self.empty)

    def get_warning(self):
        return self.driver.find_element(By.XPATH, self.warning)


    def go_continue_shopping(self):
        self.get_continue_shopping().click()
        time.sleep(0.5)

    def cart_opened(self):
        actual_message = self.get_continue_shopping().text
        return actual_message == "Continue Shopping"


    def book_is_there(self):
        return self.get_book().is_displayed()

    def add_input(self):
        self.get_input().clear()
        self.get_input().send_keys('2')
        self.get_update().click()
        time.sleep(0.5)

    def check_value(self):
        value = self.get_input().get_attribute("value")
        return value == "2"


    def delete_book(self):
        self.get_delete().click()
        time.sleep(0.5)

    def check_empty_cart(self):
        actual_message = self.get_empty().text
        return actual_message == "Your cart is empty"

    def buy_book(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.get_checkout().click()
        time.sleep(0.5)

    def check_warning(self):
        actual_message = self.get_warning().text
        return actual_message == "You need to be registered to place an order"


    @staticmethod
    def get_base_url():
        return base_url


