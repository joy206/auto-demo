"""
买家信息页，测试用例
"""
import allure
import pytest

from ui_skills_demo.complete.pages.checkinfo_page import CheckInfoPage
from ui_skills_demo.complete.pages.overview_page import OverviewPage
from ui_skills_demo.complete.utils.log_util import swag_logger


@allure.feature("买家信息页")
class TestCheckInfo:

    @allure.story("页面跳转")
    @allure.title("买家信息页返回购物车页面")
    def test_back_to_cart(self, driver,products_page):
        """取消购买，返回到购物车页面"""
        with allure.step("由购物车页面，点击进入买家信息页"):
            product_name = "Sauce Labs Backpack"
            products_page.add_to_cart(product_name)
            cart_page = products_page.click_shopping_cart()
            cart_page.click_to_checkout()
            checkInfo_page = CheckInfoPage(driver)

        with allure.step("买家信息页，点击返回，验证回到购物车页面"):
            checkInfo_page.click_cancel()
            title = cart_page.get_cart_page_title()
            amount = cart_page.get_cart_list_amount()
            assert '/cart.html' in driver.current_url, f"url不匹配，期望'/cart.html'，实际{driver.current_url}"
            assert title == "Your Cart", f"标题不符，期望'Your Cart'，实际{title}"
            assert amount == 1, f"数量不符，期望1，实际商品数量{amount}"

    @allure.story("页面跳转")
    @allure.title("正常进入最终结算页")
    def test_click_to_overview(self, driver, products_page):
        """正常情况：输入买家信息后，点击continue。测试结算第一步，跳转到结算第二步。"""
        with allure.step("前置操作：添加商品并进入结算流程"):
            product_name = "Sauce Labs Bike Light"
            product_price = products_page.get_product_price_by_name(product_name)
            products_page.add_to_cart(product_name)
            cart_page = products_page.click_shopping_cart()
            cart_page.click_to_checkout()

        checkinfo_page = CheckInfoPage(driver)

        with allure.step("输入姓名、邮编"):
            checkinfo_page.input_first_name('Jim')
            checkinfo_page.input_last_name('Green')
            checkinfo_page.input_post_code('03356')

        with allure.step("点击进入最终结算页"):
            checkinfo_page.click_continue()

        overview_page = OverviewPage(driver)

        with allure.step("验证价格计算正确"):
            subtotal = overview_page.get_subtotal()
            tax = overview_page.get_tax()
            total = overview_page.get_total()

            expected_subtotal = product_price
            expected_tax = round(expected_subtotal * 0.08, 2)
            expected_total = round(expected_subtotal + expected_tax, 2)

            assert subtotal == expected_subtotal
            assert tax == expected_tax
            assert total == expected_total

    @allure.story("页面异常跳转")
    @allure.title("异常情况进入最终结算页")
    def test_click_to_overview_without_info(self, driver, products_page):
        """异常情况：不输入买家信息，直接点击continue。测试结算第一步，跳转到结算第二步。"""
        with allure.step("前置操作：添加商品，进入结算流程"):
            product_name = "Sauce Labs Backpack"
            products_page.add_to_cart(product_name)
            cart_page = products_page.click_shopping_cart()
            cart_page.click_to_checkout()

        checkinfo_page = CheckInfoPage(driver)

        with allure.step("点击continue，验证进入最终结算页"):
            checkinfo_page.click_continue()
            error_text = checkinfo_page.get_error_text()

            assert 'is required' in error_text, f"测试失败，期望'is required'，实际{error_text}"


