import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def login(browser):
    browser.get("https://www.saucedemo.com")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()


def test_remove_from_cart(browser, login):
    """购物车页面移除商品"""
    # 添加商品
    add_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']"))
    )
    add_btn.click()

    # 等待角标出现
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    # 进入购物车页面
    cart_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
    )
    cart_link.click()

    # 等待 Remove 按钮可点击
    remove_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    )
    remove_btn.click()

    # 等待购物车商品列表为空
    WebDriverWait(browser, 10).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    # 验证
    cart_items = browser.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, "购物车中的商品未成功移除"