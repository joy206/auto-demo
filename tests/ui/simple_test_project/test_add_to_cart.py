import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64

@pytest.fixture(scope="function")
def login(browser):
    browser.get("https://www.saucedemo.com")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

def test_add_to_cart(browser, login):
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    png = browser.get_screenshot_as_base64()
    with open("debug_add.png", "wb") as f:
        f.write(base64.b64decode(png))
    print(">>> current URL :", browser.current_url)

    badge = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1"

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    )

    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(browser, 10).until(EC.url_contains("cart"))

    items = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )
    assert len(items) == 1
