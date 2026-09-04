"""
个人信息页页面元素
"""
from selenium.webdriver.common.by import By


class CheckInfoLocators:

    INFO_PAGE_TITLE = (By.CLASS_NAME, "title")
    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_POST_CODE = (By.ID, "postal-code")
    ERROR_TEXT = (By.CSS_SELECTOR, "h3[data-test='error']")

    BTN_CANCEL = (By.ID, "cancel")
    BTN_CONTINUE = (By.ID, "continue")