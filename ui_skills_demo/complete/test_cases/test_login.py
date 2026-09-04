"""
登录页测试用例
"""
import allure
import pytest

from ui_skills_demo.complete.pages.login_page import LoginPage
from ui_skills_demo.complete.pages.product_page import ProductPage


@allure.feature("登录模块")
class TestLogin:

    @allure.story("用户登录")
    @allure.title("验证正确密码登录成功")
    def test_login_success(self, driver, login_page):
        """正常场景：输入正确的用户名和密码，成功登录"""
        with allure.step("输入正确的用户名、密码"):
            login_page.do_login("standard_user", "secret_sauce")
        with allure.step("验证登录成功，进入商品列表页"):
            product_page = ProductPage(driver)
            assert '/inventory.html' in driver.current_url, f"测试失败，url不匹配{driver.current_url}"
            products = product_page.get_products_list()
            assert len(products) > 0, "商品列表为空"

    @allure.story("用户登录")
    @allure.title("验证错误的用户名、错误的密码登录失败")
    def test_login_failure(self, driver, login_page):
        """异常场景：输入错误的用户名、密码，登录失败"""
        with allure.step("输入错误的用户名、密码"):
            login_page.do_login("111", "222")
        with allure.step("获取错误提示信息"):
            error_text = login_page.get_error_text()
        with allure.step("验证提示信息包含'do not match'"):
            assert 'do not match' in error_text, f"测试失败，期望'do not match'，实际{error_text}"
