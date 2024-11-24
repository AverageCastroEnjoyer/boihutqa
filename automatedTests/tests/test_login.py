import os

from automatedTests.Pages import HomePage
from automatedTests.Pages.HomePage import HomePage
from automatedTests.Pages import LoginPage
from automatedTests.Pages.LoginPage import LoginPage
from automatedTests.Pages import DashboardPage
from automatedTests.Pages.DashboardPage import DashboardPage

import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import warnings


warnings.simplefilter("ignore", ResourceWarning)

###
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
    def test_null_email_without_at_char_login(self):
        driver = self.driver
        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("invalido", "invalido1")

        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", login_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "Incluye un signo \"@\" en la dirección de correo electrónico. La dirección \"invalido\" no incluye el signo \"@\".")

#26
    def test_no_text_before_at_char_login(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("@gmail.com","invalido1")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", login_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "Ingresa texto antes del signo \"@\". La dirección \"@gmail.com\" está incompleta.")
#27
    def test_no_text_after_at_char_login(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("invalido@","invalido1")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", login_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "Ingresa texto después del signo \"@\". La dirección \"invalido@\" está incompleta.")

#28
    def test_wrong_password_login(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("UsedEmail@test.com","invalid")
                

        # Obtener el texto del mensaje
        message_text = login_page.get_message_text()
        # Hacer el assert del mensaje
        self.assertEqual(message_text, "Sorry your Email/Password don't match")

#29
    def test_unused_email_login(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("correoNoUsado@gmail.com","contrasenaNoUsada")
                

        # Obtener el texto del mensaje
        message_text = login_page.get_message_text()
        # Hacer el assert del mensaje
        self.assertEqual(message_text, "Sorry your Email/Password don't match")

#29 (2) (hay 2 29 repetidos.)
    def test_succesful_login(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("UsedEmail@test.com","truepassword12")
                
        # Esperar que la página redirija a la página de login (10 segundos de espera)
        WebDriverWait(driver, 10).until(EC.url_to_be("http://127.0.0.1:8000/dashboard/"))

        # Verificar que la URL actual es la de la página de login
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/dashboard/")

        dashboard_page = DashboardPage(driver)

        # Obtener el texto del mensaje
        message_text = dashboard_page.get_message_text()

        # Hacer el assert del mensaje
        self.assertEqual(message_text, "You have been logged in.")

#30
    def test_special_char_after_at_char_login(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("valido@invalido#.com","invalido1")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", login_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "El texto después del signo \"@\" no debe incluir el símbolo \"#\".")

#31
    def test_email_ends_dot_login(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_login()
        login_page = LoginPage(driver)

        login_page.login_fill("valido@invalido.","invalido1")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", login_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "El signo \".\" está colocado en una posición incorrecta en \"invalido.\".")
###

if __name__ == "__main__":
    unittest.main()
