import pytest

def test_intentional_fail(browser):
    browser.get("https://www.saucedemo.com/")
    assert "Nonexistent text" in browser.page_source  # ❌ специально ложное утверждение
