import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from _pytest.fixtures import SubRequest


@pytest.fixture()
def driver():
    # options = webdriver.ChromeOptions()
    chrome_options = Options()
    page = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield page
    page.quit()


def pytest_addoption(parser):
    parser.addoption('--browser')


# @pytest.fixture()
# def something(request: SubRequest):
#     if request.config.getoption('--browser').upper() == 'FF':
#         driver = webdriver.Firefox()
#     elif request.config.getoption('--browser').lower() == 'chrome':
#         driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
