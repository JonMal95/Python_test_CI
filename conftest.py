import pytest
import os
import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # 🔑 Уникальный профиль для каждой сессии
    profile_dir = tempfile.mkdtemp(prefix="selenium-profile-")
    options.add_argument(f"--user-data-dir={profile_dir}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    yield driver

    # Сделать скриншот при падении теста
    if request.node.rep_call.failed:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        file_name = f"{request.node.nodeid.replace('::', '_')}.png"
        screenshot_path = os.path.join(screenshot_dir, file_name)
        driver.save_screenshot(screenshot_path)
        print(f"\n📸 Скриншот сохранён: {screenshot_path}")

    driver.quit()

    # 🧹 Удаляем временный профиль
    shutil.rmtree(profile_dir, ignore_errors=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Для определения упал ли тест
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
