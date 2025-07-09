from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_two_products_to_cart(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login()

    products_page = ProductsPage(browser)
    products_page.add_to_cart_by_id("sauce-labs-backpack")
    products_page.add_to_cart_by_id("sauce-labs-bolt-t-shirt")
    products_page.go_to_cart()

    cart_page = CartPage(browser)
    titles = cart_page.get_cart_items_titles()

    assert "Sauce Labs Backpack" in titles
    assert "Sauce Labs Bolt T-Shirt" in titles
