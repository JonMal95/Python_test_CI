import os
import tempfile
import shutil
import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 🔒 Отключаем проверку SSL-сертификатов (для GitHub Actions)
os.environ["WDM_SSL_VERIFY"] = "0"

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

    # 📸 Скриншот при падении
    if request.node.rep_call.failed:
        screenshot_dir = os.path.join("screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        # 👇 Безопасное имя файла
        file_name = f"{request.node.nodeid.replace('::', '_').replace('/', '_')}.png"
        screenshot_path = os.path.join(screenshot_dir, file_name)

        try:
            driver.save_screenshot(screenshot_path)

            if os.path.exists(screenshot_path):
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name="Скриншот при падении",
                        attachment_type=allure.attachment_type.PNG
                    )

                print(f"\n📸 Скриншот сохранён: {screenshot_path}")
        except Exception as e:
            print(f"\n⚠️ Не удалось сохранить скриншот: {e}")

    driver.quit()
    shutil.rmtree(profile_dir, ignore_errors=True)

# 📌 Хук нужен, чтобы видеть результат теста (успех/ошибка)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
