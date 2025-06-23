
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium, pytest

LINK = 'https://store.steampowered.com/'
TEST_LOGIN = 'test'
TEST_PASSWORD = 'test'


@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


class TestSteamPage:
    @pytest.mark.smoke
    def test_load_page(self, browser):
        browser.get(LINK)
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Популярное')]"))
        )

    @pytest.mark.smoke
    def test_click_login(self, browser):
        browser.find_element(By.XPATH, "//a[text()='войти']").click()

    @pytest.mark.smoke
    def test_load_login_page(self, browser):
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Вход']")))
        browser.find_element(By.XPATH, "//div[text()='Вход']").is_displayed()

    @pytest.mark.smoke
    def test_login(self, browser):
        input_login = browser.find_element(By.XPATH,
                                           "//div[contains(text(), 'Войдите')]//following-sibling::input[@type='text']")
        input_login.is_displayed()
        input_login.send_keys(TEST_LOGIN)

        input_password = browser.find_element(By.XPATH,
                                              "//div[contains(text(), 'Пароль')]//following-sibling::input[@type='password']")
        input_password.is_displayed()
        input_password.send_keys(TEST_PASSWORD)

        button_login = browser.find_element(By.XPATH, "//button[@type='submit']")
        button_login.is_enabled()
        button_login.submit()

        text_error_login = browser.find_element(By.XPATH, "//div[contains(text(), 'проверьте')]")
        text_error_login.is_displayed()
