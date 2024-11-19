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
        self.cart = "//*[@id=\"navbarResponsive\"]/div/a[3]"
        self.hero = "/html/body/section/div/div/div/div[1]/p[1]"
        self.buy_now = "/html/body/section/div/div/div/div[1]/p[2]/a[1]"
        self.buy_now2 = "/html/body/div/div/div[2]/a/button"
        self.add = "/html/body/section/div[1]/div[1]/div[2]/div[2]/div/a"
        self.out_of_stock = "/html/body/div/div/div[1]/a/button"
        self.btn_out_of_stock = "/html/body/section/div[1]/div[1]/div[2]/div[2]/div/button"


    def get_navbar(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.navbar)

    def get_user(self):
        return self.driver.find_element(By.XPATH, self.user)

    def get_login(self):
        return self.driver.find_element(By.XPATH, self.login)

    def get_register(self):
        return self.driver.find_element(By.XPATH, self.register)

    def get_cart(self):
        return self.driver.find_element(By.XPATH, self.cart)

    def get_hero(self):
        return self.driver.find_element(By.XPATH, self.hero)

    def get_buy_now(self):
        return self.driver.find_element(By.XPATH, self.buy_now)

    def get_buy_now2(self):
        return self.driver.find_element(By.XPATH, self.buy_now2)

    def get_add(self):
        return self.driver.find_element(By.XPATH, self.add)

    def get_out_of_stock(self):
        return self.driver.find_element(By.XPATH, self.out_of_stock)

    def get_btn_out_of_stock(self):
        return self.driver.find_element(By.XPATH, self.btn_out_of_stock)



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


    def open_cart(self):
        self.get_cart().click()
        time.sleep(0.4)

    def hero_text_is_there(self):
        actual_message = self.get_hero().text
        return actual_message == "Buy your favorite books from our huge list of collection. You will get your product delivered to your doorsteps in 24 hours."

    def buy_book_now(self):
        self.get_buy_now().click()
        self.get_buy_now2().click()
        self.get_add().click()

    def buy_out_of_stock(self):
        self.get_buy_now().click()
        self.get_out_of_stock().click()
        current_url = self.driver.current_url
        self.get_btn_out_of_stock().click()
        time.sleep(2)
        return self.driver.current_url == current_url









    @staticmethod
    def get_base_url():
        return base_url


