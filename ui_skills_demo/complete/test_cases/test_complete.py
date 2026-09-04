"""
结算完成页测试用例
"""
import allure
import pytest

from ui_skills_demo.complete.pages.checkinfo_page import CheckInfoPage
from ui_skills_demo.complete.pages.complete_page import CompletePage
from ui_skills_demo.complete.pages.overview_page import OverviewPage


@allure.feature("结算完成页")
class TestComplete:

    @allure.story("页面跳转")
    @allure.title("完成页返回到商品页")
    def test_back_to_products(self, driver, products_page):
        """结算完成页，点击返回商品页"""
        with allure.step("前置操作：添加商品，进入结算流程"):
            product_name = "Sauce Labs Backpack"
            products_page.add_to_cart(product_name)
            cart_page = products_page.click_shopping_cart()

        with allure.step("买家信息页输入买家信息后，进入最终结算页"):
            cart_page.click_to_checkout()
            checkinfo_page = CheckInfoPage(driver)
            checkinfo_page.input_first_name('Jim')
            checkinfo_page.input_last_name('Green')
            checkinfo_page.input_post_code('03356')
            checkinfo_page.click_continue()

        with allure.step("最终结算页点击下一步，进入结算完成页"):
            overview_page = OverviewPage(driver)
            overview_page.finish()

        with allure.step("结算完成页点击返回，验证回到商品页"):
            complete_page = CompletePage(driver)
            complete_page.back_to_home()

            title = products_page.get_page_title()
            product_list = products_page.get_products_list()

            assert '/inventory.html' in driver.current_url, f"url不匹配，期望'/inventory.html'，实际{driver.current_url}"
            assert 'Products' in title, f"标题不匹配，期望'Products'，实际{title}"
            assert len(product_list) > 0, f"商品列表为0"
