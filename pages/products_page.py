from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import allure

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавление в корзину по ID: {item_id}")
    def add_to_cart_by_id(self, item_id):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{item_id}"))
        ).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    @allure.step("Сортировка товаров по цене: Low → High")
    def sort_by_price_low_to_high(self):
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("lohi")

    @allure.step("Получение всех цен на странице товаров")
    def get_all_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(p.text.replace("$", "")) for p in price_elements]
        allure.attach(str(prices), name="Цены на странице", attachment_type=allure.attachment_type.TEXT)
        return prices
