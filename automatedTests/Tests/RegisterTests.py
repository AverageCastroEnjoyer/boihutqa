import os

from automatedTests.Pages import HomePage
from automatedTests.Pages.HomePage import HomePage

from automatedTests.Pages import RegisterPage
from automatedTests.Pages.RegisterPage import RegisterPage
import time
import unittest
from selenium import webdriver
import warnings

warnings.simplefilter("ignore", ResourceWarning)



class HomePageTests(unittest.TestCase):

    def setUp(self):
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jose", "Perez", "joseperez", "jose@gmail.com", "1234", "1234", "1234")
        self.assertTrue(register_page.register_completed())



if __name__ == "__main__":
    unittest.main()
