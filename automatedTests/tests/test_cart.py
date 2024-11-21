import os

from automatedTests.Pages import HomePage
from automatedTests.Pages.HomePage import HomePage

from automatedTests.Pages import CartPage
from automatedTests.Pages.CartPage import CartPage

from automatedTests.Pages import DashboardPage
from automatedTests.Pages.DashboardPage import DashboardPage
from automatedTests.Pages import RegisterPage
from automatedTests.Pages.RegisterPage import RegisterPage
import time
import unittest
from selenium import webdriver
import warnings
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from automatedTests.Pages import LoginPage
from automatedTests.Pages.LoginPage import LoginPage

warnings.simplefilter("ignore", ResourceWarning)
"""

class CartPageTests(unittest.TestCase):

    def setUp(self):
        # Configuración inicial, se ejecuta una sola vez antes de todas las pruebas
        self.driver = webdriver.Chrome()  # Cambia a tu controlador deseado
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")



    def tearDown(self):
        self.driver.quit()

#47
    def test_check_cart(self):
        driver = self.driver

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        home_page.open_cart()

        cart_page = CartPage(driver)

        self.assertTrue(cart_page.cart_opened())

#48
    def test_continue_shopping(self):
        driver = self.driver

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        home_page.open_cart()

        cart_page = CartPage(driver)
        cart_page.go_continue_shopping()

        self.assertTrue(home_page.hero_text_is_there())


#49
    def test_add_book(self):
        driver = self.driver

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        home_page.buy_book_now()

        cart_page = CartPage(driver)
        self.assertTrue(cart_page.book_is_there())

#50
    def test_modify_quantity(self):
        driver = self.driver

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        home_page.buy_book_now()

        cart_page = CartPage(driver)
        cart_page.add_input()

        self.assertTrue(cart_page.check_value())


#51
    def test_delete_book(self):
        driver = self.driver

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        home_page.buy_book_now()

        cart_page = CartPage(driver)
        cart_page.delete_book()

        self.assertTrue(cart_page.check_empty_cart())


#52
    def test_out_of_stock(self):
        driver = self.driver

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        self.assertTrue(home_page.buy_out_of_stock())

"""
if __name__ == "__main__":
    unittest.main()
