from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

AMAZON_LINK = (By.ID,"twotabsearchtextbox")
               #"//input[@id='twotabsearchtextbox']")
EXPECTED = '"gifts for mom"'
ACTUAL_AMAZON_TEXT = (By.XPATH, "//*[@id='nav-logo']")
AMAZON_SEARCH_FIELD = (By.XPATH)
SUBMIT = (By.XPATH, "//input[@type='submit']")
SEARCH_TEXT = (By.CSS_SELECTOR, "span.a-color-state")
GIFT_ITEMS = (By.XPATH, "//div[@class='a-section aok-relative s-image-square-aspect']")
BASE_URL = 'https://www.amazon.com/'
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(4)

driver.get(BASE_URL)
FILD = WebDriverWait(driver,4).until(EC.element_to_be_clickable(AMAZON_LINK))
FILD.send_keys("gifts for mom")
driver.find_element(*SUBMIT).click()

search_text = driver.find_element(*SEARCH_TEXT).text

assert EXPECTED in search_text,f"EXPECTED{EXPECTED},but got {search_text}"
GIFTS = driver.find_elements(*GIFT_ITEMS)[1]
GIFTS.click()
assert BASE_URL in driver.current_url

driver.quit()
