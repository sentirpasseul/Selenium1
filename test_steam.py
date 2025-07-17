from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium, pytest
from faker import Faker


class TestSteamPage:
    TIMEOUT = 5

    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class, 'global_action_link')]")
    LOGIN_TEXT = (By.XPATH, "//div[contains(@class,'page_content')]//form")
    LOGIN_USERNAME_INPUT = (By.XPATH,
                            "//div[contains(@class,'page_content')]//input[@type='text']")
    LOGIN_PASSWORD_INPUT = (By.XPATH,
                            "//div[contains(@class,'page_content')]//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_ERROR_MESSAGE_DIV = (
    By.XPATH, "//button[@type='submit']/../following-sibling::div[string-length(normalize-space(text())) > 1]")
    STORE_NAV_DIV = (By.XPATH, "//div[contains(@class,'store_nav')]")

    def test_login(self, browser):
        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.STORE_NAV_DIV))

        WebDriverWait(browser, self.TIMEOUT).until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.LOGIN_TEXT))

        WebDriverWait(browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.LOGIN_USERNAME_INPUT)).send_keys(Faker().user_name())
        WebDriverWait(browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.LOGIN_PASSWORD_INPUT)).send_keys(Faker().password())
        WebDriverWait(browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(self.LOGIN_SUBMIT_BUTTON)).submit()

        element_error = WebDriverWait(browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.LOGIN_ERROR_MESSAGE_DIV))
        assert element_error.text == "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
