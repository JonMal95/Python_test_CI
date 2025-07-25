import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.xfail(reason="Checkout page unstable on CI. Known issue #123")
def test_checkout_process(browser):
    # 1. Авторизация
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login()

    # 2. Добавление товаров
    products_page = ProductsPage(browser)
    products_page.add_to_cart_by_id("sauce-labs-backpack")
    products_page.add_to_cart_by_id("sauce-labs-bolt-t-shirt")

    # 3. Переход в корзину
    products_page.go_to_cart()
    print("🧭 URL перед start_checkout:", browser.current_url)

    # 4. Начало оформления
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)
    checkout_page.start_checkout()

    # 5. Заполнение данных
    checkout_page.fill_checkout_info("Vanya", "Testovich", "123456")

    # 6. Завершение заказа
    checkout_page.finish_order()

    # 7. Проверка
    message = checkout_page.get_confirmation_message()
    print("📦 Сообщение подтверждения:", message)

    assert "Thank you for your order!" in message
