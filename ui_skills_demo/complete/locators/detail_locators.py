"""
商品详情页页面元素封装
"""
from selenium.webdriver.common.by import By


class DetailLocators:

    DETAIL_PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_details_name.large_size")
    DETAIL_PRODUCT_PRICE = (By.CLASS_NAME, "inventory_details_price")

    DETAIL_ADD_TO_CART = (By.ID, "add-to-cart")
    DETAIL_REMOVE_FROM_CART = (By.ID, "remove")

    BACK_TO_PRODUCTS = (By.ID, "back-to-products")

