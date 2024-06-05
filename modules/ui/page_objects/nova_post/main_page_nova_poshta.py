from selenium.common import TimeoutException, NoSuchElementException, \
    ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage


class MainPageNP(BasePage):

    URL = "https://air.nova.global/"
    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(MainPageNP.URL)

    def try_to_choose_usa(self):
        usa_link = self.driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[3]/div/div/div/a[1]')
        self.close_banner()
        self.driver.maximize_window()
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   usa_link)

        usa_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/a[1]'))
        )
        try:
            usa_link.click()
        except ElementClickInterceptedException:
            self.close_banner()
            usa_link.click()

    def close_banner(self):
        try:
            banner_to_close = self.driver.find_element(By.XPATH,
                        '//*[@id="registration-banner-close"]')
            banner_to_close.click()
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException):
            pass

    def get_country_title(self):
        try:
            css_selector = "h1.promo-h1 span.promo-h1__country > span"
            country_title_elem = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            country_title = country_title_elem.text
            return country_title
        except TimeoutException:
            print("*******COUNTRY WASNT FOUNDED*******")
            return None






