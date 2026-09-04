"""
各页面共享的元素
"""
from selenium.webdriver.common.by import By


class CommonLocators:

    SHOPPING_CART = (By.ID, "shopping_cart_container")  # 顶部购物车图标
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")  # 购物车角标商品数量
