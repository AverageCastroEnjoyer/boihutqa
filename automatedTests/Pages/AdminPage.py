from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

base_url = "http://127.0.0.1:8000/admin/"

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = "//*[@id=\"id_username\"]"
        self.password = "//*[@id=\"id_password\"]"
        self.login = "//*[@id=\"login-form\"]/div[3]/input"


        self.user_tools = "//*[@id=\"user-tools\"]"
        self.error_note = "//*[@id=\"content\"]/p"





        self.orders = "//*[@id=\"content-main\"]/div[6]/table/tbody/tr[4]/th/a"
        self.order = "//*[@id=\"result_list\"]/tbody/tr[1]/th/a"
        self.dropdown = "//*[@id=\"id_order_status\"]"
        self.save_order = "//*[@id=\"order_form\"]/div/div/input[1]"
        self.saved_order = "//*[@id=\"main\"]/div/ul"



        self.accounts = "//*[@id=\"content-main\"]/div[1]/table/tbody/tr[1]/th/a"
        self.account = "//*[@id=\"result_list\"]/tbody/tr[1]/th/a"
        self.checkbox = "//*[@id=\"id_is_admin\"]"
        self.save_account = "//*[@id=\"account_form\"]/div/div/input[1]"
        self.saved_account = "//*[@id=\"main\"]/div/ul"
        self.delete_account = "//*[@id=\"account_form\"]/div/div/p/a"
        self.confirm_delete_account = "//*[@id=\"content\"]/form/div/input[2]"
        self.account_deleted = "//*[@id=\"main\"]/div/ul/li"
        self.add_account = "//*[@id=\"content-main\"]/ul/li/a"
        self.new_password = "//*[@id=\"id_password\"]"
        self.first_name = "//*[@id=\"id_first_name\"]"
        self.last_name = "//*[@id=\"id_last_name\"]"
        self.username = "//*[@id=\"id_username\"]"
        self.phone = "//*[@id=\"id_phone\"]"
        self.new_email = "//*[@id=\"id_email\"]"
        self.is_admin = "//*[@id=\"id_is_admin\"]"
        self.logout = "//*[@id=\"user-tools\"]/a[3]"
        self.loggedout_text = "//*[@id=\"content\"]/h1"



        self.books = "//*[@id=\"content-main\"]/div[3]/table/tbody/tr[1]/th/a"
        self.book = "//*[@id=\"result_list\"]/tbody/tr[1]/th/a"
        self.stock_status = "//*[@id=\"id_stocks_available\"]"
        self.save_book = "//*[@id=\"book_form\"]/div/div/input[1]"
        self.saved_book = "//*[@id=\"main\"]/div/ul"
        self.history = "//*[@id=\"content-main\"]/ul/li/a"
        self.text = "//*[@id=\"content\"]/h1"
        self.add_book = "//*[@id=\"content-main\"]/ul/li/a"
        self.title = "//*[@id=\"id_title\"]"
        self.slug = "//*[@id=\"id_slug\"]"
        self.author = "//*[@id=\"id_author\"]"
        self.description = "//*[@id=\"id_description\"]"
        self.price = "//*[@id=\"id_price\"]"
        self.stocks = "//*[@id=\"id_stocks\"]"
        self.errors = "//*[@id=\"book_form\"]/div/p"
        self.required = "//*[@id=\"book_form\"]/div/fieldset/div[3]/ul/li"
        self.required2 = "//*[@id=\"book_form\"]/div/fieldset/div[7]/ul/li"
        self.delete_book = "//*[@id=\"book_form\"]/div/div/p/a"
        self.confirm_delete_book = "//*[@id=\"content\"]/form/div/input[2]"
        self.deleted_book = "//*[@id=\"main\"]/div/ul/li"




        self.categorys = "//*[@id=\"content-main\"]/div[5]/table/tbody/tr[1]/th/a"
        self.add_category = "//*[@id=\"content-main\"]/ul/li/a"
        self.name = "//*[@id=\"id_category_name\"]"
        self.category_slug = "//*[@id=\"id_slug\"]"
        self.category_des = "//*[@id=\"id_category_des\"]"
        self.save_category = "//*[@id=\"category_form\"]/div/div/input[1]"
        self.name_error = "//*[@id=\"category_form\"]/div/fieldset/div[1]/ul/li"
        self.category = "//*[@id=\"result_list\"]/tbody/tr[1]/th/a"
        self.delete_category = "//*[@id=\"category_form\"]/div/div/p/a"
        self.confirm_delete_category = "//*[@id=\"content\"]/form/div/input[2]"
        self.deleted_category = "//*[@id=\"main\"]/div/ul/li"
        self.saved_category = "//*[@id=\"main\"]/div/ul"





        self.invoices = "//*[@id=\"content-main\"]/div[6]/table/tbody/tr[1]/th/a"
        self.invoice = "//*[@id=\"result_list\"]/tbody/tr[1]/th/a"
        self.invoice_dropdown = "//*[@id=\"id_invoice_status\"]"
        self.save_invoice = "//*[@id=\"invoice_form\"]/div/div/input[1]"
        self.saved_invoice = "//*[@id=\"main\"]/div/ul"



    def get_email(self):
        return self.driver.find_element(By.XPATH, self.email)

    def get_user_tools(self):
        return self.driver.find_element(By.XPATH, self.user_tools)

    def get_error_note(self):
        return self.driver.find_element(By.XPATH, self.error_note)

    def get_password(self):
        return self.driver.find_element(By.XPATH, self.password)

    def get_login(self):
        return self.driver.find_element(By.XPATH, self.login)

    def get_orders(self):
        return self.driver.find_element(By.XPATH, self.orders)

    def get_order(self):
        return self.driver.find_element(By.XPATH, self.order)

    def get_dropdown(self):
        return self.driver.find_element(By.XPATH, self.dropdown)

    def get_save_order(self):
        return self.driver.find_element(By.XPATH, self.save_order)

    def get_saved_order(self):
        return self.driver.find_element(By.XPATH, self.saved_order)

    def get_accounts(self):
        return self.driver.find_element(By.XPATH, self.accounts)

    def get_account(self):
        return self.driver.find_element(By.XPATH, self.account)

    def get_save_account(self):
        return self.driver.find_element(By.XPATH, self.save_account)

    def get_saved_account(self):
        return self.driver.find_element(By.XPATH, self.saved_account)

    def get_delete_account(self):
        return self.driver.find_element(By.XPATH, self.delete_account)

    def get_confirm_delete_account(self):
        return self.driver.find_element(By.XPATH, self.confirm_delete_account)

    def get_account_deleted(self):
        return self.driver.find_element(By.XPATH, self.account_deleted)

    def get_add_account(self):
        return self.driver.find_element(By.XPATH, self.add_account)

    def get_new_password(self):
        return self.driver.find_element(By.XPATH, self.new_password)

    def get_first_name(self):
        return self.driver.find_element(By.XPATH, self.first_name)

    def get_last_name(self):
        return self.driver.find_element(By.XPATH, self.last_name)

    def get_username(self):
        return self.driver.find_element(By.XPATH, self.username)

    def get_phone(self):
        return self.driver.find_element(By.XPATH, self.phone)

    def get_new_email(self):
        return self.driver.find_element(By.XPATH, self.new_email)

    def get_is_admin(self):
        return self.driver.find_element(By.XPATH, self.is_admin)

    def get_logout(self):
        return self.driver.find_element(By.XPATH, self.logout)

    def get_loggedout_text(self):
        return self.driver.find_element(By.XPATH, self.loggedout_text)

    def get_books(self):
        return self.driver.find_element(By.XPATH, self.books)

    def get_book(self):
        return self.driver.find_element(By.XPATH, self.book)

    def get_stock_status(self):
        return self.driver.find_element(By.XPATH, self.stock_status)

    def get_save_book(self):
        return self.driver.find_element(By.XPATH, self.save_book)

    def get_saved_book(self):
        return self.driver.find_element(By.XPATH, self.saved_book)

    def get_history(self):
        return self.driver.find_element(By.XPATH, self.history)

    def get_text(self):
        return self.driver.find_element(By.XPATH, self.text)

    def get_add_book(self):
        return self.driver.find_element(By.XPATH, self.add_book)

    def get_title(self):
        return self.driver.find_element(By.XPATH, self.title)

    def get_slug(self):
        return self.driver.find_element(By.XPATH, self.slug)

    def get_author(self):
        return self.driver.find_element(By.XPATH, self.author)

    def get_description(self):
        return self.driver.find_element(By.XPATH, self.description)

    def get_price(self):
        return self.driver.find_element(By.XPATH, self.price)

    def get_stocks(self):
        return self.driver.find_element(By.XPATH, self.stocks)

    def get_add_errors(self):
        return self.driver.find_element(By.XPATH, self.errors)

    def get_required(self):
        return self.driver.find_element(By.XPATH, self.required)

    def get_required2(self):
        return self.driver.find_element(By.XPATH, self.required2)

    def get_delete_book(self):
        return self.driver.find_element(By.XPATH, self.delete_book)

    def get_confirm_delete_book(self):
        return self.driver.find_element(By.XPATH, self.confirm_delete_book)

    def get_deleted_book(self):
        return self.driver.find_element(By.XPATH, self.deleted_book)

    def get_categorys(self):
        return self.driver.find_element(By.XPATH, self.categorys)

    def get_category(self):
        return self.driver.find_element(By.XPATH, self.category)

    def get_name(self):
        return self.driver.find_element(By.XPATH, self.name)

    def get_category_slug(self):
        return self.driver.find_element(By.XPATH, self.category_slug)

    def get_category_des(self):
        return self.driver.find_element(By.XPATH, self.category_des)

    def get_save_category(self):
        return self.driver.find_element(By.XPATH, self.save_category)

    def get_name_error(self):
        return self.driver.find_element(By.XPATH, self.name_error)

    def get_delete_category(self):
        return self.driver.find_element(By.XPATH, self.delete_category)

    def get_confirm_delete_category(self):
        return self.driver.find_element(By.XPATH, self.confirm_delete_category)

    def get_deleted_category(self):
        return self.driver.find_element(By.XPATH, self.deleted_category)

    def get_saved_category(self):
        return self.driver.find_element(By.XPATH, self.saved_category)


    def get_invoices(self):
        return self.driver.find_element(By.XPATH, self.invoices)

    def get_invoice(self):
        return self.driver.find_element(By.XPATH, self.invoice)

    def get_invoice_dropdown(self):
        return self.driver.find_element(By.XPATH, self.invoice_dropdown)

    def get_save_invoice(self):
        return self.driver.find_element(By.XPATH, self.save_invoice)

    def get_saved_invoice(self):
        return self.driver.find_element(By.XPATH, self.saved_invoice)




    def fill_login(self, email, password):
        self.get_email().send_keys(email)
        self.get_password().send_keys(password)
        self.get_login().click()
        time.sleep(2)

    def login_successful(self):
        return self.get_user_tools().is_displayed()

    def login_unsuccesful(self):
        return self.get_error_note().is_displayed()

    def change_order_status(self):
        self.get_orders().click()
        self.get_order().click()

        select = Select(self.get_dropdown())


        select.select_by_value("COMPLETED")
        self.get_save_order()

        self.get_dropdown().click()
        self.get_save_order().click()
        time.sleep(1)

    def check_order_saved(self):
        return self.get_saved_order().is_displayed


    def change_user(self):
        self.get_accounts().click()
        self.get_account().click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.get_is_admin().click()
        self.get_save_account().click()
        time.sleep(1)

    def check_account_saved(self):
        return self.get_saved_account().is_displayed

    def mark_book_unavailable(self):
        self.get_books().click()
        self.get_book().click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.get_stock_status().click()
        self.get_save_book().click()
        time.sleep(1)

    def check_book_saved(self):
        return self.get_saved_book().is_displayed

    def check_history(self):
        self.get_books().click()
        self.get_book().click()
        self.get_history().click()
        time.sleep(1)

    def check_history_opened(self):
        return self.get_text().is_displayed()

    def change_invoice(self):
        self.get_invoices().click()
        self.get_invoice().click()

        select = Select(self.get_invoice_dropdown())

        select.select_by_value("REJECTED")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.get_save_invoice().click()
        time.sleep(1.5)

    def check_invoice_saved(self):
        return self.get_saved_invoice().is_displayed()

    def add_book_info(self, title, slug, author, description, price, stocks):
        self.get_books().click()
        self.get_add_book().click()
        self.get_title().send_keys(title)
        self.get_slug().send_keys(slug)
        self.get_author().send_keys(author)
        self.get_description().send_keys(description)
        self.get_price().send_keys(price)
        self.get_stocks().send_keys(stocks)
        self.get_save_book().click()
        time.sleep(1.5)

    def check_book_no_category_image(self):
        return self.get_required().is_displayed()

    def check_book_invalid_values(self):
        return self.get_required2().is_displayed()


    def delete_category_task(self):
        self.get_categorys().click()
        self.get_category().click()
        self.get_delete_category().click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.get_confirm_delete_category().click()
        time.sleep(1.5)

    def check_deleted_category(self):
        actual_message = self.get_deleted_category().text
        return "was deleted successfully." in actual_message

    def delete_book_task(self):
        self.get_books().click()
        self.get_book().click()
        self.get_delete_book().click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.get_confirm_delete_book().click()
        time.sleep(1.5)

    def check_deleted_book(self):
        actual_message = self.get_deleted_book().text
        return "was deleted successfully." in actual_message

    def delete_account_task(self):
        self.get_accounts().click()
        self.get_account().click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.get_delete_account().click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.get_confirm_delete_account().click()
        time.sleep(1.5)

    def check_deleted_account(self):
        actual_message = self.get_account_deleted().text
        return "was deleted successfully." in actual_message

    def change_category_task(self):
        self.get_categorys().click()
        self.get_category().click()
        self.get_category_des().send_keys("speculative fiction")
        self.get_save_category().click()
        time.sleep(1.5)

    def check_changed_category(self):
        actual_message = self.get_saved_category().text
        return "was changed successfully." in actual_message

    def add_account_task(self, password, first_name, last_name, username, phone, email):
        self.get_accounts().click()
        self.get_add_account().click()
        self.get_new_password().send_keys(password)
        self.get_first_name().send_keys(first_name)
        self.get_last_name().send_keys(last_name)
        self.get_username().send_keys(username)
        self.get_phone().send_keys(phone)
        self.get_new_email().send_keys(email)
        self.get_is_admin().click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.get_save_account().click()
        time.sleep(1.5)

    def check_new_account(self):
        actual_message = self.get_saved_account().text
        return "was added successfully." in actual_message

    def logout_task(self):
        self.get_logout().click()
        time.sleep(1.5)

    def check_logout(self):
        actual_message = self.get_loggedout_text().text
        return "Logged out" in actual_message



        #return self.get_deleted_category().is_displayed()




    @staticmethod
    def get_base_url():
        return base_url


