import requests

def test_saucedemo_status():
    url = "https://www.saucedemo.com/"
    response = requests.get(url)   # GET-запрос

    # Проверяем статус-код
    assert response.status_code == 200
