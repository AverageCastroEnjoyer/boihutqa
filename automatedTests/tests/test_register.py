import os

from automatedTests.Pages import HomePage
from automatedTests.Pages.HomePage import HomePage

from automatedTests.Pages import RegisterPage
from automatedTests.Pages.RegisterPage import RegisterPage
import time
import unittest
from selenium import webdriver
import warnings
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

warnings.simplefilter("ignore", ResourceWarning)


class HomePageTests(unittest.TestCase):

    def setUp(self):
        # Configuración inicial, se ejecuta una sola vez antes de todas las pruebas
        self.driver = webdriver.Chrome()  # Cambia a tu controlador deseado
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")

        """
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
        # Configuración de Chrome para que no use el modo "headless"
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Para iniciar en pantalla completa
        # Asegúrate de que no se usa `chrome_options.add_argument("--headless")`
        service = Service(DRIVER_BIN)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("http://127.0.0.1:8000/")
        """

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jose", "Perez", "joseperez1", "jose1@gmail.com", "1234", "1234", "12341")
        self.assertTrue(register_page.register_completed())



if __name__ == "__main__":
    unittest.main()
