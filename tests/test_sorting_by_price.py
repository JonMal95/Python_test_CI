from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_sort_by_price_low_to_high(browser):
    # 1. Заходим на сайт
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login()

    # 2. Переходим на страницу товаров и сортируем
    products_page = ProductsPage(browser)
    products_page.sort_by_price_low_to_high()

    # 3. Получаем все цены
    prices = products_page.get_all_prices()
    sorted_prices = sorted(prices)

    # 4. Проверяем, что цены отсортированы
    assert prices == sorted_prices, f"❌ Цены не отсортированы: {prices}"
