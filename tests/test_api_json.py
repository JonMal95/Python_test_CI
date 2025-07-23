import requests
import allure

@allure.title("Проверка JSON Placeholder: todo/1")
def test_json_placeholder():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    with allure.step("Отправляем GET-запрос"):
        response = requests.get(url)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяем поля ответа"):
        data = response.json()
        assert data["id"] == 1
        assert data["userId"] == 1
