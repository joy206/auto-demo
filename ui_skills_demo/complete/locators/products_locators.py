"""
商品页页面元素封装
"""
from selenium.webdriver.common.by import By


class ProductsLocators:

    TITLE = (By.CLASS_NAME, "title")

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_IMAGE = (By.CLASS_NAME, "inventory_item_img")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-{product_name}")
    REMOVE_FROM_CART_BTN = (By.ID, "remove-{product_name}")

    PRODUCTS_SELECT = (By.CLASS_NAME, "product_sort_container")
    NAME_ASC = "Name (A to Z)"
    NAME_DESC = "Name (Z to A)"
    PRICE_ASC = "Price (low to high)"
    PRICE_DESC = "Price (high to low)"

    APPOINTED_PRODUCT_NAME = (By.XPATH, "//div[normalize-space(text()) = '{product_name}']")
    APPOINTED_PRODUCT_PRICE = (By.XPATH, "//div[normalize-space(text())='{product_name}']/ancestor::div["
                                         "@class='inventory_item']//div[@class='inventory_item_price']")
    APPOINTED_PRODUCT_IMAGE = (By.XPATH, "//div[normalize-space(text()) = '{product_name}']/ancestor::div["
                                         "@class='inventory_item']//img")




