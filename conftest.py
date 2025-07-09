import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver

    # Сделать скриншот при падении теста
    if request.node.rep_call.failed:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        file_name = f"{request.node.nodeid.replace('::', '_')}.png"
        screenshot_path = os.path.join(screenshot_dir, file_name)
        driver.save_screenshot(screenshot_path)
        print(f"\n Скриншот сохранён: {screenshot_path}")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Для определения упал ли тест
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
