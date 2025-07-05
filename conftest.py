import pytest
from selenium import webdriver

LINK = 'https://store.steampowered.com/'


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.get(LINK)
    yield browser
    browser.quit()