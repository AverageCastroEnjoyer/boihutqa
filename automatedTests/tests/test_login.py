import os

from automatedTests.Pages import HomePage
from automatedTests.Pages.HomePage import HomePage

from automatedTests.Pages import RegisterPage
from automatedTests.Pages.RegisterPage import RegisterPage

from automatedTests.Pages import LoginPage
from automatedTests.Pages.LoginPage import LoginPage

import unittest
from selenium import webdriver
import warnings
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

warnings.simplefilter("ignore", ResourceWarning)


class LoginTests(unittest.TestCase):

    def setUp(self):
        # Configuración inicial, se ejecuta una sola vez antes de todas las pruebas
        self.driver = webdriver.Chrome()  # Cambia a tu controlador deseado
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")

    def tearDown(self):
        self.driver.quit()
    
    #24
    def test_null_login(self):
        driver = self.driver
        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("", "")

        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", login_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "Completa este campo")

    #25
    def test_null_email_without_at(self):
        driver = self.driver
        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("invalido", "invalido1")

        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", login_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "Incluye un signo \"@\" en la dirección de correo electrónico. La dirección \"invalido\" no incluye el signo \"@\".")

if __name__ == "__main__":
    unittest.main()
