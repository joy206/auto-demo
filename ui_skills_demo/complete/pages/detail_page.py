"""
商品详情页封装
"""
from ui_skills_demo.complete.locators.detail_locators import DetailLocators
from ui_skills_demo.complete.pages.common_page import CommonPage
from ui_skills_demo.complete.utils.log_util import swag_logger


class DetailPage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.detail_locators = DetailLocators()
        swag_logger.debug('DetailPage页面实例化成功')

    def get_detail_product_name(self):
        """获取详情页中的商品名"""
        product_name = self.get_text(self.detail_locators.DETAIL_PRODUCT_NAME)
        return product_name

    def get_detail_product_price(self):
        """获取详情页中的商品价格"""
        product_price = self.get_text(self.detail_locators.DETAIL_PRODUCT_PRICE)
        return float(product_price.replace('$', ''))

    def detail_add_to_cart(self):
        """在详情页中，把商品添加到购物车里"""
        self.click(self.detail_locators.DETAIL_ADD_TO_CART)

    def detail_remove_from_cart(self):
        """在详情页中，把商品从购物车中移除"""
        self.click(self.detail_locators.DETAIL_REMOVE_FROM_CART)

    def detail_back_to_products(self):
        """详情页返回商品页"""
        self.click(self.detail_locators.BACK_TO_PRODUCTS)


