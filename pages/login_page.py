from selenium.webdriver.common.by import By
import allure

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы логина")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Логин пользователя: {username}")
    def login(self, username="standard_user", password="secret_sauce"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Получение текста ошибки на странице логина")
    def get_error_message(self):
        message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        allure.attach(message, name="Ошибка логина", attachment_type=allure.attachment_type.TEXT)
        return message
