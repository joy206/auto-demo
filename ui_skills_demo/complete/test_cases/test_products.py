"""
商品页测试用例
"""
import allure
import pytest

from ui_skills_demo.complete.pages.detail_page import DetailPage
from ui_skills_demo.complete.utils.log_util import swag_logger


@allure.feature("商品模块")
class TestProducts:

    @pytest.mark.parametrize(
        "sort_action, sort_method, reverse, desc",
        [
            ("order_by_name_asc", "get_product_names", False, "按名字a~z"),
            ("order_by_name_desc", "get_product_names", True, "按名字z~a"),
            ("order_by_price_asc", "get_product_prices", False, "按价格low~high"),
            ("order_by_price_desc", "get_product_prices", True, "按价格high~low"),
        ],
        ids=["name-asc", "name-desc", "price-low_to_high", "price-high_to_low"]
    )
    @allure.story("商品排序")
    @allure.title("商品排序")
    def test_sort_products(self, products_page, sort_action, sort_method, reverse, desc):
        """商品排序"""
        with allure.step(f"选择排序的方式: {desc}"):
            getattr(products_page, sort_action)()

        with allure.step("获取并验证排序结果"):
            actual_result = getattr(products_page, sort_method)()
            expected_result = sorted(actual_result, reverse=reverse)
            assert actual_result == expected_result, f"用例【{desc}】排序结果与预期不符合，预期{expected_result}, 实际{actual_result}"

    @allure.story("添加商品到购物车")
    @allure.title("添加单个商品到购物车")
    def test_add_product_to_cart(self, products_page):
        """添加单个商品到购物车中"""
        with allure.step("添加商品到购物车"):
            products_page.add_to_cart("Sauce Labs Backpack")
        with allure.step("验证购物车商品数量"):
            amount = products_page.get_badge_amount()
            assert amount == 1, f"购物商品数量不匹配，期望1，实际{amount}"

    @allure.story("添加商品到购物车")
    @allure.title("添加多个商品到购物车")
    def test_add_multi_products_to_cart(self, products_page):
        """添加多个商品到购物车中"""
        with allure.step("添加多个商品到购物车"):
            products_list = [
                "Sauce Labs Backpack",
                "Sauce Labs Bike Light",
                "Sauce Labs Bolt T-Shirt"
            ]
            for p in products_list:
                products_page.add_to_cart(p)

        with allure.step("断言购物车中的商品数量"):
            amount = products_page.get_badge_amount()
            assert amount == 3, f"购物商品数量不匹配，期望3，实际{amount}"

    @allure.story("把商品从购物车中移除")
    @allure.title("把商品从购物车中移除")
    def test_remove_product_from_cart(self, products_page):
        """把商品从购物车中移除"""
        with allure.step("添加单个商品到购物车中"):
            products_page.add_to_cart("Sauce Labs Backpack")
        with allure.step("把指定商品从购物车中移除"):
            products_page.remove_from_cart("Sauce Labs Backpack")
        with allure.step("验证购物车中商品数量"):
            amount = products_page.get_badge_amount()
            assert amount == 0, f"购物商品数量不匹配，期望0，实际{amount}"

    @allure.story("把多个商品从购物车中移除")
    @allure.title("把多个商品从购物车中移除")
    def test_remove_multi_products_to_cart(self, products_page):
        """把多个商品从购物车中移除"""
        with allure.step("添加多个商品到购物车"):
            products_list = [
                "Sauce Labs Backpack",
                "Sauce Labs Bike Light",
                "Sauce Labs Bolt T-Shirt"
            ]
            for p in products_list:
                products_page.add_to_cart(p)

        with allure.step("把多个商品从购物车中移除"):
            for p in products_list:
                products_page.remove_from_cart(p)
        with allure.step("验证购物车中的商品数量"):
            amount = products_page.get_badge_amount()
            assert amount == 0, f"购物商品数量不匹配，期望0，实际{amount}"

    @allure.story("跳转到商品详情页")
    @allure.title("点击列表中的第一个商品名跳转")
    def test_first_product_name_to_detail(self, driver, products_page):
        """点击第一个商品名，跳转到该商品详情页"""
        with allure.step("点击第一个商品"):
            first_product_name = products_page.get_first_product_name()
            first_product_price = products_page.get_first_product_price()
            products_page.click_first_product_name_to_detail()
        with allure.step("验证跳转到详情页"):
            detail_page = DetailPage(driver)
            detail_product_name = detail_page.get_detail_product_name()
            detail_price = detail_page.get_detail_product_price()

            assert '/inventory-item.html?id=' in driver.current_url, f"url不匹配，期望'/inventory-item.html?id='，实际{driver.current_url}"
            assert detail_product_name == first_product_name, f"商品名不匹配，期望{first_product_name}，实际{detail_product_name}"
            assert abs(detail_price - first_product_price) < 0.01, f"价格不匹配，期望{first_product_price}，实际{detail_price}"

    @allure.story("跳转到商品详情页")
    @allure.title("点击指定商品名跳转")
    def test_appointed_product_name_to_detail(self, driver, products_page):
        """点击指定商品名，跳转到该商品详情页"""
        product_name = "Sauce Labs Onesie"
        with allure.step(f"点击指定商品名:{product_name}"):
            product_price = products_page.get_product_price_by_name("Sauce Labs Onesie")
            products_page.click_appointed_product_name_to_detail(product_name)
        with allure.step("验证跳转到商品详情页"):
            detail_page = DetailPage(driver)
            detail_product_name = detail_page.get_detail_product_name()
            detail_price = detail_page.get_detail_product_price()

            assert '/inventory-item.html?id=' in driver.current_url, f"url不匹配，期望'/inventory-item.html?id='，实际{driver.current_url}"
            assert detail_product_name == product_name, f"商品名不匹配，期望{product_name}，实际{detail_product_name}"
            assert abs(detail_price - product_price) < 0.01, f"价格不匹配，期望{product_price}，实际{detail_price}"

    @allure.story("跳转到商品详情页")
    @allure.title("点击第一个商品图片跳转")
    def test_first_product_image_to_detail(self, driver, products_page):
        """点击第一个商品的图片，跳转到该商品详情页"""
        with allure.step("点击第一个商品的图片"):
            product_name = products_page.get_first_product_name()
            product_price = products_page.get_first_product_price()
            products_page.click_first_product_image_to_detail()

        with allure.step("验证详情页跳转"):
            detail_page = DetailPage(driver)
            detail_product_name = detail_page.get_detail_product_name()
            detail_product_price = detail_page.get_detail_product_price()
            assert '/inventory-item.html?id=' in driver.current_url, f"url不匹配，期望'/inventory-item.html?id='，实际{driver.current_url}"
            assert detail_product_name == product_name, f"商品名不匹配，期望{product_name}，实际{detail_product_name}"
            assert abs(detail_product_price - product_price) < 0.01, f"价格不匹配，期望{product_price}，实际{detail_product_price}"

    @allure.story("跳转到商品详情页")
    @allure.title("点击指定商品图片，跳转到该商品详情页")
    def test_appointed_product_image_to_detail(self, driver, products_page):
        """点击任意商品图片，跳转到商品详情页"""
        product_name = "Sauce Labs Bike Light"
        with allure.step(f"点击指定商品{product_name}的图片，进入商品详情页"):
            product_price = products_page.get_product_price_by_name(product_name)
            products_page.click_appointed_product_name_to_detail(product_name)
        with allure.step("验证详情页跳转"):
            detail_page = DetailPage(driver)
            detail_product_name = detail_page.get_detail_product_name()
            detail_product_price = detail_page.get_detail_product_price()
            assert '/inventory-item.html?id=' in driver.current_url, f"url不匹配，期望'/inventory-item.html?id='，实际{driver.current_url}"
            assert detail_product_name == product_name, f"商品名不匹配，期望{product_name}，实际{detail_product_name}"
            assert abs(
                detail_product_price - product_price) < 0.01, f"价格不匹配，期望{product_price}，实际{detail_product_price}"














