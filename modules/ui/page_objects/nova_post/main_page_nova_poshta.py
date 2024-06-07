import time

from selenium.common import TimeoutException, NoSuchElementException, \
    ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from modules.ui.page_objects.base_page import BasePage


class MainPageNP(BasePage):

    URL = "https://novaposhta.ua/"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(MainPageNP.URL)

    def try_to_find_parcel(self, parcel_delivery_note):
        input_form = self.driver.find_element(By.CSS_SELECTOR, '#cargo_number')
        self.close_banner()
        input_form.clear()

        input_form.send_keys(parcel_delivery_note)

        input_form.send_keys(Keys.RETURN)

    def close_banner(self):
        try:
            banner_to_close = self.driver.find_element(By.CSS_SELECTOR,
                        '#popup_info > div.header > i')
            banner_to_close.click()
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException):
            pass

    def get_error_message_found_parcel(self):
        # css_selector_error = "#np-number-input-desktop-message-error-message > span"
        css_selector_error = "#root > div.container.smooth-scroll.visible > section > div > div > div.tracking__error > div"
        print("************ERROR************")
        error_message = self.driver.find_element(By.CSS_SELECTOR, css_selector_error)
        print(error_message.text)
        return error_message.text
