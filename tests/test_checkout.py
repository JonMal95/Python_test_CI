from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_process(browser):
    # 1. Авторизация
    login_page = LoginPage(browser)              # создаём объект логин-страницы
    login_page.open()                            # открываем сайт
    login_page.login()                           # логинимся как стандартный пользователь

    # 2. Добавление товаров
    products_page = ProductsPage(browser)        # создаём объект страницы товаров
    products_page.add_to_cart_by_id("sauce-labs-backpack")
    products_page.add_to_cart_by_id("sauce-labs-bolt-t-shirt")
    products_page.go_to_cart()                   # переходим в корзину

    # 3. Переход к оформлению
    cart_page = CartPage(browser)                # создаём объект корзины
    checkout_page = CheckoutPage(browser)        # создаём объект страницы оформления
    checkout_page.start_checkout()               # нажимаем кнопку Checkout

    # 4. Заполнение формы
    checkout_page.fill_checkout_info("Vanya", "Testovich", "123456")

    # 5. Завершение оформления
    checkout_page.finish_order()

    # 6. Проверка
    message = checkout_page.get_confirmation_message()
    assert "Thank you for your order!" in message

