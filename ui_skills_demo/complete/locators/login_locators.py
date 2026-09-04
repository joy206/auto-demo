"""
登录页页面元素封装
"""
from selenium.webdriver.common.by import By


class LoginLocators:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_TEXT = (By.CSS_SELECTOR, "h3[data-test='error']")