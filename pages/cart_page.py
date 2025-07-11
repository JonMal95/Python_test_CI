from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver


    def get_cart_items_titles(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [e.text for e in elements]
