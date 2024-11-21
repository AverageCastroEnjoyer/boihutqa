import os

from automatedTests.Pages import HomePage
from automatedTests.Pages.HomePage import HomePage

from automatedTests.Pages import CheckoutPage
from automatedTests.Pages.CheckoutPage import CheckoutPage



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
class CheckoutPageTests(unittest.TestCase):

    def setUp(self):
        # Configuración inicial, se ejecuta una sola vez antes de todas las pruebas
        self.driver = webdriver.Chrome()  # Cambia a tu controlador deseado
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")



    def tearDown(self):
        self.driver.quit()



#53
    def test_buy_book(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        home_page.buy_book_now()

        cart_page = CartPage(driver)
        cart_page.buy_book()

        checkout_page = CheckoutPage(driver)

        checkout_page.fill_checkout("Marco", "Solis", "Esparza", "Puntarenas", "Primero", "38458", "Costa Rica", "322", "Casa cafe")
        self.assertTrue(checkout_page.order_successful())


#54
    def test_buy_nologin(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)

        home_page.buy_book_now()

        cart_page = CartPage(driver)
        cart_page.buy_book()

        self.assertTrue(cart_page.check_warning())


#55
    def test_division_as_number(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        home_page.buy_book_now()

        cart_page = CartPage(driver)
        cart_page.buy_book()

        checkout_page = CheckoutPage(driver)

        checkout_page.fill_checkout("Marco", "Solis", "Esparza", "Puntarenas", "1", "38458", "Costa Rica", "483", "Casa cafe")
        self.assertTrue(checkout_page.check_division_warning())

#56
    def test_city_as_number(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        home_page.buy_book_now()

        cart_page = CartPage(driver)
        cart_page.buy_book()

        checkout_page = CheckoutPage(driver)

        checkout_page.fill_checkout("Marco", "Solis", "Esparza", "2", "Primero", "38458", "Costa Rica", "454", "Casa cafe")
        self.assertTrue(checkout_page.check_city_warning())


#57
    def test_invalid_transaction(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("marco@gmail.com", "marco")

        dashboard_page = DashboardPage(driver)
        dashboard_page.go_menu()

        home_page.buy_book_now()

        cart_page = CartPage(driver)
        cart_page.buy_book()

        checkout_page = CheckoutPage(driver)

        checkout_page.fill_checkout("Marco", "Solis", "Esparza", "2", "Primero", "38458", "Costa Rica", "322", "Casa cafe")
        self.assertTrue(checkout_page.check_transaction_warning())


"""
if __name__ == "__main__":
    unittest.main()
