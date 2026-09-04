"""
验证各页面跳转到购物车
"""
import allure
import pytest
from ui_skills_demo.complete.pages.checkinfo_page import CheckInfoPage
from ui_skills_demo.complete.pages.complete_page import CompletePage
from ui_skills_demo.complete.pages.overview_page import OverviewPage
from ui_skills_demo.complete.utils.log_util import swag_logger


@allure.feature("购物车——页面跳转")
class TestNavigateToCart:
    """页面跳转"""

    @allure.story("页面跳转")
    @allure.title("从商品页跳转到购物车页面")
    def test_from_products_page(self, products_page):
        """从商品页跳转到购物车页"""
        with allure.step("商品页点击购物车，验证跳转到购物车页面"):
            cart_page = products_page.click_shopping_cart()
            url = cart_page.get_url()
            cart_title = cart_page.get_cart_page_title()

            assert '/cart.html' in url
            assert 'Your Cart' == cart_title

    @allure.story("页面跳转")
    @allure.title("从商品详情页，跳转到购物车页面")
    def test_from_detail_page(self, products_page, detail_page):
        """从商品详情页跳转到购物车页"""
        with allure.step("商品页点击进入详情页"):
            products_page.click_first_product_name_to_detail()

        with allure.step("详情页点击购物车，验证跳转到购物车页面"):
            cart_page = detail_page.click_shopping_cart()
            url = cart_page.get_url()
            cart_title = cart_page.get_cart_page_title()

            assert '/cart.html' in url
            assert 'Your Cart' == cart_title


@allure.feature("购物车——端到端验证")
class TestAddToCartE2E:
    """验证从不同页面，添加商品到购物车"""

    @allure.story("商品端—购物车端")
    @allure.title("商品页添加商品，购物车页验证商品信息")
    def test_add_single_from_inventory(self, products_page):
        """从商品列表添加单个商品"""
        with allure.step("添加商品到购物车"):
            product_name = "Sauce Labs Backpack"
            price = products_page.get_product_price_by_name(product_name)
            expected = {
                "name": product_name,
                "price": price
            }
            products_page.add_to_cart(product_name)

        with allure.step("进入购物车验证商品名和价格"):
            cart_page = products_page.click_shopping_cart()
            # 2. 购物车拿到的是列表，但每个元素是对象/字典
            # [{"name": "...", "price": "..."}, ...]
            cart_items = cart_page.get_cart_items()
            # 3. 用 any() 做"存在且匹配"
            assert any(
                item["name"] == expected["name"] and item["price"] == expected["price"]
                for item in cart_items
            )

    @allure.story("商品端—购物车端")
    @allure.title("商品页添加多个商品，购物车页验证商品信息")
    def test_add_multiple_from_inventory(self, products_page):
        """从商品列表添加多个商品"""
        with allure.step("添加多个商品到购物车"):
            product_list = [
                "Sauce Labs Backpack",
                "Sauce Labs Bike Light",
                "Sauce Labs Bolt T-Shirt"
            ]

            expected_items = []

            for p in product_list:
                swag_logger.info(p)
                price = products_page.get_product_price_by_name(p)
                expected_items.append({
                    "name": p,
                    "price": price,
                })
                products_page.add_to_cart(p)

        with allure.step("进入购物车验证商品名和价格"):
            cart_page = products_page.click_shopping_cart()
            cart_items = cart_page.get_cart_items()

            for expected in expected_items:
                assert any(
                    item["name"] == expected["name"] and item["price"] == expected["price"]
                    for item in cart_items
                ), f"购物车中未找到商品：{expected['name']}"

    @allure.story("详情页端—购物车端")
    @allure.title("详情页添加商品，购物车页验证商品信息")
    def test_add_from_detail(self, products_page, detail_page):
        """从详情页添加商品"""
        with allure.step("进入详情页，添加商品到购物车中"):
            products_page.click_first_product_name_to_detail()
            product_name = detail_page.get_detail_product_name()
            product_price = detail_page.get_detail_product_price()
            detail_page.detail_add_to_cart()

            expected = {
                "name": product_name,
                "price": product_price
            }

        with allure.step("进入购物车，验证商品名称和价格"):
            cart_page = detail_page.click_shopping_cart()
            cart_items = cart_page.get_cart_items()
            assert any(
                item['name'] == expected['name'] and item['price'] == expected['price']
                for item in cart_items
            ), f"购物车中未找到商品{expected['name']}"


@allure.feature("全流程")
class TestPurchaseFlow:
    """全流程"""

    @allure.story("全流程测试")
    @allure.title("添加商品到完整结算的流程")
    def test_purchase_flow(self, driver, products_page):
        """全流程"""
        with allure.step("商品页添加商品，进入购物车页"):
            product_name = "Sauce Labs Backpack"
            products_page.add_to_cart(product_name)
            cart_page = products_page.click_shopping_cart()

        with allure.step("购物车进入买家信息页，输入基本信息"):
            cart_page.click_to_checkout()
            checkinfo_page = CheckInfoPage(driver)

            checkinfo_page.input_first_name('Jim')
            checkinfo_page.input_last_name('Green')
            checkinfo_page.input_post_code('03356')

        with allure.step("买家信息页进入最终结算页"):
            checkinfo_page.click_continue()

        overview_page = OverviewPage(driver)
        with allure.step("最终结算页点击finish，进入结算完成页"):
            overview_page.finish()

        complete_page = CompletePage(driver)
        with allure.step("结算完成页点击返回，验证回到商品页"):
            complete_page.back_to_home()
            badge_amount = products_page.get_badge_amount()

            assert '/inventory.html' in driver.current_url, f"url不匹配，期望'/inventory.html'，实际{driver.current_url}"
            assert badge_amount == 0, f"购物车未清空，期望0，实际{badge_amount}"




