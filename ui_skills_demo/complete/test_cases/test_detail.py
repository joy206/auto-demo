"""
商品详情页测试用例
"""
import allure
import pytest
from ui_skills_demo.complete.pages.detail_page import DetailPage


@allure.feature("商品详情页")
class TestDetail:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("添加商品")
    @allure.title("添加商品到购物车中")
    def test_detail_add_to_cart(self, products_page, detail_page):
        """详情页测试，把商品添加到详情页中"""
        with allure.step("进入详情页"):
            products_page.click_first_product_name_to_detail()

        with allure.step("详情页添加商品到购物车，并断言购物车角标数量"):
            detail_page.detail_add_to_cart()
            amount = detail_page.get_badge_amount()
            assert amount == 1, f"数量不匹配，期望1，实际{amount}"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("移除商品")
    @allure.title("把商品从购物车中移除")
    def test_detail_remove_from_cart(self, products_page, detail_page):
        """详情页测试，详情页把商品移除购物车"""
        with allure.step("进入详情页，添加商品到购物车中"):
            products_page.click_first_product_name_to_detail()
            detail_page.detail_add_to_cart()

        with allure.step("把商品从购物车中移除，断言购物车角标为0"):
            detail_page.detail_remove_from_cart()
            amount = detail_page.get_badge_amount()
            assert amount == 0, f"数量不匹配，期望0，实际{amount}"

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip("已通过，暂不测")
    @allure.story("页面跳转")
    @allure.title("返回到商品页")
    def test_back_to_product_page(self, driver, products_page, detail_page):
        """详情页返回商品页"""
        with allure.step("进入详情页"):
            products_page.click_first_product_name_to_detail()

        with allure.step("详情页点击返回，验证返回到购物车页面"):
            detail_page.detail_back_to_products()
            title = products_page.get_page_title()
            product_list = products_page.get_products_list()
            assert '/inventory-item.html?id=' not in driver.current_url, f"url不匹配，实际{driver.current_url}"
            assert title == 'Products', f"标题不匹配，期望'Products'，实际{title}"
            assert len(product_list) > 0, f"商品列表为空"


