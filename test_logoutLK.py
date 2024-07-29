from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

browser = webdriver.Chrome()


def test_logout():
    browser.get('https://www.saucedemo.com/')

    url_before_test = browser.current_url
    # print(url_before_test)

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    burger_menu = browser.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(2)

    logout = browser.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout.click()
    # time.sleep(3)

    url_after_test = browser.current_url
    # print(url_after_test)

    assert url_before_test == url_after_test

    browser.quit()
