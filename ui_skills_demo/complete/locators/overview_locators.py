"""
结算总览页面元素封装
"""
from selenium.webdriver.common.by import By


class OverviewLocators:

    OVERVIEW_PAGE_TITLE = (By.CLASS_NAME, "title")
    OVERVIEW_PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    OVERVIEW_PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    PAYMENT_INFORMATION = (By.XPATH, "//div[normalize() = 'Payment Information:']/following-sibling::div[1]")
    SHIPPINT_INFORMATION = (By.XPATH, "//div[normalize() = 'Shipping Information:']/following-sibling::div[1]")
    ITEM_TOTAL_PRICE = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_PRICE = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")
    BTN_CANCEL = (By.ID, "cancel")
    BTN_FINISH = (By.ID, "finish")