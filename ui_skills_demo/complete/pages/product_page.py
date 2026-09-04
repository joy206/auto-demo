"""
商品页操作封装
"""
from ui_skills_demo.complete.locators.products_locators import ProductsLocators
from ui_skills_demo.complete.pages.common_page import CommonPage
from ui_skills_demo.complete.utils.log_util import swag_logger


class ProductPage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.product_locators = ProductsLocators()
        swag_logger.debug("初始化ProductPage")

    def get_page_title(self):
        """获取商品页页面标题"""
        return self.get_text(self.product_locators.TITLE)

    def get_products_list(self):
        """获取商品列表"""
        products_list = self.find_elements(self.product_locators.PRODUCT_NAME)
        return products_list

    def add_to_cart(self, product_name):
        """把商品添加到购物车中"""
        format_product = product_name.lower().replace(' ', "-")
        final_locator = self.get_dynamic_locator(
            self.product_locators.ADD_TO_CART_BTN,
            product_name=format_product,
        )
        self.click(final_locator)

    def remove_from_cart(self, product_name):
        """把商品从购物车中移除"""
        format_product = product_name.lower().replace(' ', "-")
        final_locator = self.get_dynamic_locator(
            self.product_locators.REMOVE_FROM_CART_BTN,
            product_name=format_product
        )
        self.click(final_locator)

    def order_by_name_asc(self):
        """根据商品名字 A~Z 升序排列"""
        self.select_dropdown(self.product_locators.PRODUCTS_SELECT, self.product_locators.NAME_ASC)

    def order_by_name_desc(self):
        """根据商品名字 Z~A 降序排列"""
        self.select_dropdown(self.product_locators.PRODUCTS_SELECT, self.product_locators.NAME_DESC)

    def order_by_price_asc(self):
        """根据商品价格由 低到高 排列"""
        self.select_dropdown(self.product_locators.PRODUCTS_SELECT, self.product_locators.PRICE_ASC)

    def order_by_price_desc(self):
        """根据商品价格由 高到低 排列"""
        self.select_dropdown(self.product_locators.PRODUCTS_SELECT, self.product_locators.PRICE_DESC)

    def get_product_names(self):
        """获取 商品名 列表（排序用）"""
        products_list = self.find_elements_visible(self.product_locators.PRODUCT_NAME)
        return [p.text for p in products_list]

    def get_product_prices(self):
        """获取 商品价格 列表（排序用）"""
        prices_list = self.find_elements_visible(self.product_locators.PRODUCT_PRICE)
        return [float(p.text.replace('$', '')) for p in prices_list]

    def get_first_product_name(self):
        """获取第一个商品名"""
        elements = self.find_elements_visible(self.product_locators.PRODUCT_NAME)
        first_product_name = elements[0].text if elements else None
        print(f"first_product_name: {first_product_name}, elements[0].text: {elements[0].text}")
        return first_product_name

    def get_first_product_price(self):
        """获取第一个商品的商品价格"""
        elements = self.find_elements_visible(self.product_locators.PRODUCT_PRICE)
        first_product_price = elements[0].text if elements else None
        return float(first_product_price.replace('$', ''))

    def get_product_price_by_name(self, product_name):
        """根据商品名，获取商品价格"""
        final_locator = self.get_dynamic_locator(
            self.product_locators.APPOINTED_PRODUCT_PRICE,
            product_name=product_name
        )
        price = self.get_text(final_locator)
        return float(price.replace('$', ''))

    def click_first_product_name_to_detail(self):
        """点击第一个商品名，跳转到商品详情页"""
        self.click(self.product_locators.PRODUCT_NAME)

    def click_first_product_image_to_detail(self):
        """点击第一个商品的图片，跳转到商品详情页"""
        self.click(self.product_locators.PRODUCT_IMAGE)

    def click_appointed_product_name_to_detail(self, product_name):
        """点击指定商品名，跳转到商品详情页"""
        final_locator = self.get_dynamic_locator(
            self.product_locators.APPOINTED_PRODUCT_NAME,
            product_name=product_name
        )
        self.click(final_locator)

    def click_appointed_product_image_to_detail(self, product_name):
        """点击指定商品图片，跳转到该商品详情页"""
        final_locator = self.get_dynamic_locator(
            self.product_locators.APPOINTED_PRODUCT_IMAGE,
            product_name=product_name,
        )
        self.click(final_locator)







