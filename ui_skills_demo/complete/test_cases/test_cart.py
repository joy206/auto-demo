"""
购物车页面测试用例
"""
import allure
import pytest
from ui_skills_demo.complete.pages.checkinfo_page import CheckInfoPage
from ui_skills_demo.complete.utils.log_util import swag_logger


@allure.feature("购物车模块")
class TestCart:

    @allure.story("购物车角标")
    @allure.title("验证购物车角标数量显示正确")
    def test_assert_badge_amount(self, products_page):
        """验证购物车角标商品数量"""
        with allure.step("添加1件商品到购物车中，进入购物车页面"):
            products_page.add_to_cart("Sauce Labs Backpack")
            cart_page = products_page.click_shopping_cart()

        with allure.step("断言购物车角标和列表数量均为1"):
            amount = cart_page.get_badge_amount()
            assert amount == 1, f"数量不匹配，期望1，实际数量{amount}"
            cart_list = cart_page.get_cart_list_amount()
            assert cart_list == 1, f"数量不匹配，期望1，实际数量{cart_list}"

    @allure.story("移除商品")
    @allure.title("移除单个商品")
    def test_remove_product(self, products_page):
        """购物车页面，移除单个商品"""
        with allure.step("添加1件商品，并进入购物车页面"):
            products_page.add_to_cart("Sauce Labs Backpack")
            cart_page = products_page.click_shopping_cart()

        with allure.step("从购物车中移除1件商品，并验证购物车为空"):
            cart_page.cart_remove_by_name("Sauce Labs Backpack")
            amount = cart_page.get_badge_amount()
            cart_list = cart_page.get_cart_list_amount()
            assert amount == 0, f"购物车角标数量不匹配，实际{amount}"
            assert cart_list == 0, f"商品数量不匹配，实际{cart_list}"

    @allure.story("移除商品")
    @allure.title("移除多个商品")
    def test_remove_multiple_products(self, products_page):
        """购物车页面，移除多个商品"""
        with allure.step("添加多个商品，进入购物车页面"):
            products_page.add_to_cart("Sauce Labs Backpack")
            products_page.add_to_cart("Sauce Labs Bike Light")
            products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
            cart_page = products_page.click_shopping_cart()

        with allure.step("移除购物车中的商品，并验证购物车角标数量和商品列表数量"):
            cart_page.cart_remove_by_name("Sauce Labs Backpack")
            cart_page.cart_remove_by_name("Sauce Labs Bike Light")
            amount = cart_page.get_badge_amount()
            cart_list = cart_page.get_cart_list_amount()

            assert amount == 1, f"购物车角标数量不匹配，期望1，实际{amount}"
            assert cart_list == 1, f"商品数量不匹配，实际{cart_list}"

    @allure.story("页面跳转")
    @allure.title("从购物车页面，返回商品页")
    def test_back_to_shopping(self, driver, products_page):
        """购物车页面，点击后返回商品页"""
        with allure.step("进入购物车页面"):
            cart_page = products_page.click_shopping_cart()
        with allure.step("点击返回，验证回到商品列表页"):
            cart_page.back_to_shopping()
            url = driver.current_url
            title = products_page.get_page_title()
            product_list = products_page.get_products_list()

            assert '/inventory.html' in url, f"url不匹配，实际{url}"
            assert title == 'Products', f"标题不匹配"
            assert len(product_list) > 0, f"商品列表为0"

    @allure.story("页面跳转")
    @allure.title("从购物车页面，进入结算页")
    def test_checkout(self, driver, products_page):
        """购物车页面，点击后进入结算页（第一步：填买家信息）"""
        with allure.step("添加商品后，进入购物车页面"):
            products_page.add_to_cart("Sauce Labs Backpack")
            cart_page = products_page.click_shopping_cart()
        with allure.step("点击下一步，验证进入结算页"):
            cart_page.click_to_checkout()
            checkInfo_page = CheckInfoPage(driver)
            title = checkInfo_page.get_page_title()

            assert '/checkout-step-one.html' in driver.current_url, f"url不匹配"
            assert title == 'Checkout: Your Information', f"标题不匹配"