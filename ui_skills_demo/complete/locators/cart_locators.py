"""
购物车页面元素封装
"""
from selenium.webdriver.common.by import By


class CartLocators:

    CART_TITLE = (By.CLASS_NAME, "title")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CART_REMOVE = (By.ID, "remove-{product_name}")
    BTN_CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    BTN_CHECKOUT = (By.ID, "checkout")