import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture(scope="module")
def login(browser):
    browser.get("https://www.saucedemo.com")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()


def test_product_sorting(browser, login):
    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Name (A to Z)")

    products = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [p.text for p in products]
    assert product_names == sorted(product_names)