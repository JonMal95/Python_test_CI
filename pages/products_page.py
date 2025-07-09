from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart_by_id(self, item_id):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{item_id}"))
        ).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
