from selenium.common import TimeoutException, NoSuchElementException, \
    ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage
COUNTRY_BASE_XPATH = "/html/body/div[1]/div/div[3]/div/div/div/a[{}]"
COUNTRIES_XPATH_MAIN_PAGE_CODES = {
    "usa": 1,
    "china": 2,
    "great_britain": 3,
    "germany": 4,
    "italy": 5,
    "poland": 6,
    "france": 7,
    "spain": 8,
    "turkey": 9,
    "czech": 10,
    "canada": 11,
    "hungary": 12,
    "slovenia": 13,
    "romania": 14,
    "latvia": 15,
    "estonia": 16,
    "litva": 17
}


class MainPageNP(BasePage):

    URL = "https://air.nova.global/"
    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(MainPageNP.URL)

    def try_to_choose_country(self, country: str):
        usa_link = self.driver.find_element(By.XPATH,
            COUNTRY_BASE_XPATH.format(COUNTRIES_XPATH_MAIN_PAGE_CODES[country]))
        self.close_banner()
        self.driver.maximize_window()
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   usa_link)

        usa_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
            COUNTRY_BASE_XPATH.format(COUNTRIES_XPATH_MAIN_PAGE_CODES[country]))))

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






