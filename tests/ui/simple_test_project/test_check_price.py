import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def login(browser):
    browser.get("https://www.saucedemo.com")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    WebDriverWait(browser, 5).until(EC.url_contains("inventory.html"))


def test_checkout_flow(browser, login):
    """完整结算流程"""
    # 添加商品
    browser.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    WebDriverWait(browser, 3).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "shopping_cart_badge"),"1"
    ))

    # 进入购物车页面
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(browser, 3).until(EC.url_contains("cart.html"))

    # 结算
    browser.find_element(By.ID, "checkout").click()
    WebDriverWait(browser, 3).until(EC.url_contains("checkout-step-one.html"))

    # 填写个人信息
    browser.find_element(By.ID, "first-name").send_keys("dirst")
    browser.find_element(By.ID, "last-name").send_keys("lat")
    browser.find_element(By.ID, "postal-code").send_keys("07225")
    browser.find_element(By.ID, "continue").click()
    WebDriverWait(browser, 5).until(EC.url_contains("checkout-step-two.html"))

    # 订单确认
    browser.find_element(By.ID, "finish").click()
    header = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text
    assert header == "Thank you for your order!"