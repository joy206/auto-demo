"""
结算总览页 页面操作封装
"""
import re

from ui_skills_demo.complete.locators.overview_locators import OverviewLocators
from ui_skills_demo.complete.pages.common_page import CommonPage


class OverviewPage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.overview_locators = OverviewLocators()

    def get_subtotal(self):
        """获取商品价格"""
        price = self.get_text(self.overview_locators.ITEM_TOTAL_PRICE)
        re_price = re.search(r'\d+\.\d+', price).group()
        return float(re_price)

    def get_tax(self):
        """获取税费"""
        tax = self.get_text(self.overview_locators.TAX_PRICE)
        re_tax = re.search(r'\d+\.\d+', tax).group()
        return float(re_tax)

    def get_total(self):
        """获取加税费后的总价格"""
        total_price = self.get_text(self.overview_locators.TOTAL_PRICE)
        re_total_price = re.search(r'\d+\.\d+', total_price).group()
        return float(re_total_price)

    def cancel(self):
        """点击取消按钮，返回商品页"""
        self.click(self.overview_locators.BTN_CANCEL)

    def finish(self):
        """finish按钮，进入结算完成页"""
        self.click(self.overview_locators.BTN_FINISH)
    
