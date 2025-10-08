import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def login(browser):
    browser.get("https://www.saucedemo.com")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

def test_add_to_cart(browser, login):
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1"

    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    items = browser.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items) == 1
