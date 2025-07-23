from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
    def start_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
    def fill_checkount(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first_name").send_keys(first_name)
        self.driver.find_element(By.ID,"last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def finish_order(self):
            self.driver.find_element(By.ID, "finish").click()
    def get_confirmation_message(self):
        return self.driver.find_element(By.CLASS_NAME,"complete-header").text  # извлекает текст из HTML-элемента, чтобы мы могли сравнивать, проверять и утверждат