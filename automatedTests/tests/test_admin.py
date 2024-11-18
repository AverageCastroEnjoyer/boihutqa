import os

from automatedTests.Pages import HomePage
from automatedTests.Pages.HomePage import HomePage

from automatedTests.Pages import CartPage
from automatedTests.Pages.CartPage import CartPage

from automatedTests.Pages import AdminPage
from automatedTests.Pages.AdminPage import AdminPage

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


class AdminPageTests(unittest.TestCase):

    def setUp(self):
        # Configuración inicial, se ejecuta una sola vez antes de todas las pruebas
        self.driver = webdriver.Chrome()  # Cambia a tu controlador deseado
        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/admin/")



    def tearDown(self):
        self.driver.quit()

    #58
    def test_login(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())
        self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")
        self.assertTrue(admin_page.login_successful())

    #59
    def test_login_invalid(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())
        self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admi")
        self.assertTrue(admin_page.login_unsuccesful())


    #60 Manual

    #61 Manual

    #62
    def test_modify_order(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.change_order_status()
        self.assertTrue(admin_page.check_order_saved())

    # 63
    def test_modify_user(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.change_user()
        self.assertTrue(admin_page.check_account_saved())

   # 64
    def test_mark_unavailable(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.mark_book_unavailable()
        self.assertTrue(admin_page.check_book_saved())


    # 65
    def test_check_history(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.check_history()
        self.assertTrue(admin_page.check_history_opened())


    # 66
    def test_change_invoice(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.change_invoice()
        self.assertTrue(admin_page.check_invoice_saved())



   # 67
    def test_no_image_category(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.add_book_info("Game", "game", "Scott", "fiction", "40", "25")
        self.assertTrue(admin_page.check_book_no_category_image())

    # 68
    def test_invalid_values(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.add_book_info("Game", "game", "Scott", "fiction", "a", "e")
        self.assertTrue(admin_page.check_book_no_category_image())


# 68 Manual

#69 Manual

    # 70
    def test_delete_category(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.delete_category_task()
        self.assertTrue(admin_page.check_deleted_category())


    # 71
    def test_delete_book(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.delete_book_task()
        self.assertTrue(admin_page.check_deleted_book())

    # 72
    def test_delete_account(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.delete_account_task()
        self.assertTrue(admin_page.check_deleted_account())


   # 73
    def test_change_category_desc(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.change_category_task()
        self.assertTrue(admin_page.check_changed_category())

# 74
    def test_add_admin(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.add_account_task("juliangarcia", "Julian", "Garcia", "juliang", "2843274", "juliangarcia@gmail.com")
        self.assertTrue(admin_page.check_new_account())


# 75
    def test_logout(self):
        driver = self.driver
        # self.driver.get(HomePage.get_base_url())

        admin_page = AdminPage(driver)
        admin_page.fill_login("admin@gmail.com", "admin")

        admin_page.logout_task()
        self.assertTrue(admin_page.check_logout())









if __name__ == "__main__":
    unittest.main()
