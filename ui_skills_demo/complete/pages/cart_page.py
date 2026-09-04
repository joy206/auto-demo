"""
购物车页面操作封装
"""
from ui_skills_demo.complete.locators.cart_locators import CartLocators
from ui_skills_demo.complete.pages.checkinfo_page import CheckInfoPage
from ui_skills_demo.complete.pages.common_page import CommonPage
from ui_skills_demo.complete.utils.log_util import swag_logger


class CartPage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.cart_locators = CartLocators()

    def get_cart_list_amount(self):
        """获取购物车列表中的商品数量"""
        cart_list = self.find_elements(self.cart_locators.CART_PRODUCT_NAME)
        return len(cart_list)

    def cart_remove_by_name(self, product_name):
        """购物车页面，移除商品"""
        product_name_format = product_name.lower().replace(' ', '-')
        locator = self.get_dynamic_locator(
            self.cart_locators.CART_REMOVE,
            product_name=product_name_format,
        )
        self.click(locator)

    def back_to_shopping(self):
        """从购物车页面，返回到商品页"""
        self.click(self.cart_locators.BTN_CONTINUE_SHOPPING)

    def get_cart_page_title(self):
        """获取购物车页面标题"""
        return self.get_text(self.cart_locators.CART_TITLE)

    def click_to_checkout(self):
        """购物车页面，点击后跳转到结算前准备页"""
        self.click(self.cart_locators.BTN_CHECKOUT)

    def get_cart_items(self):
        """获取购物车所有条目，返回字典列表"""
        items = []
        rows = self.find_elements(self.cart_locators.CART_ITEM)

        for row in rows:
            name = self.get_text(self.cart_locators.CART_PRODUCT_NAME, root=row)
            price = self.get_text(self.cart_locators.CART_PRODUCT_PRICE, root=row)
            items.append({
                "name": name,
                "price": float(price.replace('$', ''))
            })
        return items

    
