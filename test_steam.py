from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium, pytest

LINK = 'https://store.steampowered.com/'


@pytest.mark.usefixtures('browser')
class TestSteamPage:
    TIMEOUT = 5

    LOGIN_BUTTON = (By.XPATH, "//a[text()='войти']")
    LOGIN_TEXT = (By.XPATH, "//div[text()='Вход']")
    LOGIN_USERNAME_INPUT = (By.XPATH,
                            "//div[contains(text(), 'Войдите')]//following-sibling::input[@type='text']")
    LOGIN_PASSWORD_INPUT = (By.XPATH,
                            "//div[contains(text(), 'Пароль')]//following-sibling::input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    #LOGIN_ERROR_MESSAGE_DIV = (By.XPATH, "//div[contains(text(), 'проверьте')]")
    LOGIN_ERROR_MESSAGE_DIV = (By.XPATH, "//div[@*='auth_message_incorrectcode']")
    STORE_NAV_DIV = (By.XPATH, "//div[@class='store_nav']")

    def test_load_page(self, browser):
        browser.get(LINK)
        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.STORE_NAV_DIV))

    def test_click_login(self, browser):
        WebDriverWait(browser, self.TIMEOUT).until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def test_load_login_page(self, browser):
        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.LOGIN_TEXT))

    def test_login(self, browser):
        WebDriverWait(browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.LOGIN_USERNAME_INPUT)).send_keys('TEST_LOGIN')
        WebDriverWait(browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.LOGIN_PASSWORD_INPUT)).send_keys('TEST_PASSWORD')
        WebDriverWait(browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(self.LOGIN_SUBMIT_BUTTON)).submit()
        WebDriverWait(browser, self.TIMEOUT).until(
            EC.presence_of_element_located(self.LOGIN_ERROR_MESSAGE_DIV))

