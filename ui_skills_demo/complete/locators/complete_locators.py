"""
结算完成页页面元素封装
"""
from selenium.webdriver.common.by import By


class CompleteLocators:
    COMPLETE_PAGE_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    BACK_HOME = (By.ID, "back-to-products")
