import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password,error_message", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
])
def test_login_negative(browser, username, password, error_message):
    # Открываем страницу логина
    login_page = LoginPage(browser)
    login_page.open()

    # Выполняем логин с заданными параметрами
    login_page.login(username, password)

    # Получаем текст ошибки и сравниваем с ожидаемым
    actual_message = login_page.get_error_message()
    assert error_message in actual_message
