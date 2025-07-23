from selenium.webdriver.common.by import By
import allure

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получение названий товаров в корзине")
    def get_cart_items_titles(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        titles = [e.text for e in elements]
        allure.attach(str(titles), name="Товары в корзине", attachment_type=allure.attachment_type.TEXT)
        return titles
