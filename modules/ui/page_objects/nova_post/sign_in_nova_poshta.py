import time

from selenium.webdriver.common.by import By

from modules.ui.page_objects.base_page import BasePage


class SignInPageNP(BasePage):

    URL = "https://air.nova.global/login"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPageNP.URL)

    def try_to_login(self, email: str, password: str):
        email_elem = self.driver.find_element(By.ID, "email")
        email_elem.send_keys(email)

        password_elem = self.driver.find_element(By.ID, "password")
        password_elem.send_keys(password)

        btn_login = self.driver.find_element(By.TAG_NAME,
                                             "button")

        btn_login.click()
        time.sleep(3)

    def check_title(self, excpected_message):
        message = self.driver.find_element(By.CLASS_NAME, "text-error")

        return message.text == excpected_message
