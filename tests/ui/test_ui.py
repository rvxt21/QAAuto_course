import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome()

    driver.get("https://github.com/login")

    login_elem = driver.find_element(By.ID, 'login_field')
    login_elem.send_keys('anastasia1koryagina@gmail.com')

    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("wrong_PASSWORD")

    btn_element = driver.find_element(By.NAME, "commit")
    btn_element.click()

    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(15)
    driver.close()
