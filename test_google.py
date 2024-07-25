import time

from selenium.webdriver.common.by import By


def test_google(driver):
    driver.get('https://www.google.com/')
    time.sleep(3)
    search_field = driver.find_element(By.NAME, 'q')
    search_field.send_keys('smart tv')
    time.sleep(3)
    search_field.submit()
