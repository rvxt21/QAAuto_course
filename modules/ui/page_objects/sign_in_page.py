from selenium.webdriver.common.by import By

from modules.ui.page_objects.base_page import BasePage


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_to_login(self, username: str, password: str):
        login_elem = self.driver.find_element(By.ID, 'login_field')
        login_elem.send_keys(username)

        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)

        btn_element = self.driver.find_element(By.NAME, "commit")

        btn_element.click()

    def check_title(self, excpected_title):
        return self.driver.title == excpected_title