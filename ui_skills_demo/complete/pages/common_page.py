"""
购物车通用操作
"""
from ui_skills_demo.complete.locators.common_locators import CommonLocators
from ui_skills_demo.complete.pages.base_page import BasePage
from ui_skills_demo.complete.utils.log_util import swag_logger


class CommonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.common_locators = CommonLocators()

    def click_shopping_cart(self):
        """点击购物车角标"""
        from ui_skills_demo.complete.pages.cart_page import CartPage

        self.click(self.common_locators.SHOPPING_CART)
        return CartPage(self.driver)

    def get_badge_amount(self):
        """获取购物车商品数量"""

        badge_amount = self.find_elements(self.common_locators.SHOPPING_CART_BADGE)
        swag_logger.info(f"badge_amount: {badge_amount}")

        if len(badge_amount) > 0:
            swag_logger.info(int(badge_amount[0].text))
            return int(badge_amount[0].text)
        else:
            return 0

        """
                if not badge_amount:
            return 0
        else:
            swag_logger.info(f"badge_amount[0].text: {int(badge_amount[0].text)}")
            return int(badge_amount[0].text)
        """


