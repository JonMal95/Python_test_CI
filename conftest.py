import os
import tempfile
import shutil
import pytest
import allure
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

os.environ["WDM_SSL_VERIFY"] = "0"

@pytest.fixture
def browser(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    profile_dir = tempfile.mkdtemp(prefix="selenium-profile-")
    options.add_argument(f"--user-data-dir={profile_dir}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        screenshot_dir = os.path.join("screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

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

                    # 📤 Отправка в Telegram
                    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
                    chat_id = os.getenv("TELEGRAM_CHAT_ID")

                    if bot_token and chat_id:
                        print("📲 Отправка скрина в Telegram...")
                        requests.post(
                            f"https://api.telegram.org/bot{bot_token}/sendDocument",
                            files={"document": open(screenshot_path, "rb")},
                            data={"chat_id": chat_id, "caption": f"❌ Тест упал: {request.node.nodeid}"}
                        )
        except Exception as e:
            print(f"\n⚠️ Не удалось сохранить/отправить скриншот: {e}")

    driver.quit()
    shutil.rmtree(profile_dir, ignore_errors=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
