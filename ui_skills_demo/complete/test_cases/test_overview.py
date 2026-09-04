"""
结算总览页测试用例
"""
import allure
import pytest
from ui_skills_demo.complete.pages.checkinfo_page import CheckInfoPage
from ui_skills_demo.complete.pages.complete_page import CompletePage
from ui_skills_demo.complete.pages.overview_page import OverviewPage


@allure.feature("最终结算页")
class TestOverview:

    @allure.story("页面跳转")
    @allure.step("最终结算页进入完成页")
    def test_finish_to_complete(self, driver, products_page):
        """结算总览页，点击进入结算完成页"""
        with allure.step("前置操作：添加商品，进入买家信息页"):
            product_name = "Sauce Labs Backpack"
            products_page.add_to_cart(product_name)
            cart_page = products_page.click_shopping_cart()
            cart_page.click_to_checkout()

        checkinfo_page = CheckInfoPage(driver)

        with allure.step("买家信息页输入信息后，进入最终结算页"):
            checkinfo_page.input_first_name('Jim')
            checkinfo_page.input_last_name('Green')
            checkinfo_page.input_post_code('03356')
            checkinfo_page.click_continue()

        overview_page = OverviewPage(driver)
        with allure.step("最终结算页点击finish，验证进入结算完成页"):
            overview_page.finish()

            complete_page = CompletePage(driver)
            title = complete_page.get_page_title()
            text = complete_page.get_desc()

            assert 'checkout-complete.html' in driver.current_url, f"url不匹配，期望'checkout-complete.html'，实际{driver.current_url}"
            assert 'Complete' in title, f"标题不匹配，期望'Complete'，实际{title}"
            assert 'Thank you for your order' in text, f"描述不匹配，期望'Thank you for your order'，实际{text}"

    @allure.story("页面跳转")
    @allure.step("最终结算页返回商品页")
    def test_cancel_to_products(self, driver, products_page):
        """结算总览页，返回到商品页"""
        with allure.step("前置操作：添加商品，进入买家信息页"):
            product_name = "Sauce Labs Backpack"
            products_page.add_to_cart(product_name)
            cart_page = products_page.click_shopping_cart()

            cart_page.click_to_checkout()
        checkinfo_page = CheckInfoPage(driver)

        with allure.step("买家信息页输入信息后，进入最终结算页"):
            checkinfo_page.input_first_name('Jim')
            checkinfo_page.input_last_name('Green')
            checkinfo_page.input_post_code('03356')
            checkinfo_page.click_continue()

        overview_page = OverviewPage(driver)
        with allure.step("最终结算页点击cancel，验证返回商品页"):
            overview_page.cancel()

            title = products_page.get_page_title()
            product_list = products_page.get_products_list()

            assert '/inventory.html' in driver.current_url, f"url不匹配，期望'/inventory.html'，实际{driver.current_url}"
            assert 'Products' in title, f"标题不匹配，期望'Products'，实际{title}"
            assert len(product_list) > 0, f"商品列表为0"