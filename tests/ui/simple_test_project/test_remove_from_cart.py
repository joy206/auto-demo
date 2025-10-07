import time
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def login(browser):
    browser.get("https://www.saucedemo.com")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()


def test_remove_from_cart(browser, login):
    """购物车页面移除商品"""
    # 加商品
    browser.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    time.sleep(2)
    # 进购物车
    browser.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(1)
    # 移除
    browser.find_element(By.XPATH, "//button[text()='Remove']").click()
    time.sleep(1)
    # 验证
    cart_items = browser.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, "购物车中的商品未成功移除"