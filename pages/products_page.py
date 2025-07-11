from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  #  Импорт наверху

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart_by_id(self, item_id):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{item_id}"))
        ).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def sort_by_price_low_to_high(self):
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("lohi")  # сортировка: low to high

    def get_all_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(p.text.replace("$", "")) for p in price_elements]
