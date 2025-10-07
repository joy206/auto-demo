import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def login(browser):
    browser.get("https://www.saucedemo.com")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))


def test_sort_by_name_ascending(browser, login):
    """按商品名首字母升序排列"""
    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Name (A to Z)")
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "product_sort_container"), "Name (A to Z)"
        )
    )
    products = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [p.text for p in products]
    assert product_names == sorted(product_names), "产品未按升序排列"


def test_sort_by_name_descending(browser, login):
    """按商品名首字母降序排列"""
    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Name (Z to A)")
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "product_sort_container"), "Name (Z to A)"
        )
    )
    products = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [p.text for p in products]
    assert product_names == sorted(product_names, reverse=True), "产品未按降序排列"


def test_sort_by_price_low_to_high(browser, login):
    """按价格从低到高排列"""
    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (low to high)")
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "product_sort_container"), "Price (low to high)"
        )
    )
    prices = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    product_prices = [float(p.text.replace("$", "")) for p in prices]
    assert product_prices == sorted(product_prices), "价格未按从低到高排列"


def test_sort_by_price_high_to_low(browser, login):
    """按价格从高到低排列"""
    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (high to low)")
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "product_sort_container"), "Price (high to low)"
        )
    )
    prices = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    product_prices = [float(p.text.replace("$", "")) for p in prices]
    assert product_prices == sorted(product_prices, reverse=True), "价格未按从高到低排序"