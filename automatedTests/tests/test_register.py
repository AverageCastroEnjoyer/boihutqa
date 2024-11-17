import os
import time
import unittest
import warnings

from automatedTests.Pages import HomePage
from automatedTests.Pages.HomePage import HomePage
from automatedTests.Pages import RegisterPage
from automatedTests.Pages.RegisterPage import RegisterPage
from automatedTests.Pages import LoginPage
from automatedTests.Pages.LoginPage import LoginPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

warnings.simplefilter("ignore", ResourceWarning)

class HomePageTests(unittest.TestCase):

    def setUp(self):
        # Configuración inicial, se ejecuta una sola vez antes de todas las pruebas
        self.driver = webdriver.Chrome()  # Cambia a tu controlador deseado
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")

    def tearDown(self):
        self.driver.quit()
    
    #1
    def test_valid_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin", "gyro@gmail.com", "steelball", "steelball", "501")
        
        # Esperar que la página redirija a la página de login (10 segundos de espera)
        WebDriverWait(driver, 10).until(EC.url_to_be("http://127.0.0.1:8000/login"))

        # Verificar que la URL actual es la de la página de login
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/login")

        login_page = LoginPage(driver)

        # Obtener el texto del mensaje
        message_text = login_page.get_message_text()

        # Hacer el assert del mensaje
        self.assertEqual(message_text, "Your account has been registered. Please Login now")

    #2
    def test_no_first_name_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("", "Zeppeli", "GyroSpin2", "gyro2@gmail.com", "steelball", "steelball", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_first_name())
        #print(f"<{mensaje}>")
        assert(mensaje == "Completa este campo")
        
    #3
    def test_no_last_name_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "", "GyroSpin2", "gyro2@gmail.com", "steelball", "steelball", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_last_name())
        #print(f"<{mensaje}>")
        assert(mensaje == "Completa este campo")

    #4
    def test_no_username_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "", "gyro2@gmail.com", "steelball1", "steelball1", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_username())
        #print(f"<{mensaje}>")
        assert(mensaje == "Completa este campo")

    #5
    def test_no_email_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "", "steelball1", "steelball1", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "Completa este campo")

    #6
    def test_no_password_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "gyro2@gmail.com", "", "", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_password())
        #print(f"<{mensaje}>")
        assert(mensaje == "Completa este campo")

    #7
    def test_no_confirm_password_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "gyro2@gmail.com", "stellball1", "", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_confirm_password())
        #print(f"<{mensaje}>")
        assert(mensaje == "Completa este campo")

    #8
    def test_no_phone_number_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "gyro2@gmail.com", "stellball1", "stellball1", "")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_phone())
        #print(f"<{mensaje}>")
        assert(mensaje == "Completa este campo")

    #9
    def test_no_data_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("", "", "", "", "", "", "")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_first_name())
        #print(f"<{mensaje}>")
        assert(mensaje == "Completa este campo")

    #10 Es manual
    
    #11
    def test_used_phone_number_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "gyro2@gmail.com", "steelball1", "steelball1", "1")
                

        # Obtener el texto del mensaje
        message_text = register_page.get_message_text()
        # Obtener el color del mensaje
        message_color = register_page.get_message().value_of_css_property("color")

        # Asegurarse de que el color sea #842029
        self.assertEqual(message_color, "rgba(132, 32, 41, 1)")  # El color 'rgba(132, 32, 41, 1)' corresponde a '#842029'

        # Hacer el assert del mensaje
        self.assertEqual(message_text, "An user with the phone number already exits.")
    
    #12 es manual

    #13
    def test_special_char_in_first_name_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("#Jairo", "Zeppeli", "GyroSpin2", "gyro2@gmail.com", "steelball1", "steelball1", "502")
                

        # Obtener el texto del mensaje
        message_text = register_page.get_message_text()
        # Obtener el color del mensaje
        message_color = register_page.get_message().value_of_css_property("color")

        # Asegurarse de que el color sea #842029
        self.assertEqual(message_color, "rgba(132, 32, 41, 1)")  # El color 'rgba(132, 32, 41, 1)' corresponde a '#842029'

        # Hacer el assert del mensaje
        self.assertEqual(message_text, "Sorry, First Name can't contain a special character.")
    #14
    def test_number_in_first_name_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo777", "Zeppeli", "GyroSpin2", "gyro2@gmail.com", "steelball1", "steelball1", "502")
                

        # Obtener el texto del mensaje
        message_text = register_page.get_message_text()
        # Obtener el color del mensaje
        message_color = register_page.get_message().value_of_css_property("color")

        # Asegurarse de que el color sea #842029
        self.assertEqual(message_color, "rgba(132, 32, 41, 1)")  # El color 'rgba(132, 32, 41, 1)' corresponde a '#842029'

        # Hacer el assert del mensaje
        self.assertEqual(message_text, "Sorry, First Name can't contain number")

    #15
    def test_invalid_char_in_last_name_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli%", "GyroSpin2", "gyro2@gmail.com", "steelball1", "steelball1", "502")
                

        # Obtener el texto del mensaje
        message_text = register_page.get_message_text()
        # Obtener el color del mensaje
        message_color = register_page.get_message().value_of_css_property("color")

        # Asegurarse de que el color sea #842029
        self.assertEqual(message_color, "rgba(132, 32, 41, 1)")  # El color 'rgba(132, 32, 41, 1)' corresponde a '#842029'

        # Hacer el assert del mensaje
        self.assertEqual(message_text, "Sorry, Last Name can't contain a special character.")

    #16
    def test_number_in_last_name_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli2", "GyroSpin2", "gyro2@gmail.com", "steelball1", "steelball1", "502")
                

        # Obtener el texto del mensaje
        message_text = register_page.get_message_text()
        # Obtener el color del mensaje
        message_color = register_page.get_message().value_of_css_property("color")

        # Asegurarse de que el color sea #842029
        self.assertEqual(message_color, "rgba(132, 32, 41, 1)")  # El color 'rgba(132, 32, 41, 1)' corresponde a '#842029'

        # Hacer el assert del mensaje
        self.assertEqual(message_text, "Sorry, Last Name can't contain number")

        

    #17
    def test_no_at_char_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "emailinvalido", "steelball1", "steelball1", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "Incluye un signo \"@\" en la dirección de correo electrónico. La dirección \"emailinvalido\" no incluye el signo \"@\".")

    #18
    def test_no_text_befor_at_char_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "@gmail.com", "steelball1", "steelball1", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "Ingresa texto antes del signo \"@\". La dirección \"@gmail.com\" está incompleta.")

    #19
    def test_no_text_after_at_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "gyro2@", "debil", "debil", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "Ingresa texto después del signo \"@\". La dirección \"gyro2@\" está incompleta.")

    #20
    def test_special_char_before_at_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "#@gmail.com", "steelball1", "s", "502")
                

        # Obtener el texto del mensaje
        message_text = register_page.get_message_text()
        # Obtener el color del mensaje
        message_color = register_page.get_message().value_of_css_property("color")

        # Asegurarse de que el color sea #842029
        self.assertEqual(message_color, "rgba(132, 32, 41, 1)")  # El color 'rgba(132, 32, 41, 1)' corresponde a '#842029'

        # Hacer el assert del mensaje
        self.assertEqual(message_text, "Sorry, Email can't contain a special character.")

    #21
    def test_special_char_after_at_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "gyro2@#.com", "debil", "debil", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "El texto después del signo \"@\" no debe incluir el símbolo \"#\".")


    #22
    def test_email_ends_dot_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "gyro2@gmail.", "debil", "debil", "502")
        
        # Usar JavaScript para obtener el mensaje de validación
        mensaje = driver.execute_script("return arguments[0].validationMessage;", register_page.get_email())
        #print(f"<{mensaje}>")
        assert(mensaje == "El signo \".\" está colocado en una posición incorrecta en \"gmail.\".")

    #23
    def test_mismatch_password_register(self):
        driver = self.driver
        #self.driver.get(HomePage.get_base_url())

        home_page = HomePage(driver)
        home_page.open_register()
        register_page = RegisterPage(driver)

        register_page.register_fill("Jairo", "Zeppeli", "GyroSpin2", "gyro2@gmail.com", "steelball1", "s", "502")
                

        # Obtener el texto del mensaje
        message_text = register_page.get_message_text()
        # Obtener el color del mensaje
        message_color = register_page.get_message().value_of_css_property("color")

        # Asegurarse de que el color sea #842029
        self.assertEqual(message_color, "rgba(132, 32, 41, 1)")  # El color 'rgba(132, 32, 41, 1)' corresponde a '#842029'

        # Hacer el assert del mensaje
        self.assertEqual(message_text, "Password and Confirm Password Does not match")

if __name__ == "__main__":
    unittest.main()
